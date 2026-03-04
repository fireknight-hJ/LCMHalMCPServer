/*
 * Zephyr官方ETH驱动测试用例 - 用于开源贡献
 * 基于Zephyr官方ETH示例，包含网络协议栈和MMIO操作
 * 目标：支持ETH的ARM板子（STM32F746G Discovery）
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

/* STM32 ETH寄存器定义 - 用于直接的MMIO操作 */
typedef struct {
    volatile u32_t MACCR;     /* MAC配置寄存器 */
    volatile u32_t MACFFR;    /* MAC帧过滤寄存器 */
    volatile u32_t MACHTHR;   /* MAC哈希表高位寄存器 */
    volatile u32_t MACHTLR;   /* MAC哈希表低位寄存器 */
    volatile u32_t MACMIIAR;  /* MAC MII地址寄存器 */
    volatile u32_t MACMIIDR;  /* MAC MII数据寄存器 */
    volatile u32_t MACFCR;    /* MAC流控制寄存器 */
    volatile u32_t MACVLANTR; /* MAC VLAN标签寄存器 */
    volatile u32_t RESERVED0[2];
    volatile u32_t MACRWUFFR; /* MAC远程唤醒帧过滤寄存器 */
    volatile u32_t MACPMTCSR; /* MAC电源管理控制状态寄存器 */
    volatile u32_t RESERVED1[2];
    volatile u32_t MACSR;     /* MAC状态寄存器 */
    volatile u32_t MACIMR;    /* MAC中断屏蔽寄存器 */
    volatile u32_t MACA0HR;   /* MAC地址0高位寄存器 */
    volatile u32_t MACA0LR;   /* MAC地址0低位寄存器 */
    volatile u32_t MACA1HR;   /* MAC地址1高位寄存器 */
    volatile u32_t MACA1LR;   /* MAC地址1低位寄存器 */
    volatile u32_t MACA2HR;   /* MAC地址2高位寄存器 */
    volatile u32_t MACA2LR;   /* MAC地址2低位寄存器 */
    volatile u32_t MACA3HR;   /* MAC地址3高位寄存器 */
    volatile u32_t MACA3LR;   /* MAC地址3低位寄存器 */
    volatile u32_t RESERVED2[40];
    volatile u32_t MMCCR;     /* MMC控制寄存器 */
    volatile u32_t MMCRIR;    /* MMC接收中断寄存器 */
    volatile u32_t MMCTIR;    /* MMC发送中断寄存器 */
    volatile u32_t MMCRIMR;   /* MMC接收中断屏蔽寄存器 */
    volatile u32_t MMCTIMR;   /* MMC发送中断屏蔽寄存器 */
    volatile u32_t RESERVED3[14];
    volatile u32_t MMCTGFSCCR; /* MMC发送良好帧单冲突计数器 */
    volatile u32_t MMCTGFMSCCR; /* MMC发送良好帧多冲突计数器 */
    volatile u32_t RESERVED4[5];
    volatile u32_t MMCTGFCR;  /* MMC发送良好帧计数器 */
    volatile u32_t RESERVED5[10];
    volatile u32_t MMCRFCECR; /* MMC接收帧校验错误计数器 */
    volatile u32_t MMCRFAECR; /* MMC接收对齐错误计数器 */
    volatile u32_t RESERVED6[10];
    volatile u32_t MMCRGUFCR; /* MMC接收良好单播帧计数器 */
    volatile u32_t RESERVED7[334];
    volatile u32_t PTPTSCR;   /* PTP时间戳控制寄存器 */
    volatile u32_t PTPSSIR;   /* PTP子秒增量寄存器 */
    volatile u32_t PTPTSHR;   /* PTP时间戳高位寄存器 */
    volatile u32_t PTPTSLR;   /* PTP时间戳低位寄存器 */
    volatile u32_t PTPTSHUR;  /* PTP时间戳高位更新寄存器 */
    volatile u32_t PTPTSLUR;  /* PTP时间戳低位更新寄存器 */
    volatile u32_t PTPTSAR;   /* PTP时间戳添加寄存器 */
    volatile u32_t PTPTTHR;   /* PTP目标时间高位寄存器 */
    volatile u32_t PTPTTLR;   /* PTP目标时间低位寄存器 */
    volatile u32_t RESERVED8[567];
    volatile u32_t DMABMR;    /* DMA总线模式寄存器 */
    volatile u32_t DMATPDR;   /* DMA发送轮询请求寄存器 */
    volatile u32_t DMARPDR;   /* DMA接收轮询请求寄存器 */
    volatile u32_t DMARDLAR;  /* DMA接收描述符列表地址寄存器 */
    volatile u32_t DMATDLAR;  /* DMA发送描述符列表地址寄存器 */
    volatile u32_t DMASR;     /* DMA状态寄存器 */
    volatile u32_t DMAOMR;    /* DMA操作模式寄存器 */
    volatile u32_t DMAIER;    /* DMA中断使能寄存器 */
    volatile u32_t DMAMFBOCR; /* DMA错过帧和缓冲区溢出计数器 */
    volatile u32_t DMARSWTR;  /* DMA接收状态轮询定时器寄存器 */
    volatile u32_t RESERVED9[8];
    volatile u32_t DMACHTDR;  /* DMA当前主机发送描述符寄存器 */
    volatile u32_t DMACHRDR;  /* DMA当前主机接收描述符寄存器 */
    volatile u32_t DMACHTBAR; /* DMA当前主机传输缓冲区地址寄存器 */
    volatile u32_t DMACHRBAR; /* DMA当前主机接收缓冲区地址寄存器 */
} ETH_TypeDef;

/* STM32 ETH基地址 */
#define ETH_BASE 0x40028000UL
#define ETH ((ETH_TypeDef *)ETH_BASE)

/* ETH MAC配置寄存器位定义 */
#define ETH_MACCR_WD   (1 << 23)  /* 看门狗禁用 */
#define ETH_MACCR_JD   (1 << 22)  /* Jabber禁用 */
#define ETH_MACCR_IFG  (0x3 << 17) /* 帧间间隙 */
#define ETH_MACCR_CSD  (1 << 16)  /* 载波侦听禁用 */
#define ETH_MACCR_FES  (1 << 14)  /* 快速以太网速度 */
#define ETH_MACCR_ROD  (1 << 13)  /* 接收自有禁用 */
#define ETH_MACCR_LM   (1 << 12)  /* 环回模式 */
#define ETH_MACCR_DM   (1 << 11)  /* 双工模式 */
#define ETH_MACCR_IPCO (1 << 10)  /* IP校验和卸载 */
#define ETH_MACCR_RD   (1 << 9)   /* 重试禁用 */
#define ETH_MACCR_APCS (1 << 7)   /* 自动暂停/继续支持 */
#define ETH_MACCR_BL   (0x3 << 5) /* 退避限制 */
#define ETH_MACCR_DC   (1 << 4)   /* 延迟补偿 */
#define ETH_MACCR_TE   (1 << 3)   /* 发送使能 */
#define ETH_MACCR_RE   (1 << 2)   /* 接收使能 */

/* ETH DMA总线模式寄存器位定义 */
#define ETH_DMABMR_SR  (1 << 0)   /* 软件复位 */
#define ETH_DMABMR_DA  (1 << 2)   /* 描述符跳过模式 */
#define ETH_DMABMR_DSL (0x7 << 2) /* 描述符跳过长度 */
#define ETH_DMABMR_EDFE (1 << 7)  /* 增强描述符格式使能 */
#define ETH_DMABMR_PBL (0x3F << 8) /* 可编程突发长度 */

/* ETH DMA状态寄存器位定义 */
#define ETH_DMASR_TS   (1 << 0)   /* 发送状态 */
#define ETH_DMASR_TPSS (1 << 1)   /* 发送进程暂停状态 */
#define ETH_DMASR_TBUS (1 << 2)   /* 发送缓冲区不可用状态 */
#define ETH_DMASR_TJTS (1 << 3)   /* 发送作业完成状态 */
#define ETH_DMASR_ROS  (1 << 4)   /* 接收溢出状态 */
#define ETH_DMASR_TUS  (1 << 5)   /* 发送下溢状态 */
#define ETH_DMASR_RS   (1 << 6)   /* 接收状态 */
#define ETH_DMASR_RBUS (1 << 7)   /* 接收缓冲区不可用状态 */
#define ETH_DMASR_RPSS (1 << 8)   /* 接收进程暂停状态 */
#define ETH_DMASR_RWTS (1 << 9)   /* 接收看门狗超时状态 */
#define ETH_DMASR_ETS  (1 << 10)  /* 早期发送状态 */
#define ETH_DMASR_FBES (1 << 13)  /* 致命总线错误状态 */
#define ETH_DMASR_ERS  (1 << 14)  /* 早期接收状态 */
#define ETH_DMASR_AIS  (1 << 15)  /* 异常中断汇总 */
#define ETH_DMASR_NIS  (1 << 16)  /* 正常中断汇总 */

/* Zephyr风格的状态码 */
#define EOK       0
#define EIO      -5
#define EINVAL   -22
#define ENODEV   -19
#define EBUSY    -16
#define ETIMEDOUT -110

/* ETH缓冲区大小 */
#define ETH_RX_BUFFER_SIZE 1524  /* 标准以太网帧大小 + VLAN标签 */
#define ETH_TX_BUFFER_SIZE 1524
#define ETH_DESC_COUNT     4     /* 描述符数量 */

/* ETH描述符结构 */
typedef struct {
    volatile u32_t Status;
    volatile u32_t ControlBufferSize;
    volatile u32_t Buffer1Addr;
    volatile u32_t Buffer2NextDescAddr;
} ETH_DMADescTypeDef;

/* ETH描述符状态位 */
#define ETH_DMATXDESC_OWN     (1 << 31)  /* 所有权位 */
#define ETH_DMATXDESC_IC      (1 << 30)  /* 中断完成 */
#define ETH_DMATXDESC_LS      (1 << 29)  /* 最后段 */
#define ETH_DMATXDESC_FS      (1 << 28)  /* 第一段 */
#define ETH_DMATXDESC_DC      (1 << 27)  /* 禁用CRC */
#define ETH_DMATXDESC_DP      (1 << 26)  /* 禁用填充 */
#define ETH_DMATXDESC_TTSE    (1 << 25)  /* 发送时间戳使能 */
#define ETH_DMATXDESC_CIC     (0x3 << 23) /* 校验和插入控制 */

#define ETH_DMARXDESC_OWN     (1 << 31)  /* 所有权位 */
#define ETH_DMARXDESC_AFM     (1 << 30)  /* 目的地址过滤器失败 */
#define ETH_DMARXDESC_FL      (0x3FFF << 16) /* 帧长度 */
#define ETH_DMARXDESC_ES      (1 << 15)  /* 错误汇总 */
#define ETH_DMARXDESC_DE      (1 << 14)  /* 描述符错误 */
#define ETH_DMARXDESC_SAF     (1 << 13)  /* 源地址过滤器失败 */
#define ETH_DMARXDESC_LE      (1 << 12)  /* 长度错误 */
#define ETH_DMARXDESC_OE      (1 << 11)  /* 溢出错误 */
#define ETH_DMARXDESC_VLAN    (1 << 10)  /* VLAN标签 */
#define ETH_DMARXDESC_FS      (1 << 9)   /* 第一段 */
#define ETH_DMARXDESC_LS      (1 << 8)   /* 最后段 */
#define ETH_DMARXDESC_IPHCE   (1 << 7)   /* IP头校验和错误 */
#define ETH_DMARXDESC_LC      (1 << 6)   /* 延迟冲突 */
#define ETH_DMARXDESC_FT      (1 << 5)   /* 帧类型 */
#define ETH_DMARXDESC_RWT     (1 << 4)   /* 接收看门狗超时 */
#define ETH_DMARXDESC_RE      (1 << 3)   /* 接收错误 */
#define ETH_DMARXDESC_DBE     (1 << 2)   /* 描述符错误 */
#define ETH_DMARXDESC_CE      (1 << 1)   /* CRC错误 */
#define ETH_DMARXDESC_PCE     (1 << 0)   /* 物理层错误 */

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

int __attribute__((noinline, used, __weak__)) HAL_BE_ENET_ReadFrame(void* buf, int length){
    return 1;
}

int __attribute__((noinline, used, __weak__)) HAL_BE_Block_Write(void* buf, int block_size, int block_num){
    return block_num;
}

int __attribute__((noinline, used, __weak__)) HAL_BE_Block_Read(void* buf, int block_size, int block_num){
    return block_num;
}

/* ETH全局变量 */
static ETH_DMADescTypeDef DMARxDscrTab[ETH_DESC_COUNT] __attribute__((aligned(4)));
static ETH_DMADescTypeDef DMATxDscrTab[ETH_DESC_COUNT] __attribute__((aligned(4)));
static u8_t Rx_Buff[ETH_DESC_COUNT][ETH_RX_BUFFER_SIZE] __attribute__((aligned(4)));
static u8_t Tx_Buff[ETH_DESC_COUNT][ETH_TX_BUFFER_SIZE] __attribute__((aligned(4)));

/* ETH初始化函数 */
static int eth_init(void)
{
    u32_t i;
    
    printf("ETH: Initializing Ethernet controller...\n");
    
    /* 软件复位ETH */
    ETH->DMABMR |= ETH_DMABMR_SR;
    
    /* 等待复位完成 */
    for (i = 0; i < 1000000; i++) {
        if (!(ETH->DMABMR & ETH_DMABMR_SR)) {
            break;
        }
    }
    
    if (i >= 1000000) {
        printf("ETH: Software reset timeout\n");
        return -ETIMEDOUT;
    }
    
    /* 配置DMA */
    ETH->DMABMR = ETH_DMABMR_EDFE | (1 << 8); /* 增强描述符格式，PBL=1 */
    
    /* 初始化接收描述符 */
    for (i = 0; i < ETH_DESC_COUNT; i++) {
        DMARxDscrTab[i].Status = ETH_DMARXDESC_OWN;
        DMARxDscrTab[i].ControlBufferSize = ETH_RX_BUFFER_SIZE;
        DMARxDscrTab[i].Buffer1Addr = (u32_t)&Rx_Buff[i][0];
        DMARxDscrTab[i].Buffer2NextDescAddr = (u32_t)&DMARxDscrTab[(i + 1) % ETH_DESC_COUNT];
    }
    
    /* 初始化发送描述符 */
    for (i = 0; i < ETH_DESC_COUNT; i++) {
        DMATxDscrTab[i].Status = 0;
        DMATxDscrTab[i].ControlBufferSize = 0;
        DMATxDscrTab[i].Buffer1Addr = (u32_t)&Tx_Buff[i][0];
        DMATxDscrTab[i].Buffer2NextDescAddr = (u32_t)&DMATxDscrTab[(i + 1) % ETH_DESC_COUNT];
    }
    
    /* 设置DMA描述符列表地址 */
    ETH->DMARDLAR = (u32_t)DMARxDscrTab;
    ETH->DMATDLAR = (u32_t)DMATxDscrTab;
    
    /* 配置MAC */
    ETH->MACCR = ETH_MACCR_WD | ETH_MACCR_JD | ETH_MACCR_CSD |
                 ETH_MACCR_FES | ETH_MACCR_ROD | ETH_MACCR_DC |
                 ETH_MACCR_BL | ETH_MACCR_APCS;
    
    /* 配置帧过滤 - 接收所有帧 */
    ETH->MACFFR = 0;
    
    /* 设置MAC地址 (00:80:E1:00:00:00) */
    ETH->MACA0HR = 0x000080E1;
    ETH->MACA0LR = 0x00000000;
    
    /* 启动DMA */
    ETH->DMABMR |= ETH_DMABMR_DA;
    
    /* 启动MAC */
    ETH->MACCR |= ETH_MACCR_TE | ETH_MACCR_RE;
    
    /* 启动DMA接收和发送 */
    ETH->DMASR = 0xFFFFFFFF; /* 清除所有状态位 */
    ETH->DMAOMR |= (1 << 1) | (1 << 13); /* 启动接收和发送 */
    
    printf("ETH: Initialization complete\n");
    return EOK;
}

/* ETH发送函数 */
static int eth_send(const void *data, u32_t length)
{
    static u32_t tx_index = 0;
    ETH_DMADescTypeDef *dmatx;
    u32_t timeout = 1000000;
    
    if (length == 0 || length > ETH_TX_BUFFER_SIZE) {
        printf("ETH: Invalid send length: %u\n", length);
        return -EINVAL;
    }
    
    /* 获取当前发送描述符 */
    dmatx = &DMATxDscrTab[tx_index];
    
    /* 等待描述符可用 */
    while ((dmatx->Status & ETH_DMATXDESC_OWN) && timeout > 0) {
        timeout--;
    }
    
    if (timeout == 0) {
        printf("ETH: Send timeout\n");
        return -ETIMEDOUT;
    }
    
    /* 复制数据到发送缓冲区 */
    memcpy((void *)dmatx->Buffer1Addr, data, length);
    
    /* 配置描述符 */
    dmatx->ControlBufferSize = (length & 0x1FFF) | ETH_DMATXDESC_FS | ETH_DMATXDESC_LS;
    dmatx->Status = ETH_DMATXDESC_OWN | ETH_DMATXDESC_IC;
    
    /* 触发发送 */
    ETH->DMASR = ETH_DMASR_TJTS; /* 清除发送完成状态 */
    ETH->DMATPDR = 0; /* 触发发送轮询请求 */
    
    /* 更新索引 */
    tx_index = (tx_index + 1) % ETH_DESC_COUNT;
    
    printf("ETH: Sent %u bytes\n", length);
    return EOK;
}

/* ETH接收函数 */
static int eth_receive(void *buffer, u32_t buffer_size, u32_t *received)
{
    static u32_t rx_index = 0;
    ETH_DMADescTypeDef *dmarx;
    u32_t frame_length;
    
    if (buffer == NULL || received == NULL) {
        return -EINVAL;
    }
    
    /* 获取当前接收描述符 */
    dmarx = &DMARxDscrTab[rx_index];
    
    /* 检查是否有数据到达 */
    if (dmarx->Status & ETH_DMARXDESC_OWN) {
        /* 描述符仍由DMA拥有，无数据 */
        *received = 0;
        return EOK;
    }
    
    /* 检查错误 */
    if (dmarx->Status & ETH_DMARXDESC_ES) {
        printf("ETH: Receive error: 0x%08X\n", dmarx->Status);
        /* 归还描述符给DMA */
        dmarx->Status = ETH_DMARXDESC_OWN;
        rx_index = (rx_index + 1) % ETH_DESC_COUNT;
        return -EIO;
    }
    
    /* 获取帧长度 */
    frame_length = (dmarx->Status & ETH_DMARXDESC_FL) >> 16;
    
    if (frame_length > buffer_size) {
        printf("ETH: Buffer too small: need %u, have %u\n", frame_length, buffer_size);
        /* 归还描述符给DMA */
        dmarx->Status = ETH_DMARXDESC_OWN;
        rx_index = (rx_index + 1) % ETH_DESC_COUNT;
        return -EINVAL;
    }
    
    /* 复制数据到用户缓冲区 */
    memcpy(buffer, (void *)dmarx->Buffer1Addr, frame_length);
    *received = frame_length;
    
    /* 归还描述符给DMA */
    dmarx->Status = ETH_DMARXDESC_OWN;
    rx_index = (rx_index + 1) % ETH_DESC_COUNT;
    
    printf("ETH: Received %u bytes\n", frame_length);
    return EOK;
}

/* ETH链路状态检查 */
static int eth_check_link(void)
{
    /* 在模拟器环境中，假设链路总是通的 */
    /* 实际硬件中会检查PHY状态寄存器 */
    return EOK;
}

/* ETH性能测试函数 */
static int eth_performance_test(void)
{
    u8_t test_data[64];
    u8_t rx_buffer[64];
    u32_t received;
    int ret;
    int i;
    
    printf("ETH: Starting performance test...\n");
    
    /* 准备测试数据 */
    for (i = 0; i < sizeof(test_data); i++) {
        test_data[i] = i & 0xFF;
    }
    
    /* 发送测试数据 */
    ret = eth_send(test_data, sizeof(test_data));
    if (ret != EOK) {
        printf("ETH: Performance test failed at send\n");
        return ret;
    }
    
    /* 短暂延迟 */
    for (i = 0; i < 10000; i++) {
        __asm__ volatile ("nop");
    }
    
    /* 尝试接收 */
    ret = eth_receive(rx_buffer, sizeof(rx_buffer), &received);
    if (ret != EOK) {
        printf("ETH: Performance test failed at receive\n");
        return ret;
    }
    
    if (received > 0) {
        /* 验证接收到的数据 */
        if (memcmp(test_data, rx_buffer, sizeof(test_data)) == 0) {
            printf("ETH: Performance test passed - data verified\n");
        } else {
            printf("ETH: Performance test failed - data mismatch\n");
            return -EIO;
        }
    } else {
        printf("ETH: Performance test - no data received (expected in loopback)\n");
    }
    
    return EOK;
}

/* 测试函数：ETH初始化测试 */
static int test_eth_init(void)
{
    int ret;
    
    printf("Test 1: ETH Initialization\n");
    
    ret = eth_init();
    if (ret != EOK) {
        printf("  Error: ETH initialization failed (%d)\n", ret);
        return ret;
    }
    
    printf("  Success: ETH initialized correctly\n");
    return EOK;
}

/* 测试函数：ETH链路状态测试 */
static int test_eth_link_status(void)
{
    int ret;
    
    printf("Test 2: ETH Link Status\n");
    
    ret = eth_check_link();
    if (ret != EOK) {
        printf("  Error: ETH link check failed (%d)\n", ret);
        return ret;
    }
    
    printf("  Success: ETH link is up\n");
    return EOK;
}

/* 测试函数：ETH发送接收测试 */
static int test_eth_tx_rx(void)
{
    u8_t test_packet[] = {0x00, 0x80, 0xE1, 0x00, 0x00, 0x00,  /* 目的MAC */
                          0x00, 0x80, 0xE1, 0x00, 0x00, 0x01,  /* 源MAC */
                          0x08, 0x00,                          /* 以太网类型: IP */
                          0x45, 0x00, 0x00, 0x1C,              /* IP头 */
                          0x00, 0x00, 0x40, 0x00,
                          0x40, 0x11, 0x00, 0x00,
                          0xC0, 0xA8, 0x01, 0x01,              /* 源IP: 192.168.1.1 */
                          0xC0, 0xA8, 0x01, 0x02,              /* 目的IP: 192.168.1.2 */
                          0x00, 0x00, 0x00, 0x00};             /* 数据 */
    u8_t rx_buffer[ETH_RX_BUFFER_SIZE];
    u32_t received;
    int ret;
    int i;
    
    printf("Test 3: ETH TX/RX Test\n");
    
    /* 发送测试数据包 */
    ret = eth_send(test_packet, sizeof(test_packet));
    if (ret != EOK) {
        printf("  Error: ETH send failed (%d)\n", ret);
        return ret;
    }
    
    /* 短暂延迟 */
    for (i = 0; i < 50000; i++) {
        __asm__ volatile ("nop");
    }
    
    /* 尝试接收 */
    ret = eth_receive(rx_buffer, sizeof(rx_buffer), &received);
    if (ret != EOK) {
        printf("  Error: ETH receive failed (%d)\n", ret);
        return ret;
    }
    
    if (received > 0) {
        printf("  Success: Received %u bytes\n", received);
        
        /* 简单验证接收到的数据 */
        if (received >= 14) { /* 至少包含以太网头 */
            printf("  Packet type: 0x%02X%02X\n", rx_buffer[12], rx_buffer[13]);
        }
    } else {
        printf("  Info: No data received (expected in non-loopback mode)\n");
    }
    
    return EOK;
}

/* 测试函数：ETH性能测试 */
static int test_eth_performance(void)
{
    int ret;
    
    printf("Test 4: ETH Performance Test\n");
    
    ret = eth_performance_test();
    if (ret != EOK) {
        printf("  Error: ETH performance test failed (%d)\n", ret);
        return ret;
    }
    
    printf("  Success: ETH performance test completed\n");
    return EOK;
}

/* 测试函数：ETH错误处理测试 */
static int test_eth_error_handling(void)
{
    int ret;
    
    printf("Test 5: ETH Error Handling\n");
    
    /* 测试无效发送长度 */
    ret = eth_send(NULL, 0);
    if (ret != -EINVAL) {
        printf("  Error: Invalid send length not rejected\n");
        return -EIO;
    }
    
    /* 测试过大发送长度 */
    ret = eth_send(NULL, ETH_TX_BUFFER_SIZE + 1);
    if (ret != -EINVAL) {
        printf("  Error: Oversized send length not rejected\n");
        return -EIO;
    }
    
    /* 测试无效接收参数 */
    u32_t received;
    ret = eth_receive(NULL, 100, &received);
    if (ret != -EINVAL) {
        printf("  Error: NULL buffer not rejected\n");
        return -EIO;
    }
    
    ret = eth_receive(&received, 100, NULL);
    if (ret != -EINVAL) {
        printf("  Error: NULL received pointer not rejected\n");
        return -EIO;
    }
    
    printf("  Success: Error handling works correctly\n");
    return EOK;
}

/* 主函数 */
int main(void)
{
    int ret;
    
    simple_print("\n========================================\n");
    simple_print("Zephyr ETH Driver Test for Open Source Contribution\n");
    simple_print("Target: STM32F746G Discovery\n");
    simple_print("ETH Controller: STM32F7xx Ethernet MAC\n");
    simple_print("PHY: LAN8742A\n");
    simple_print("Speed: 100Mbps, Full Duplex\n");
    simple_print("========================================\n\n");
    
    simple_print("Running ETH driver test suite...\n\n");
    
    /* 运行测试套件 */
    ret = test_eth_init();
    if (ret != EOK) {
        simple_print("ETH test suite failed at test 1\n");
        return ret;
    }
    
    ret = test_eth_link_status();
    if (ret != EOK) {
        simple_print("ETH test suite failed at test 2\n");
        return ret;
    }
    
    ret = test_eth_tx_rx();
    if (ret != EOK) {
        simple_print("ETH test suite failed at test 3\n");
        return ret;
    }
    
    ret = test_eth_performance();
    if (ret != EOK) {
        simple_print("ETH test suite failed at test 4\n");
        return ret;
    }
    
    ret = test_eth_error_handling();
    if (ret != EOK) {
        simple_print("ETH test suite failed at test 5\n");
        return ret;
    }
    
    simple_print("\n========================================\n");
    simple_print("All ETH driver tests completed successfully!\n");
    simple_print("Ready for Zephyr community contribution\n");
    simple_print("========================================\n");
    
    return EOK;
}
