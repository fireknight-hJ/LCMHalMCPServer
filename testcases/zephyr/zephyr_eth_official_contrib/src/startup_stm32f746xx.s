.syntax unified
.cpu cortex-m7
.fpu softvfp
.thumb

.global g_pfnVectors
.global Default_Handler

/* 启动代码 */
.section .isr_vector,"a",%progbits
.type g_pfnVectors, %object
.size g_pfnVectors, .-g_pfnVectors

g_pfnVectors:
    .word _estack
    .word Reset_Handler
    .word NMI_Handler
    .word HardFault_Handler
    .word MemManage_Handler
    .word BusFault_Handler
    .word UsageFault_Handler
    .word 0
    .word 0
    .word 0
    .word 0
    .word SVC_Handler
    .word DebugMon_Handler
    .word 0
    .word PendSV_Handler
    .word SysTick_Handler

    /* 外部中断 */
    .word WWDG_IRQHandler
    .word PVD_IRQHandler
    .word TAMP_STAMP_IRQHandler
    .word RTC_WKUP_IRQHandler
    .word FLASH_IRQHandler
    .word RCC_IRQHandler
    .word EXTI0_IRQHandler
    .word EXTI1_IRQHandler
    .word EXTI2_IRQHandler
    .word EXTI3_IRQHandler
    .word EXTI4_IRQHandler
    .word DMA1_Stream0_IRQHandler
    .word DMA1_Stream1_IRQHandler
    .word DMA1_Stream2_IRQHandler
    .word DMA1_Stream3_IRQHandler
    .word DMA1_Stream4_IRQHandler
    .word DMA1_Stream5_IRQHandler
    .word DMA1_Stream6_IRQHandler
    .word ADC_IRQHandler
    .word CAN1_TX_IRQHandler
    .word CAN1_RX0_IRQHandler
    .word CAN1_RX1_IRQHandler
    .word CAN1_SCE_IRQHandler
    .word EXTI9_5_IRQHandler
    .word TIM1_BRK_TIM9_IRQHandler
    .word TIM1_UP_TIM10_IRQHandler
    .word TIM1_TRG_COM_TIM11_IRQHandler
    .word TIM1_CC_IRQHandler
    .word TIM2_IRQHandler
    .word TIM3_IRQHandler
    .word TIM4_IRQHandler
    .word I2C1_EV_IRQHandler
    .word I2C1_ER_IRQHandler
    .word I2C2_EV_IRQHandler
    .word I2C2_ER_IRQHandler
    .word SPI1_IRQHandler
    .word SPI2_IRQHandler
    .word USART1_IRQHandler
    .word USART2_IRQHandler
    .word USART3_IRQHandler
    .word EXTI15_10_IRQHandler
    .word RTC_Alarm_IRQHandler
    .word OTG_FS_WKUP_IRQHandler
    .word TIM8_BRK_TIM12_IRQHandler
    .word TIM8_UP_TIM13_IRQHandler
    .word TIM8_TRG_COM_TIM14_IRQHandler
    .word TIM8_CC_IRQHandler
    .word DMA1_Stream7_IRQHandler
    .word FMC_IRQHandler
    .word SDMMC1_IRQHandler
    .word TIM5_IRQHandler
    .word SPI3_IRQHandler
    .word UART4_IRQHandler
    .word UART5_IRQHandler
    .word TIM6_DAC_IRQHandler
    .word TIM7_IRQHandler
    .word DMA2_Stream0_IRQHandler
    .word DMA2_Stream1_IRQHandler
    .word DMA2_Stream2_IRQHandler
    .word DMA2_Stream3_IRQHandler
    .word DMA2_Stream4_IRQHandler
    .word ETH_IRQHandler
    .word ETH_WKUP_IRQHandler
    .word CAN2_TX_IRQHandler
    .word CAN2_RX0_IRQHandler
    .word CAN2_RX1_IRQHandler
    .word CAN2_SCE_IRQHandler
    .word OTG_FS_IRQHandler
    .word DMA2_Stream5_IRQHandler
    .word DMA2_Stream6_IRQHandler
    .word DMA2_Stream7_IRQHandler
    .word USART6_IRQHandler
    .word I2C3_EV_IRQHandler
    .word I2C3_ER_IRQHandler
    .word OTG_HS_EP1_OUT_IRQHandler
    .word OTG_HS_EP1_IN_IRQHandler
    .word OTG_HS_WKUP_IRQHandler
    .word OTG_HS_IRQHandler
    .word DCMI_IRQHandler
    .word 0
    .word RNG_IRQHandler
    .word FPU_IRQHandler
    .word UART7_IRQHandler
    .word UART8_IRQHandler
    .word SPI4_IRQHandler
    .word SPI5_IRQHandler
    .word SPI6_IRQHandler
    .word SAI1_IRQHandler
    .word LTDC_IRQHandler
    .word LTDC_ER_IRQHandler
    .word DMA2D_IRQHandler

/* 弱定义默认中断处理程序 */
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

/* 弱定义所有中断处理程序为默认处理程序 */
.macro weak_handler name
    .weak \name
    .thumb_set \name,Default_Handler
.endm

weak_handler WWDG_IRQHandler
weak_handler PVD_IRQHandler
weak_handler TAMP_STAMP_IRQHandler
weak_handler RTC_WKUP_IRQHandler
weak_handler FLASH_IRQHandler
weak_handler RCC_IRQHandler
weak_handler EXTI0_IRQHandler
weak_handler EXTI1_IRQHandler
weak_handler EXTI2_IRQHandler
weak_handler EXTI3_IRQHandler
weak_handler EXTI4_IRQHandler
weak_handler DMA1_Stream0_IRQHandler
weak_handler DMA1_Stream1_IRQHandler
weak_handler DMA1_Stream2_IRQHandler
weak_handler DMA1_Stream3_IRQHandler
weak_handler DMA1_Stream4_IRQHandler
weak_handler DMA1_Stream5_IRQHandler
weak_handler DMA1_Stream6_IRQHandler
weak_handler ADC_IRQHandler
weak_handler CAN1_TX_IRQHandler
weak_handler CAN1_RX0_IRQHandler
weak_handler CAN1_RX1_IRQHandler
weak_handler CAN1_SCE_IRQHandler
weak_handler EXTI9_5_IRQHandler
weak_handler TIM1_BRK_TIM9_IRQHandler
weak_handler TIM1_UP_TIM10_IRQHandler
weak_handler TIM1_TRG_COM_TIM11_IRQHandler
weak_handler TIM1_CC_IRQHandler
weak_handler TIM2_IRQHandler
weak_handler TIM3_IRQHandler
weak_handler TIM4_IRQHandler
weak_handler I2C1_EV_IRQHandler
weak_handler I2C1_ER_IRQHandler
weak_handler I2C2_EV_IRQHandler
weak_handler I2C2_ER_IRQHandler
weak_handler SPI1_IRQHandler
weak_handler SPI2_IRQHandler
weak_handler USART1_IRQHandler
weak_handler USART2_IRQHandler
weak_handler USART3_IRQHandler
weak_handler EXTI15_10_IRQHandler
weak_handler RTC_Alarm_IRQHandler
weak_handler OTG_FS_WKUP_IRQHandler
weak_handler TIM8_BRK_TIM12_IRQHandler
weak_handler TIM8_UP_TIM13_IRQHandler
weak_handler TIM8_TRG_COM_TIM14_IRQHandler
weak_handler TIM8_CC_IRQHandler
weak_handler DMA1_Stream7_IRQHandler
weak_handler FMC_IRQHandler
weak_handler SDMMC1_IRQHandler
weak_handler TIM5_IRQHandler
weak_handler SPI3_IRQHandler
weak_handler UART4_IRQHandler
weak_handler UART5_IRQHandler
weak_handler TIM6_DAC_IRQHandler
weak_handler TIM7_IRQHandler
weak_handler DMA2_Stream0_IRQHandler
weak_handler DMA2_Stream1_IRQHandler
weak_handler DMA2_Stream2_IRQHandler
weak_handler DMA2_Stream3_IRQHandler
weak_handler DMA2_Stream4_IRQHandler
weak_handler ETH_IRQHandler
weak_handler ETH_WKUP_IRQHandler
weak_handler CAN2_TX_IRQHandler
weak_handler CAN2_RX0_IRQHandler
weak_handler CAN2_RX1_IRQHandler
weak_handler CAN2_SCE_IRQHandler
weak_handler OTG_FS_IRQHandler
weak_handler DMA2_Stream5_IRQHandler
weak_handler DMA2_Stream6_IRQHandler
weak_handler DMA2_Stream7_IRQHandler
weak_handler USART6_IRQHandler
weak_handler I2C3_EV_IRQHandler
weak_handler I2C3_ER_IRQHandler
weak_handler OTG_HS_EP1_OUT_IRQHandler
weak_handler OTG_HS_EP1_IN_IRQHandler
weak_handler OTG_HS_WKUP_IRQHandler
weak_handler OTG_HS_IRQHandler
weak_handler DCMI_IRQHandler
weak_handler RNG_IRQHandler
weak_handler FPU_IRQHandler
weak_handler UART7_IRQHandler
weak_handler UART8_IRQHandler
weak_handler SPI4_IRQHandler
weak_handler SPI5_IRQHandler
weak_handler SPI6_IRQHandler
weak_handler SAI1_IRQHandler
weak_handler LTDC_IRQHandler
weak_handler LTDC_ER_IRQHandler
weak_handler DMA2D_IRQHandler

.section .text.Reset_Handler
.weak Reset_Handler
.type Reset_Handler, %function
Reset_Handler:
    ldr r0, =_estack
    mov sp, r0
    
    /* 复制.data段从FLASH到RAM */
    ldr r0, =_sidata
    ldr r1, =_sdata
    ldr r2, =_edata
    cmp r1, r2
    beq copy_data_done
copy_data_loop:
    ldr r3, [r0], #4
    str r3, [r1], #4
    cmp r1, r2
    blt copy_data_loop
copy_data_done:
    
    /* 清零.bss段 */
    ldr r0, =_sbss
    ldr r1, =_ebss
    mov r2, #0
    cmp r0, r1
    beq zero_bss_done
zero_bss_loop:
    str r2, [r0], #4
    cmp r0, r1
    blt zero_bss_loop
zero_bss_done:
    
    /* 清零.ccmram段 */
    ldr r0, =_sccmram
    ldr r1, =_eccmram
    cmp r0, r1
    beq zero_ccmram_done
zero_ccmram_loop:
    str r2, [r0], #4
    cmp r0, r1
    blt zero_ccmram_loop
zero_ccmram_done:
    
    /* 调用SystemInit */
    bl SystemInit
    
    /* 调用main函数 */
    bl main
    
    /* 如果main返回，进入无限循环 */
    b .

.section .text.Default_Handler
.weak Default_Handler
.type Default_Handler, %function
Default_Handler:
    b Default_Handler

/* 移除有问题的.size指令 */
/* .size Reset_Handler, .-Reset_Handler */
