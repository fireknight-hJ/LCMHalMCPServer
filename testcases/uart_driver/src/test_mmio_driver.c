// 测试MMIO驱动 - 包含直接的MMIO操作
// 这个文件用于测试CodeQL的MMIO检测功能

#include <stdint.h>
#include <stddef.h>

// STM32 UART寄存器定义（简化版）
typedef struct {
    volatile uint32_t SR;     // 状态寄存器
    volatile uint32_t DR;     // 数据寄存器
    volatile uint32_t BRR;    // 波特率寄存器
    volatile uint32_t CR1;    // 控制寄存器1
    volatile uint32_t CR2;    // 控制寄存器2
    volatile uint32_t CR3;    // 控制寄存器3
    volatile uint32_t GTPR;   // 保护时间和预分频寄存器
} USART_TypeDef;

// UART1的基地址（STM32F4）
#define USART1_BASE 0x40011000UL
#define USART1 ((USART_TypeDef *)USART1_BASE)

// UART2的基地址
#define USART2_BASE 0x40004400UL
#define USART2 ((USART_TypeDef *)USART2_BASE)

// 直接MMIO操作函数 - CodeQL应该能检测到这些
void mmio_uart_init_direct(void) {
    // 直接寄存器访问 - CodeQL应该能检测为MMIO操作
    USART1->CR1 = 0x2000;  // 使能UART
    USART1->BRR = 0x0341;  // 设置波特率 115200
    USART1->CR2 = 0x0000;  // 默认设置
    USART1->CR3 = 0x0000;  // 默认设置
}

void mmio_uart_send_byte_direct(uint8_t data) {
    // 等待发送缓冲区空
    while (!(USART1->SR & 0x0080)) {
        // 空循环等待
    }
    
    // 发送数据
    USART1->DR = data;
}

uint8_t mmio_uart_receive_byte_direct(void) {
    // 等待接收数据
    while (!(USART1->SR & 0x0020)) {
        // 空循环等待
    }
    
    // 读取数据
    return (uint8_t)(USART1->DR & 0xFF);
}

// 使用指针的MMIO操作
void mmio_uart_init_pointer(USART_TypeDef *uart) {
    // 通过指针访问MMIO寄存器
    uart->CR1 = 0x2000;
    uart->BRR = 0x0341;
}

// 使用数组和指针转换的MMIO操作
void mmio_uart_init_array(void) {
    // 通过数组和指针转换访问MMIO
    uint32_t *uart_regs = (uint32_t *)USART1_BASE;
    uart_regs[3] = 0x2000;  // CR1寄存器
    uart_regs[2] = 0x0341;  // BRR寄存器
}

// 包含MMIO操作的复杂函数
void mmio_uart_complex_operation(uint8_t *buffer, size_t length) {
    // 初始化UART
    USART1->CR1 = 0x2000;
    USART1->BRR = 0x0341;
    
    // 发送多个字节
    for (size_t i = 0; i < length; i++) {
        // 等待发送缓冲区空
        while (!(USART1->SR & 0x0080)) {
            // 空循环
        }
        
        // 发送数据
        USART1->DR = buffer[i];
    }
}

// 嵌套函数调用中的MMIO操作
static void mmio_internal_send(uint8_t data) {
    // 内部函数中的MMIO操作
    while (!(USART1->SR & 0x0080)) {
        // 等待
    }
    USART1->DR = data;
}

void mmio_uart_send_string(const char *str) {
    // 调用内部函数进行MMIO操作
    while (*str) {
        mmio_internal_send(*str);
        str++;
    }
}

// 条件语句中的MMIO操作
void mmio_uart_conditional_operation(uint8_t config) {
    if (config & 0x01) {
        // 条件分支中的MMIO操作
        USART1->CR1 |= 0x2000;
    }
    
    if (config & 0x02) {
        // 另一个条件分支中的MMIO操作
        USART2->CR1 |= 0x2000;
    }
}

// 循环中的MMIO操作
void mmio_uart_bulk_transfer(const uint8_t *data, size_t size) {
    for (size_t i = 0; i < size; i++) {
        // 循环中的MMIO操作
        while (!(USART1->SR & 0x0080)) {
            // 等待
        }
        USART1->DR = data[i];
    }
}

// 结构体中的MMIO操作
typedef struct {
    USART_TypeDef *uart;
    uint32_t baudrate;
} uart_device_t;

void mmio_uart_struct_operation(uart_device_t *dev) {
    // 通过结构体指针访问MMIO
    dev->uart->BRR = dev->baudrate;
    dev->uart->CR1 = 0x2000;
}

// 主函数 - 调用各种MMIO函数
int main(void) {
    uint8_t test_data[] = "Hello MMIO!";
    
    // 调用各种MMIO函数
    mmio_uart_init_direct();
    mmio_uart_send_string("Testing MMIO detection\n");
    mmio_uart_bulk_transfer(test_data, sizeof(test_data) - 1);
    mmio_uart_conditional_operation(0x03);
    
    return 0;
}