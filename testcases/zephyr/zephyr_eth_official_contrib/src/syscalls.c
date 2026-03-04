/*
 * 系统调用实现 - 用于ETH测试
 * 提供基本的系统调用支持，用于模拟器环境
 */

#include <stdint.h>
#include <stddef.h>
#include <stdbool.h>
#include <string.h>

/* Zephyr风格的类型定义 */
typedef uint8_t u8_t;
typedef uint16_t u16_t;
typedef uint32_t u32_t;
typedef int32_t s32_t;

/* 系统调用号定义 */
#define SYS_write 1
#define SYS_read 0
#define SYS_open 2
#define SYS_close 3
#define SYS_exit 60

/* 简单的系统初始化函数 */
void SystemInit(void)
{
    /* 在模拟器环境中，不需要实际的硬件初始化 */
    /* 这个函数只是为了满足启动文件的调用 */
}

/* 简单的打印函数 */
void simple_print(const char *str)
{
    /* 在模拟器环境中，可以通过系统调用或直接输出实现 */
    /* 这里使用弱函数，可以在模拟器中被替换 */
    (void)str;
}

/* 系统调用处理函数 */
int _syscall(int num, ...)
{
    /* 基本的系统调用处理 */
    switch (num) {
        case SYS_write:
            /* 写操作 - 在模拟器中可以记录日志 */
            return 0;
        case SYS_read:
            /* 读操作 */
            return 0;
        case SYS_open:
            /* 打开文件 */
            return -1; /* 不支持 */
        case SYS_close:
            /* 关闭文件 */
            return 0;
        case SYS_exit:
            /* 退出程序 */
            while (1) {} /* 无限循环 */
        default:
            return -1;
    }
}

/* 标准库函数实现 */

/* 内存复制 */
void *memcpy(void *dest, const void *src, size_t n)
{
    char *d = (char *)dest;
    const char *s = (const char *)src;
    
    for (size_t i = 0; i < n; i++) {
        d[i] = s[i];
    }
    
    return dest;
}

/* 内存设置 */
void *memset(void *s, int c, size_t n)
{
    unsigned char *p = (unsigned char *)s;
    
    for (size_t i = 0; i < n; i++) {
        p[i] = (unsigned char)c;
    }
    
    return s;
}

/* 内存比较 */
int memcmp(const void *s1, const void *s2, size_t n)
{
    const unsigned char *p1 = (const unsigned char *)s1;
    const unsigned char *p2 = (const unsigned char *)s2;
    
    for (size_t i = 0; i < n; i++) {
        if (p1[i] != p2[i]) {
            return (int)p1[i] - (int)p2[i];
        }
    }
    
    return 0;
}

/* 字符串长度 */
size_t strlen(const char *s)
{
    size_t len = 0;
    
    while (s[len] != '\0') {
        len++;
    }
    
    return len;
}

/* 字符串复制 */
char *strcpy(char *dest, const char *src)
{
    char *d = dest;
    
    while ((*d++ = *src++) != '\0') {
        /* 空循环体 */
    }
    
    return dest;
}

/* 字符串连接 */
char *strcat(char *dest, const char *src)
{
    char *d = dest;
    
    /* 找到dest的末尾 */
    while (*d != '\0') {
        d++;
    }
    
    /* 复制src */
    while ((*d++ = *src++) != '\0') {
        /* 空循环体 */
    }
    
    return dest;
}

/* 字符串比较 */
int strcmp(const char *s1, const char *s2)
{
    while (*s1 && (*s1 == *s2)) {
        s1++;
        s2++;
    }
    
    return *(const unsigned char *)s1 - *(const unsigned char *)s2;
}

/* 弱函数定义 - 用于模拟器替换 */
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

int __attribute__((noinline, used, __weak__)) HAL_BE_ENET_ReadFrame(void* buf, int length){
    return 1;
}

int __attribute__((noinline, used, __weak__)) HAL_BE_Block_Write(void* buf, int block_size, int block_num){
    return block_num;
}

int __attribute__((noinline, used, __weak__)) HAL_BE_Block_Read(void* buf, int block_size, int block_num){
    return block_num;
}

/* 简单的printf实现 */
int printf(const char *format, ...)
{
    /* 简化实现，只打印固定字符串 */
    simple_print(format);
    return 0;
}

/* 简单的putchar实现 */
int putchar(int c)
{
    /* 简化实现 */
    return c;
}

/* 简单的puts实现 */
int puts(const char *s)
{
    simple_print(s);
    simple_print("\n");
    return 0;
}