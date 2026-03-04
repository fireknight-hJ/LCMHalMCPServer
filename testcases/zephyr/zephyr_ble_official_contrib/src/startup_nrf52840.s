/* 
 * nRF52840 启动文件
 * 为Zephyr BLE驱动测试提供正确的中断向量表
 * Cortex-M4 with FPU
 */

.syntax unified
.cpu cortex-m4
.fpu fpv4-sp-d16
.thumb

/* 向量表 */
.section .isr_vector,"a",%progbits
.type vector_table, %object
.size vector_table, .-vector_table

vector_table:
    .word _estack                 /* 初始堆栈指针值 */
    .word Reset_Handler           /* 复位处理程序 */
    .word NMI_Handler             /* NMI处理程序 */
    .word HardFault_Handler       /* 硬错误处理程序 */
    .word MemManage_Handler       /* MPU错误处理程序 */
    .word BusFault_Handler        /* 总线错误处理程序 */
    .word UsageFault_Handler      /* 使用错误处理程序 */
    .word 0                       /* 保留 */
    .word 0                       /* 保留 */
    .word 0                       /* 保留 */
    .word 0                       /* 保留 */
    .word SVC_Handler             /* SVCall处理程序 */
    .word DebugMon_Handler        /* 调试监控处理程序 */
    .word 0                       /* 保留 */
    .word PendSV_Handler          /* PendSV处理程序 */
    .word SysTick_Handler         /* SysTick处理程序 */

    /* nRF52840 外部中断 - 只定义前几个重要的 */
    .word POWER_CLOCK_IRQHandler  /* 电源时钟中断 */
    .word RADIO_IRQHandler        /* 无线电中断 (BLE) */
    .word UARTE0_UART0_IRQHandler /* UART0中断 */
    .word SPIM0_SPIS0_TWIM0_TWIS0_SPI0_TWI0_IRQHandler /* SPI/TWI0中断 */
    .word SPIM1_SPIS1_TWIM1_TWIS1_SPI1_TWI1_IRQHandler /* SPI/TWI1中断 */
    .word NFCT_IRQHandler         /* NFC中断 */
    .word GPIOTE_IRQHandler       /* GPIO任务和事件中断 */
    .word SAADC_IRQHandler        /* ADC中断 */
    .word TIMER0_IRQHandler       /* 定时器0中断 */
    .word TIMER1_IRQHandler       /* 定时器1中断 */
    .word TIMER2_IRQHandler       /* 定时器2中断 */
    .word RTC0_IRQHandler         /* RTC0中断 */
    .word TEMP_IRQHandler         /* 温度传感器中断 */
    .word RNG_IRQHandler          /* 随机数生成器中断 */
    .word ECB_IRQHandler          /* ECB加密中断 */
    .word CCM_AAR_IRQHandler      /* CCM/AAR加密中断 */
    .word WDT_IRQHandler          /* 看门狗定时器中断 */
    .word RTC1_IRQHandler         /* RTC1中断 */
    .word QDEC_IRQHandler         /* 正交解码器中断 */
    .word COMP_LPCOMP_IRQHandler  /* 比较器中断 */
    .word SWI0_EGU0_IRQHandler    /* 软件中断0/EGU0 */
    .word SWI1_EGU1_IRQHandler    /* 软件中断1/EGU1 */
    .word SWI2_EGU2_IRQHandler    /* 软件中断2/EGU2 */
    .word SWI3_EGU3_IRQHandler    /* 软件中断3/EGU3 */
    .word SWI4_EGU4_IRQHandler    /* 软件中断4/EGU4 */
    .word SWI5_EGU5_IRQHandler    /* 软件中断5/EGU5 */
    .word TIMER3_IRQHandler       /* 定时器3中断 */
    .word TIMER4_IRQHandler       /* 定时器4中断 */
    .word PWM0_IRQHandler         /* PWM0中断 */
    .word PDM_IRQHandler          /* PDM中断 */
    .word 0                       /* 保留 */
    .word 0                       /* 保留 */
    .word MWU_IRQHandler          /* 内存保护单元中断 */
    .word PWM1_IRQHandler         /* PWM1中断 */
    .word PWM2_IRQHandler         /* PWM2中断 */
    .word SPIM2_SPIS2_SPI2_IRQHandler /* SPI2中断 */
    .word RTC2_IRQHandler         /* RTC2中断 */
    .word I2S_IRQHandler          /* I2S中断 */
    .word FPU_IRQHandler          /* FPU中断 */

/* 复位处理程序 */
.section .text.Reset_Handler
.weak Reset_Handler
.type Reset_Handler, %function

Reset_Handler:
    /* 初始化.data段 */
    ldr r0, =_sidata
    ldr r1, =_sdata
    ldr r2, =_edata
    b copy_data_init

copy_data_loop:
    ldr r3, [r0], #4
    str r3, [r1], #4
copy_data_init:
    cmp r1, r2
    blt copy_data_loop

    /* 清零.bss段 */
    ldr r0, =_sbss
    ldr r1, =_ebss
    mov r2, #0
    b zero_bss_init

zero_bss_loop:
    str r2, [r0], #4
zero_bss_init:
    cmp r0, r1
    blt zero_bss_loop

    /* 直接调用main函数 */
    ldr r0, =main
    bx r0

/* 弱定义的中断处理程序 */
.section .text.Default_Handler,"ax",%progbits
Default_Handler:
Infinite_Loop:
    b Infinite_Loop

.weak NMI_Handler
.thumb_set NMI_Handler,Default_Handler

.weak HardFault_Handler
.thumb_set HardFault_Handler,Default_Handler

.weak MemManage_Handler
.thumb_set MemManage_Handler,Default_Handler

.weak BusFault_Handler
.thumb_set BusFault_Handler,Default_Handler

.weak UsageFault_Handler
.thumb_set UsageFault_Handler,Default_Handler

.weak SVC_Handler
.thumb_set SVC_Handler,Default_Handler

.weak DebugMon_Handler
.thumb_set DebugMon_Handler,Default_Handler

.weak PendSV_Handler
.thumb_set PendSV_Handler,Default_Handler

.weak SysTick_Handler
.thumb_set SysTick_Handler,Default_Handler

/* nRF52840 特定中断处理程序 */
.weak POWER_CLOCK_IRQHandler
.thumb_set POWER_CLOCK_IRQHandler,Default_Handler

.weak RADIO_IRQHandler
.thumb_set RADIO_IRQHandler,Default_Handler

.weak UARTE0_UART0_IRQHandler
.thumb_set UARTE0_UART0_IRQHandler,Default_Handler

.weak SPIM0_SPIS0_TWIM0_TWIS0_SPI0_TWI0_IRQHandler
.thumb_set SPIM0_SPIS0_TWIM0_TWIS0_SPI0_TWI0_IRQHandler,Default_Handler

.weak SPIM1_SPIS1_TWIM1_TWIS1_SPI1_TWI1_IRQHandler
.thumb_set SPIM1_SPIS1_TWIM1_TWIS1_SPI1_TWI1_IRQHandler,Default_Handler

.weak NFCT_IRQHandler
.thumb_set NFCT_IRQHandler,Default_Handler

.weak GPIOTE_IRQHandler
.thumb_set GPIOTE_IRQHandler,Default_Handler

.weak SAADC_IRQHandler
.thumb_set SAADC_IRQHandler,Default_Handler

.weak TIMER0_IRQHandler
.thumb_set TIMER0_IRQHandler,Default_Handler

.weak TIMER1_IRQHandler
.thumb_set TIMER1_IRQHandler,Default_Handler

.weak TIMER2_IRQHandler
.thumb_set TIMER2_IRQHandler,Default_Handler

.weak RTC0_IRQHandler
.thumb_set RTC0_IRQHandler,Default_Handler

.weak TEMP_IRQHandler
.thumb_set TEMP_IRQHandler,Default_Handler

.weak RNG_IRQHandler
.thumb_set RNG_IRQHandler,Default_Handler

.weak ECB_IRQHandler
.thumb_set ECB_IRQHandler,Default_Handler

.weak CCM_AAR_IRQHandler
.thumb_set CCM_AAR_IRQHandler,Default_Handler

.weak WDT_IRQHandler
.thumb_set WDT_IRQHandler,Default_Handler

.weak RTC1_IRQHandler
.thumb_set RTC1_IRQHandler,Default_Handler

.weak QDEC_IRQHandler
.thumb_set QDEC_IRQHandler,Default_Handler

.weak COMP_LPCOMP_IRQHandler
.thumb_set COMP_LPCOMP_IRQHandler,Default_Handler

.weak SWI0_EGU0_IRQHandler
.thumb_set SWI0_EGU0_IRQHandler,Default_Handler

.weak SWI1_EGU1_IRQHandler
.thumb_set SWI1_EGU1_IRQHandler,Default_Handler

.weak SWI2_EGU2_IRQHandler
.thumb_set SWI2_EGU2_IRQHandler,Default_Handler

.weak SWI3_EGU3_IRQHandler
.thumb_set SWI3_EGU3_IRQHandler,Default_Handler

.weak SWI4_EGU4_IRQHandler
.thumb_set SWI4_EGU4_IRQHandler,Default_Handler

.weak SWI5_EGU5_IRQHandler
.thumb_set SWI5_EGU5_IRQHandler,Default_Handler

.weak TIMER3_IRQHandler
.thumb_set TIMER3_IRQHandler,Default_Handler

.weak TIMER4_IRQHandler
.thumb_set TIMER4_IRQHandler,Default_Handler

.weak PWM0_IRQHandler
.thumb_set PWM0_IRQHandler,Default_Handler

.weak PDM_IRQHandler
.thumb_set PDM_IRQHandler,Default_Handler

.weak MWU_IRQHandler
.thumb_set MWU_IRQHandler,Default_Handler

.weak PWM1_IRQHandler
.thumb_set PWM1_IRQHandler,Default_Handler

.weak PWM2_IRQHandler
.thumb_set PWM2_IRQHandler,Default_Handler

.weak SPIM2_SPIS2_SPI2_IRQHandler
.thumb_set SPIM2_SPIS2_SPI2_IRQHandler,Default_Handler

.weak RTC2_IRQHandler
.thumb_set RTC2_IRQHandler,Default_Handler

.weak I2S_IRQHandler
.thumb_set I2S_IRQHandler,Default_Handler

.weak FPU_IRQHandler
.thumb_set FPU_IRQHandler,Default_Handler