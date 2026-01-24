/*
 * 简化的Zephyr官方UART驱动测试用例（包含MMIO操作）
 * 移除了Zephyr依赖，只保留MMIO操作
 */

#include <stdint.h>
#include <stddef.h>

/* STM32 UART寄存器定义 - 用于直接的MMIO操作 */
typedef struct {
    volatile uint32_t SR;     /* 状态寄存器 */
    volatile uint32_t DR;     /* 数据寄存器 */
    volatile uint32_t BRR;    /* 波特率寄存器 */
    volatile uint32_t CR1;    /* 控制寄存器1 */
    volatile uint32_t CR2;    /* 控制寄存器2 */
    volatile uint32_t CR3;    /* 控制寄存器3 */
    volatile uint32_t GTPR;   /* 保护时间和预分频寄存器 */
} USART_TypeDef;

/* STM32 UART基地址 */
#define USART1_BASE 0x40011000UL
#define USART2_BASE 0x40004400UL
#define USART3_BASE 0x40004800UL

#define USART1 ((USART_TypeDef *)USART1_BASE)
#define USART2 ((USART_TypeDef *)USART2_BASE)
#define USART3 ((USART_TypeDef *)USART3_BASE)

/* 简单的打印函数（用于调试） */
void simple_print(const char *str) {
    // 简单的打印实现
    (void)str;
}

/* 直接的MMIO操作函数 - CodeQL应该能检测到这些 */
void mmio_uart_init_direct(void)
{
    /* 直接寄存器访问 - CodeQL应该能检测为MMIO操作 */
    USART1->CR1 = 0x2000;  /* 使能UART，TE=1, UE=1 */
    USART1->BRR = 0x0341;  /* 设置波特率115200 */
    USART1->CR2 = 0x0000;  /* 默认设置 */
    USART1->CR3 = 0x0000;  /* 默认设置 */
    
    simple_print("Direct MMIO UART initialized\n");
}

void mmio_uart_send_byte_direct(uint8_t data)
{
    /* 等待发送缓冲区空 */
    while (!(USART1->SR & 0x0080)) {
        /* 空循环等待 */
        __asm__ volatile ("nop");
    }
    
    /* 发送数据 */
    USART1->DR = data;
}

void mmio_uart_send_string_direct(const char *str)
{
    while (*str) {
        mmio_uart_send_byte_direct(*str);
        str++;
    }
}

/* 混合使用不同的MMIO操作 */
void mixed_uart_operation(void)
{
    const char *msg = "Mixed operation test\n";
    
    /* 使用直接MMIO发送 */
    mmio_uart_send_string_direct(msg);
}

/* 条件语句中的MMIO操作 */
void conditional_mmio_operation(uint8_t config)
{
    if (config & 0x01) {
        /* 条件分支中的MMIO操作 */
        USART1->CR1 |= 0x2000;
        simple_print("Enabled USART1 via direct MMIO\n");
    }
    
    if (config & 0x02) {
        /* 另一个条件分支中的MMIO操作 */
        USART2->CR1 |= 0x2000;
        simple_print("Enabled USART2 via direct MMIO\n");
    }
}

/* 循环中的MMIO操作 */
void loop_mmio_operation(const uint8_t *data, size_t size)
{
    for (size_t i = 0; i < size; i++) {
        /* 循环中的MMIO操作 */
        while (!(USART1->SR & 0x0080)) {
            /* 等待 */
            __asm__ volatile ("nop");
        }
        USART1->DR = data[i];
    }
}

/* 结构体中的MMIO操作 */
typedef struct {
    USART_TypeDef *uart;
    uint32_t baudrate;
} uart_device_t;

void struct_mmio_operation(uart_device_t *dev)
{
    /* 通过结构体指针访问MMIO */
    dev->uart->BRR = dev->baudrate;
    dev->uart->CR1 = 0x2000;
}

/* 复杂的MMIO操作 */
void complex_mmio_operation(void)
{
    /* 多个MMIO操作组合 */
    USART1->CR1 = 0x2000;
    USART1->BRR = 0x0341;
    
    /* 条件MMIO操作 */
    if (USART1->SR & 0x0080) {
        USART1->DR = 'A';
    }
    
    /* 循环中的MMIO操作 */
    for (int i = 0; i < 10; i++) {
        while (!(USART1->SR & 0x0080)) {
            __asm__ volatile ("nop");
        }
        USART1->DR = '0' + i;
    }
}

/*
 * 主函数 - 简化的测试程序
 */
int main(void)
{
    uint8_t test_data[] = "Hello from simplified Zephyr UART test!";
    
    /* 初始化直接MMIO UART */
    mmio_uart_init_direct();
    
    /* 测试条件MMIO操作 */
    conditional_mmio_operation(0x03);
    
    /* 测试混合操作 */
    mixed_uart_operation();
    
    /* 测试循环中的MMIO操作 */
    loop_mmio_operation(test_data, sizeof(test_data) - 1);
    
    /* 测试结构体中的MMIO操作 */
    uart_device_t dev = {
        .uart = USART1,
        .baudrate = 115200,
    };
    struct_mmio_operation(&dev);
    
    /* 测试复杂的MMIO操作 */
    complex_mmio_operation();
    
    /* 发送完成消息 */
    mmio_uart_send_string_direct("\nTest completed!\n");
    
    return 0;
}
