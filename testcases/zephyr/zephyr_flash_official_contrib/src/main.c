/*
 * Zephyr官方Flash驱动测试用例 - 用于开源贡献
 * 基于Zephyr官方SPI Flash示例，包含MMIO操作
 * 目标：支持flash的ARM板子（STM32F103C8T6 Blue Pill）
 * 
 * SPDX-License-Identifier: Apache-2.0
 */

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>
#include <string.h>
#include <stdio.h>

/* Zephyr风格的类型定义 */
typedef uint8_t u8_t;
typedef uint16_t u16_t;
typedef uint32_t u32_t;
typedef int32_t s32_t;

/* STM32 Flash寄存器定义 - 用于直接的MMIO操作 */
typedef struct {
    volatile u32_t ACR;     /* Flash访问控制寄存器 */
    volatile u32_t KEYR;    /* Flash密钥寄存器 */
    volatile u32_t OPTKEYR; /* 选项字节密钥寄存器 */
    volatile u32_t SR;      /* 状态寄存器 */
    volatile u32_t CR;      /* 控制寄存器 */
    volatile u32_t AR;      /* 地址寄存器 */
    volatile u32_t RESERVED;
    volatile u32_t OBR;     /* 选项字节寄存器 */
    volatile u32_t WRPR;    /* 写保护寄存器 */
} FLASH_TypeDef;

/* STM32 Flash基地址 */
#define FLASH_BASE 0x40022000UL
#define FLASH ((FLASH_TypeDef *)FLASH_BASE)

/* Flash操作密钥 */
#define FLASH_KEY1 0x45670123UL
#define FLASH_KEY2 0xCDEF89ABUL

/* Flash状态标志 */
#define FLASH_SR_BSY   (1 << 0)  /* 忙标志 */
#define FLASH_SR_PGERR (1 << 2)  /* 编程错误 */
#define FLASH_SR_WRPRTERR (1 << 4) /* 写保护错误 */
#define FLASH_SR_EOP   (1 << 5)  /* 操作结束 */

/* Flash控制位 */
#define FLASH_CR_PG    (1 << 0)  /* 编程 */
#define FLASH_CR_PER   (1 << 1)  /* 页擦除 */
#define FLASH_CR_MER   (1 << 2)  /* 批量擦除 */
#define FLASH_CR_OPTPG (1 << 4)  /* 选项字节编程 */
#define FLASH_CR_OPTER (1 << 5)  /* 选项字节擦除 */
#define FLASH_CR_STRT  (1 << 6)  /* 开始 */
#define FLASH_CR_LOCK  (1 << 7)  /* 锁定 */

/* Zephyr风格的状态码 */
#define EOK       0
#define EIO      -5
#define EINVAL   -22
#define ENODEV   -19
#define EBUSY    -16

/* Flash页大小 */
#define FLASH_PAGE_SIZE 1024  /* STM32F103: 1KB页 */
#define FLASH_TOTAL_SIZE 65536 /* 64KB */

/* 硬件抽象层函数 - 用于模拟器替换 */
int __attribute__((noinline, used, __weak__))HAL_BE_return_0(){
    return 0;
}

int __attribute__((noinline, used, __weak__))HAL_BE_return_1(){
    return 1;
}

int __attribute__((noinline, used, __weak__))HAL_BE_Out(int len){
    return len;
}

int __attribute__((noinline, used, __weak__)) HAL_BE_In(void* buf, int len){
    return len;
}

/* Flash解锁函数 */
static int flash_unlock(void)
{
    /* 检查是否已解锁 */
    if (!(FLASH->CR & FLASH_CR_LOCK)) {
        return EOK;
    }
    
    /* 写入解锁密钥序列 */
    FLASH->KEYR = FLASH_KEY1;
    FLASH->KEYR = FLASH_KEY2;
    
    /* 验证解锁 */
    if (FLASH->CR & FLASH_CR_LOCK) {
        return -EIO;
    }
    
    return EOK;
}

/* Flash锁定函数 */
static int flash_lock(void)
{
    FLASH->CR |= FLASH_CR_LOCK;
    return EOK;
}

/* 等待Flash操作完成 */
static int flash_wait_for_last_operation(void)
{
    /* 等待BSY标志清除 */
    while (FLASH->SR & FLASH_SR_BSY) {
        __asm__ volatile ("nop");
    }
    
    /* 检查错误标志 */
    if (FLASH->SR & (FLASH_SR_PGERR | FLASH_SR_WRPRTERR)) {
        /* 清除错误标志 */
        FLASH->SR |= (FLASH_SR_PGERR | FLASH_SR_WRPRTERR);
        return -EIO;
    }
    
    /* 清除EOP标志 */
    if (FLASH->SR & FLASH_SR_EOP) {
        FLASH->SR |= FLASH_SR_EOP;
    }
    
    return EOK;
}

/* Flash页擦除函数 */
static int flash_erase_page(u32_t page_address)
{
    int ret;
    
    /* 检查地址对齐 */
    if (page_address % FLASH_PAGE_SIZE != 0) {
        return -EINVAL;
    }
    
    /* 检查地址范围 */
    if (page_address >= FLASH_TOTAL_SIZE) {
        return -EINVAL;
    }
    
    /* 解锁Flash */
    ret = flash_unlock();
    if (ret != EOK) {
        return ret;
    }
    
    /* 等待之前的操作完成 */
    ret = flash_wait_for_last_operation();
    if (ret != EOK) {
        flash_lock();
        return ret;
    }
    
    /* 设置页擦除模式 */
    FLASH->CR |= FLASH_CR_PER;
    
    /* 设置页地址 */
    FLASH->AR = page_address;
    
    /* 开始擦除 */
    FLASH->CR |= FLASH_CR_STRT;
    
    /* 等待操作完成 */
    ret = flash_wait_for_last_operation();
    
    /* 清除页擦除模式 */
    FLASH->CR &= ~FLASH_CR_PER;
    
    /* 锁定Flash */
    flash_lock();
    
    return ret;
}

/* Flash编程函数（半字，16位） */
static int flash_program_half_word(u32_t address, u16_t data)
{
    int ret;
    
    /* 检查地址对齐 */
    if (address % 2 != 0) {
        return -EINVAL;
    }
    
    /* 检查地址范围 */
    if (address >= FLASH_TOTAL_SIZE) {
        return -EINVAL;
    }
    
    /* 解锁Flash */
    ret = flash_unlock();
    if (ret != EOK) {
        return ret;
    }
    
    /* 等待之前的操作完成 */
    ret = flash_wait_for_last_operation();
    if (ret != EOK) {
        flash_lock();
        return ret;
    }
    
    /* 设置编程模式 */
    FLASH->CR |= FLASH_CR_PG;
    
    /* 写入数据 */
    *((volatile u16_t *)address) = data;
    
    /* 等待操作完成 */
    ret = flash_wait_for_last_operation();
    
    /* 清除编程模式 */
    FLASH->CR &= ~FLASH_CR_PG;
    
    /* 锁定Flash */
    flash_lock();
    
    return ret;
}

/* Flash批量擦除函数 */
static int flash_mass_erase(void)
{
    int ret;
    
    /* 解锁Flash */
    ret = flash_unlock();
    if (ret != EOK) {
        return ret;
    }
    
    /* 等待之前的操作完成 */
    ret = flash_wait_for_last_operation();
    if (ret != EOK) {
        flash_lock();
        return ret;
    }
    
    /* 设置批量擦除模式 */
    FLASH->CR |= FLASH_CR_MER;
    
    /* 开始擦除 */
    FLASH->CR |= FLASH_CR_STRT;
    
    /* 等待操作完成 */
    ret = flash_wait_for_last_operation();
    
    /* 清除批量擦除模式 */
    FLASH->CR &= ~FLASH_CR_MER;
    
    /* 锁定Flash */
    flash_lock();
    
    return ret;
}

/* Flash读取函数 */
static int flash_read_data(u32_t address, void *buffer, u32_t size)
{
    if (!buffer || address >= FLASH_TOTAL_SIZE) {
        return -EINVAL;
    }
    
    /* 直接内存读取 */
    memcpy(buffer, (void *)address, size);
    
    return EOK;
}

/* 测试函数：单页擦除测试 */
static int test_flash_erase_single_page(void)
{
    u32_t test_address = 0x08004000;  /* 第16页 */
    u8_t read_buffer[16];
    int ret;
    
    printf("Test 1: Single Page Erase\n");
    
    /* 擦除页面 */
    ret = flash_erase_page(test_address);
    if (ret != EOK) {
        printf("  Error: Page erase failed (%d)\n", ret);
        return ret;
    }
    
    /* 读取并验证擦除状态（应为0xFF） */
    ret = flash_read_data(test_address, read_buffer, sizeof(read_buffer));
    if (ret != EOK) {
        printf("  Error: Read after erase failed (%d)\n", ret);
        return ret;
    }
    
    for (int i = 0; i < sizeof(read_buffer); i++) {
        if (read_buffer[i] != 0xFF) {
            printf("  Error: Byte at offset %d is not erased (0x%02X)\n", 
                   i, read_buffer[i]);
            return -EIO;
        }
    }
    
    printf("  Success: Page erased correctly\n");
    return EOK;
}

/* 测试函数：编程测试 */
static int test_flash_program(void)
{
    u32_t test_address = 0x08004000;
    u16_t test_data = 0x55AA;
    u16_t read_data;
    int ret;
    
    printf("Test 2: Flash Programming\n");
    
    /* 首先擦除页面 */
    ret = flash_erase_page(test_address);
    if (ret != EOK) {
        printf("  Error: Page erase failed for programming test\n");
        return ret;
    }
    
    /* 编程数据 */
    ret = flash_program_half_word(test_address, test_data);
    if (ret != EOK) {
        printf("  Error: Flash programming failed (%d)\n", ret);
        return ret;
    }
    
    /* 读取验证 */
    read_data = *((volatile u16_t *)test_address);
    if (read_data != test_data) {
        printf("  Error: Data mismatch: wrote 0x%04X, read 0x%04X\n",
               test_data, read_data);
        return -EIO;
    }
    
    printf("  Success: Flash programming verified\n");
    return EOK;
}

/* 测试函数：批量擦除测试 */
static int test_flash_mass_erase(void)
{
    u32_t test_addresses[] = {0x08000000, 0x08002000, 0x08004000, 0x08006000};
    int ret;
    
    printf("Test 3: Mass Erase\n");
    
    /* 批量擦除 */
    ret = flash_mass_erase();
    if (ret != EOK) {
        printf("  Error: Mass erase failed (%d)\n", ret);
        return ret;
    }
    
    /* 验证多个地址被擦除 */
    for (int i = 0; i < sizeof(test_addresses)/sizeof(test_addresses[0]); i++) {
        u8_t read_byte = *((volatile u8_t *)test_addresses[i]);
        if (read_byte != 0xFF) {
            printf("  Error: Address 0x%08X not erased (0x%02X)\n",
                   test_addresses[i], read_byte);
            return -EIO;
        }
    }
    
    printf("  Success: Mass erase verified\n");
    return EOK;
}

/* 测试函数：错误处理测试 */
static int test_flash_error_handling(void)
{
    int ret;
    
    printf("Test 4: Error Handling\n");
    
    /* 测试无效地址 */
    ret = flash_erase_page(0xFFFFFFFF);
    if (ret != -EINVAL) {
        printf("  Error: Invalid address not rejected\n");
        return -EIO;
    }
    
    /* 测试未对齐地址 */
    ret = flash_program_half_word(0x08000001, 0x1234);
    if (ret != -EINVAL) {
        printf("  Error: Unaligned address not rejected\n");
        return -EIO;
    }
    
    printf("  Success: Error handling works correctly\n");
    return EOK;
}

/* 简单的打印函数 */
void simple_print(const char *str)
{
    /* 简化打印实现 */
    (void)str;
}

/* 主函数 */
int main(void)
{
    int ret;
    
    simple_print("\n========================================\n");
    simple_print("Zephyr Flash Driver Test for Open Source Contribution\n");
    simple_print("Target: STM32F103C8T6 (Blue Pill) Internal Flash\n");
    simple_print("Flash Size: 64KB, Page Size: 1KB\n");
    simple_print("========================================\n\n");
    
    simple_print("Running flash driver test suite...\n\n");
    
    /* 运行测试套件 */
    ret = test_flash_erase_single_page();
    if (ret != EOK) {
        simple_print("Flash test suite failed at test 1\n");
        return ret;
    }
    
    ret = test_flash_program();
    if (ret != EOK) {
        simple_print("Flash test suite failed at test 2\n");
        return ret;
    }
    
    ret = test_flash_mass_erase();
    if (ret != EOK) {
        simple_print("Flash test suite failed at test 3\n");
        return ret;
    }
    
    ret = test_flash_error_handling();
    if (ret != EOK) {
        simple_print("Flash test suite failed at test 4\n");
        return ret;
    }
    
    simple_print("\n========================================\n");
    simple_print("All flash driver tests completed successfully!\n");
    simple_print("Ready for Zephyr community contribution\n");
    simple_print("========================================\n");
    
    return EOK;
}