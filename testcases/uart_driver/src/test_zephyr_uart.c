/*
 * Zephyr UART 驱动测试用例
 * 这个文件使用 Zephyr UART API 并包含 MMIO 操作
 * 用于测试 CodeQL 的 MMIO 检测功能
 */

#include <zephyr/kernel.h>
#include <zephyr/device.h>
#include <zephyr/drivers/uart.h>
#include <zephyr/sys/printk.h>
#include <string.h>

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

/* Zephyr UART 设备 */
static const struct device *uart_dev;

/* 回调函数 */
static void uart_callback(const struct device *dev, struct uart_event *evt, void *user_data)
{
    switch (evt->type) {
    case UART_TX_DONE:
        printk("UART TX done\n");
        break;
    case UART_RX_RDY:
        printk("UART RX ready: %c\n", evt->data.rx.buf[evt->data.rx.offset]);
        break;
    case UART_RX_DISABLED:
        printk("UART RX disabled\n");
        break;
    default:
        break;
    }
}

/* 使用 Zephyr UART API 的函数 */
int zephyr_uart_init(void)
{
    int ret;
    
    /* 获取 UART 设备 */
    uart_dev = DEVICE_DT_GET(DT_NODELABEL(usart1));
    if (!device_is_ready(uart_dev)) {
        printk("UART device not ready\n");
        return -ENODEV;
    }
    
    /* 配置 UART */
    struct uart_config uart_cfg = {
        .baudrate = 115200,
        .parity = UART_CFG_PARITY_NONE,
        .stop_bits = UART_CFG_STOP_BITS_1,
        .data_bits = UART_CFG_DATA_BITS_8,
        .flow_ctrl = UART_CFG_FLOW_CTRL_NONE,
    };
    
    ret = uart_configure(uart_dev, &uart_cfg);
    if (ret < 0) {
        printk("Failed to configure UART: %d\n", ret);
        return ret;
    }
    
    /* 设置回调函数 */
    ret = uart_callback_set(uart_dev, uart_callback, NULL);
    if (ret < 0) {
        printk("Failed to set UART callback: %d\n", ret);
        return ret;
    }
    
    printk("Zephyr UART initialized\n");
    return 0;
}

/* 使用 Zephyr API 发送数据 */
int zephyr_uart_send(const uint8_t *data, size_t len)
{
    if (!uart_dev) {
        return -ENODEV;
    }
    
    return uart_tx(uart_dev, data, len, SYS_FOREVER_MS);
}

/* 使用 Zephyr API 接收数据 */
int zephyr_uart_receive(uint8_t *buffer, size_t len)
{
    if (!uart_dev) {
        return -ENODEV;
    }
    
    return uart_rx_enable(uart_dev, buffer, len, SYS_FOREVER_MS);
}

/* 直接的 MMIO 操作函数 - CodeQL 应该能检测到这些 */
void mmio_uart_init_direct(void)
{
    /* 直接寄存器访问 - CodeQL 应该能检测为 MMIO 操作 */
    USART1->CR1 = 0x2000;  /* 使能 UART */
    USART1->BRR = 0x0341;  /* 设置波特率 115200 */
    USART1->CR2 = 0x0000;  /* 默认设置 */
    USART1->CR3 = 0x0000;  /* 默认设置 */
    
    printk("Direct MMIO UART initialized\n");
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
    
    /* 使用 Zephyr API 接收数据 */
    uint8_t rx_buffer[32];
    zephyr_uart_receive(rx_buffer, sizeof(rx_buffer));
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
    
    /* 同时使用 Zephyr API */
    if (dev->zephyr_dev) {
        struct uart_config cfg = {
            .baudrate = dev->baudrate,
            .parity = UART_CFG_PARITY_NONE,
            .stop_bits = UART_CFG_STOP_BITS_1,
            .data_bits = UART_CFG_DATA_BITS_8,
        };
        uart_configure(dev->zephyr_dev, &cfg);
    }
}

/* 主函数 */
int main(void)
{
    printk("Starting Zephyr UART test\n");
    
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
        .zephyr_dev = uart_dev,
    };
    struct_mmio_operation(&dev);
    
    /* 使用 Zephyr API */
    zephyr_uart_send(test_data, sizeof(test_data) - 1);
    
    printk("Zephyr UART test completed\n");
    
    return 0;
}
