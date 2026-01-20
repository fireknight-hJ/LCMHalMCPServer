/*
 * ARM 架构的 Zephyr 兼容 UART 测试用例
 * 这个文件包含直接的 MMIO 操作，使用 Zephyr 兼容的 API
 * 针对 ARM Cortex-M 架构编译，适配模拟器工具链
 * 简化版本：移除复杂的启动代码，只保留核心 MMIO 函数
 */

#include <stdint.h>
#include <stddef.h>

/* Zephyr 兼容类型定义 */
typedef int32_t s32_t;
typedef uint32_t u32_t;
typedef uint8_t u8_t;
typedef size_t size_t;

/* Zephyr 设备结构 */
struct device {
    const char *name;
    void *config;
    void *data;
};

/* Zephyr UART 配置 */
struct uart_config {
    u32_t baudrate;
    u32_t parity;
    u32_t stop_bits;
    u32_t data_bits;
    u32_t flow_ctrl;
};

/* STM32 UART 寄存器定义 - ARM Cortex-M 内存映射 */
typedef struct {
    volatile uint32_t SR;     /* 状态寄存器 */
    volatile uint32_t DR;     /* 数据寄存器 */
    volatile uint32_t BRR;    /* 波特率寄存器 */
    volatile uint32_t CR1;    /* 控制寄存器1 */
    volatile uint32_t CR2;    /* 控制寄存器2 */
    volatile uint32_t CR3;    /* 控制寄存器3 */
    volatile uint32_t GTPR;   /* 保护时间和预分频寄存器 */
} USART_TypeDef;

/* STM32 UART 基地址 - ARM 内存映射 */
#define PERIPH_BASE       0x40000000UL
#define APB1PERIPH_BASE   (PERIPH_BASE + 0x00000000UL)
#define APB2PERIPH_BASE   (PERIPH_BASE + 0x00010000UL)

#define USART1_BASE       (APB2PERIPH_BASE + 0x1000UL)
#define USART2_BASE       (APB1PERIPH_BASE + 0x4400UL)
#define USART3_BASE       (APB1PERIPH_BASE + 0x4800UL)

#define USART1            ((USART_TypeDef *)USART1_BASE)
#define USART2            ((USART_TypeDef *)USART2_BASE)
#define USART3            ((USART_TypeDef *)USART3_BASE)

/* 模拟 Zephyr UART API 函数 */
static int uart_configure(const struct device *dev, const struct uart_config *cfg)
{
    /* 模拟配置 UART */
    (void)dev;
    (void)cfg;
    return 0;
}

static int __attribute__((unused)) uart_tx(const struct device *dev, const u8_t *buf, size_t len, s32_t timeout)
{
    /* 模拟发送数据 */
    (void)dev;
    (void)buf;
    (void)len;
    (void)timeout;
    return 0;
}

/* 模拟设备获取宏 */
#define DEVICE_DT_GET(x) ((const struct device *)0x1000)

/* 直接的 MMIO 操作函数 - CodeQL 应该能检测到这些 */
void mmio_uart_init_direct(void)
{
    /* 直接寄存器访问 - CodeQL 应该能检测为 MMIO 操作 */
    USART1->CR1 = 0x2000;  /* 使能 UART，TE=1, UE=1 */
    USART1->BRR = 0x0341;  /* 设置波特率 115200 */
    USART1->CR2 = 0x0000;  /* 默认设置 */
    USART1->CR3 = 0x0000;  /* 默认设置 */
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

uint8_t mmio_uart_receive_byte_direct(void)
{
    /* 等待接收数据 */
    while (!(USART1->SR & 0x0020)) {
        /* 空循环等待 */
        __asm__ volatile ("nop");
    }
    
    /* 读取数据 */
    return (uint8_t)(USART1->DR & 0xFF);
}

/* 使用 Zephyr API 的函数 */
int zephyr_uart_init(void)
{
    const struct device *uart_dev;
    
    /* 获取 UART 设备 */
    uart_dev = DEVICE_DT_GET(0);
    
    /* 配置 UART */
    struct uart_config uart_cfg = {
        .baudrate = 115200,
        .parity = 0,  /* UART_CFG_PARITY_NONE */
        .stop_bits = 1, /* UART_CFG_STOP_BITS_1 */
        .data_bits = 8, /* UART_CFG_DATA_BITS_8 */
        .flow_ctrl = 0, /* UART_CFG_FLOW_CTRL_NONE */
    };
    
    return uart_configure(uart_dev, &uart_cfg);
}

/* 混合使用 Zephyr API 和直接 MMIO 操作 */
void mixed_uart_operation(void)
{
    /* 使用 Zephyr API 初始化 */
    zephyr_uart_init();
    
    /* 使用直接 MMIO 发送数据 */
    const char *msg = "Mixed operation test\n";
    while (*msg) {
        mmio_uart_send_byte_direct(*msg);
        msg++;
    }
}

/* 条件语句中的 MMIO 操作 */
void conditional_mmio_operation(uint8_t config)
{
    if (config & 0x01) {
        /* 条件分支中的 MMIO 操作 */
        USART1->CR1 |= 0x2000;
    }
    
    if (config & 0x02) {
        /* 另一个条件分支中的 MMIO 操作 */
        USART2->CR1 |= 0x2000;
    }
}

/* 循环中的 MMIO 操作 */
void loop_mmio_operation(const uint8_t *data, size_t size)
{
    for (size_t i = 0; i < size; i++) {
        /* 循环中的 MMIO 操作 */
        while (!(USART1->SR & 0x0080)) {
            __asm__ volatile ("nop");
        }
        USART1->DR = data[i];
    }
}

/* 结构体中的 MMIO 操作 */
typedef struct {
    USART_TypeDef *uart;
    uint32_t baudrate;
    const struct device *zephyr_dev;
} uart_device_t;

void struct_mmio_operation(uart_device_t *dev)
{
    /* 通过结构体指针访问 MMIO */
    dev->uart->BRR = dev->baudrate;
    dev->uart->CR1 = 0x2000;
}

/* 复杂的 MMIO 操作 */
void complex_mmio_operation(uint8_t *buffer, size_t len)
{
    /* 初始化 */
    USART1->CR1 = 0x2000;
    USART1->BRR = 0x0341;
    
    /* 批量传输 */
    for (size_t i = 0; i < len; i++) {
        while (!(USART1->SR & 0x0080)) {
            __asm__ volatile ("nop");
        }
        USART1->DR = buffer[i];
    }
    
    /* 条件操作 */
    if (len > 10) {
        USART1->CR1 |= 0x1000;  /* 使能 RX */
    }
}

/* 简单的 main 函数 */
int main(void)
{
    uint8_t test_data[] = "Hello ARM Zephyr UART!";
    
    /* 测试各种操作 */
    mmio_uart_init_direct();
    
    /* 直接 MMIO 操作 */
    loop_mmio_operation(test_data, sizeof(test_data) - 1);
    
    /* 条件 MMIO 操作 */
    conditional_mmio_operation(0x03);
    
    /* 混合操作 */
    mixed_uart_operation();
    
    /* 结构体操作 */
    uart_device_t dev = {
        .uart = USART1,
        .baudrate = 115200,
        .zephyr_dev = DEVICE_DT_GET(0),
    };
    struct_mmio_operation(&dev);
    
    /* 复杂操作 */
    complex_mmio_operation(test_data, sizeof(test_data) - 1);
    
    return 0;
}
