/* 
 * 修复版本：添加参数使用以避免未使用参数警告
 */

#include <stdint.h>
#include <stddef.h>

// HAL函数定义
int __attribute__((noinline, used, __weak__)) HAL_BE_In(void* buf, int len){
    (void)buf;  // 明确标记参数未使用
    (void)len;
    return 0;
}

int __attribute__((noinline, used, __weak__)) HAL_BE_ENET_ReadFrame(void* buf, int length){
    (void)buf;
    (void)length;
    return 0;
}

int __attribute__((noinline, used, __weak__)) HAL_BE_Block_Write(void* buf, int block_size, int block_num){
    (void)buf;
    (void)block_size;
    (void)block_num;
    return 0;
}

int __attribute__((noinline, used, __weak__)) HAL_BE_Block_Read(void* buf, int block_size, int block_num){
    (void)buf;
    (void)block_size;
    (void)block_num;
    return 0;
}

int __attribute__((noinline, used, __weak__)) HAL_BE_Out(int val){
    return 0;
}

int __attribute__((noinline, used, __weak__)) HAL_BE_return_0(void){
    return 0;
}

int __attribute__((noinline, used, __weak__)) HAL_BE_return_1(void){
    return 1;
}

// 简单的MMIO操作函数
void simple_mmio_operation(void) {
    volatile uint32_t *reg = (volatile uint32_t *)0x40000000;
    *reg = 0x12345678;
}

// 循环MMIO操作
void loop_mmio_operation(const uint8_t *data, size_t size) {
    (void)data;  // 明确标记参数未使用
    volatile uint32_t *status_reg = (volatile uint32_t *)0x40000004;
    volatile uint32_t *data_reg = (volatile uint32_t *)0x40000008;
    
    for (size_t i = 0; i < size; i++) {
        // 等待状态就绪
        while (!(*status_reg & 0x01)) {
            // 空循环等待
        }
        // 写入数据
        *data_reg = data[i];
    }
}

// 复杂MMIO操作
void complex_mmio_operation(uint8_t *buffer, size_t len) {
    (void)buffer;  // 明确标记参数未使用
    volatile uint32_t *usart_cr1 = (volatile uint32_t *)0x40013800;
    volatile uint32_t *usart_brr = (volatile uint32_t *)0x40013808;
    volatile uint32_t *usart_sr = (volatile uint32_t *)0x40013800;
    volatile uint32_t *usart_dr = (volatile uint32_t *)0x40013804;
    
    // 初始化USART
    *usart_cr1 = 0x2000;
    *usart_brr = 0x0341;
    
    // 传输数据
    for (size_t i = 0; i < len; i++) {
        // 等待传输就绪
        while (!(*usart_sr & 0x0080)) {
            __asm__ volatile ("nop");
        }
        // 发送数据
        *usart_dr = buffer[i];
    }
    
    // 条件配置
    if (len > 10) {
        *usart_cr1 |= 0x1000;  // 使能RX
    }
}

// UART接收字节（直接MMIO）
uint8_t mmio_uart_receive_byte_direct(void) {
    volatile uint32_t *usart_sr = (volatile uint32_t *)0x40013800;
    volatile uint32_t *usart_dr = (volatile uint32_t *)0x40013804;
    
    // 等待接收就绪
    while (!(*usart_sr & 0x0020)) {
        __asm__ volatile ("nop");
    }
    
    return (uint8_t)(*usart_dr & 0xFF);
}

// UART发送字节（直接MMIO）
void mmio_uart_send_byte_direct(uint8_t data) {
    volatile uint32_t *usart_sr = (volatile uint32_t *)0x40013800;
    volatile uint32_t *usart_dr = (volatile uint32_t *)0x40013804;
    
    // 等待传输就绪
    while (!(*usart_sr & 0x0080)) {
        __asm__ volatile ("nop");
    }
    
    // 发送数据
    *usart_dr = data;
}

// 主函数
int main(void) {
    uint8_t test_data[] = {0x01, 0x02, 0x03, 0x04};
    
    // 测试各种操作
    simple_mmio_operation();
    loop_mmio_operation(test_data, sizeof(test_data));
    complex_mmio_operation(test_data, sizeof(test_data));
    
    // 测试UART操作
    mmio_uart_send_byte_direct(0x55);
    uint8_t received = mmio_uart_receive_byte_direct();
    (void)received;  // 标记未使用
    
    return 0;
}
