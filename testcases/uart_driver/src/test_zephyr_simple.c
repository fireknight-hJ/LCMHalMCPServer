/*
 * 简化的 Zephyr UART 驱动测试用例
 * 这个文件模拟 Zephyr UART API 并包含 MMIO 操作
 * 用于测试 CodeQL 的 MMIO 检测功能
 */

#include <stdint.h>
#include <stddef.h>
#include <string.h>

/* 模拟 Zephyr 类型定义 */
typedef int32_t s32_t;
typedef uint32_t u32_t;
typedef uint8_t u8_t;
typedef size_t size_t;

/* 模拟 Zephyr 设备结构 */
struct device {
    const char *name;
    void *config;
    void *data;
};

/* 模拟 Zephyr UART 事件类型 */
enum uart_event_type {
    UART_TX_DONE,
    UART_RX_RDY,
    UART_RX_DISABLED,
};

/* 模拟 Zephyr UART 事件结构 */
struct uart_event {
    enum uart_event_type type;
    union {
        struct {
            u8_t *buf;
            size_t offset;
            size_t len;
        } rx;
        struct {
            u8_t *buf;
            size_t len;
        } tx;
    } data;
};

/* 模拟 Zephyr UART 配置 */
struct uart_config {
    u32_t baudrate;
    u32_t parity;
    u32_t stop_bits;
    u32_t data_bits;
    u32_t flow_ctrl;
};

/* 模拟 Zephyr 错误代码 */
#define ENODEV 19
#define EINVAL 22

/* STM32 UART 寄存器定义 - 用于直接的 MMIO 操作 */
typedef struct {
    volatile uint32_t SR;     /* 状态寄存器 */
    volatile uint32_t DR;     /* 数据寄存器 */
    volatile uint32_t BRR;    /* 波特率寄存器 */
    volatile uint32_t CR1;    /* 控制寄存器1 */
    volatile uint32_t CR2;    /* 控制寄存器2 */
    volatile uint32_t CR3;    /* 控制寄存器3 */
    volatile uint32_t GTPR;   /* 保护时间和预分频寄存器 */
} USART_TypeDef;

/* STM32 UART 基地址 */
#define USART1_BASE 0x40011000UL
#define USART2_BASE 0x40004400UL
#define USART3_BASE 0x40004800UL

#define USART1 ((USART_TypeDef *)USART1_BASE)
#define USART2 ((USART_TypeDef *)USART2_BASE)
#define USART3 ((USART_TypeDef *)USART3_BASE)

/* 模拟 Zephyr UART API 函数 */
static int uart_configure(const struct device *dev, const struct uart_config *cfg)
{
    /* 模拟配置 UART */
    (void)dev;
    (void)cfg;
    return 0;
}

static int __attribute__((unused)) uart_callback_set(const struct device *dev, 
                            void (*callback)(const struct device *, struct uart_event *, void *),
                            void *user_data)
{
    /* 模拟设置回调 */
    (void)dev;
    (void)callback;
    (void)user_data;
    return 0;
}

static int uart_tx(const struct device *dev, const u8_t *buf, size_t len, s32_t timeout)
{
    /* 模拟发送数据 */
    (void)dev;
    (void)buf;
    (void)len;
    (void)timeout;
    return 0;
}

static int __attribute__((unused)) uart_rx_enable(const struct device *dev, u8_t *buf, size_t len, s32_t timeout)
{
    /* 模拟接收数据 */
    (void)dev;
    (void)buf;
    (void)len;
    (void)timeout;
    return 0;
}

/* 模拟设备获取宏 */
#define DEVICE_DT_GET(x) ((const struct device *)0x1000)

/* 模拟设备就绪检查 */
static int device_is_ready(const struct device *dev)
{
    (void)dev;
    return 1;
}

/* 直接的 MMIO 操作函数 - CodeQL 应该能检测到这些 */
void mmio_uart_init_direct(void)
{
    /* 直接寄存器访问 - CodeQL 应该能检测为 MMIO 操作 */
    USART1->CR1 = 0x2000;  /* 使能 UART */
    USART1->BRR = 0x0341;  /* 设置波特率 115200 */
    USART1->CR2 = 0x0000;  /* 默认设置 */
    USART1->CR3 = 0x0000;  /* 默认设置 */
}

void mmio_uart_send_byte_direct(uint8_t data)
{
    /* 等待发送缓冲区空 */
    while (!(USART1->SR & 0x0080)) {
        /* 空循环等待 */
    }
    
    /* 发送数据 */
    USART1->DR = data;
}

uint8_t mmio_uart_receive_byte_direct(void)
{
    /* 等待接收数据 */
    while (!(USART1->SR & 0x0020)) {
        /* 空循环等待 */
    }
    
    /* 读取数据 */
    return (uint8_t)(USART1->DR & 0xFF);
}

/* 模拟 Zephyr UART API 的函数 */
int zephyr_uart_init(void)
{
    const struct device *uart_dev;
    
    /* 获取 UART 设备 */
    uart_dev = DEVICE_DT_GET(0);
    if (!device_is_ready(uart_dev)) {
        return -ENODEV;
    }
    
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

/* 使用 Zephyr API 发送数据 */
int zephyr_uart_send(const uint8_t *data, size_t len)
{
    const struct device *uart_dev = DEVICE_DT_GET(0);
    if (!uart_dev) {
        return -ENODEV;
    }
    
    return uart_tx(uart_dev, data, len, 1000);
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
    
    if (config & 0x04) {
        /* 使用 Zephyr API */
        zephyr_uart_init();
    }
}

/* 循环中的 MMIO 操作 */
void loop_mmio_operation(const uint8_t *data, size_t size)
{
    for (size_t i = 0; i < size; i++) {
        /* 循环中的 MMIO 操作 */
        while (!(USART1->SR & 0x0080)) {
            /* 等待 */
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
    
    /* 同时使用模拟的 Zephyr API */
    if (dev->zephyr_dev) {
        struct uart_config cfg = {
            .baudrate = dev->baudrate,
            .parity = 0,
            .stop_bits = 1,
            .data_bits = 8,
        };
        uart_configure(dev->zephyr_dev, &cfg);
    }
}

/* 主函数 */
int main(void)
{
    uint8_t test_data[] = "Hello Zephyr UART!";
    
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
    
    /* 使用 Zephyr API */
    zephyr_uart_send(test_data, sizeof(test_data) - 1);
    
    return 0;
}
