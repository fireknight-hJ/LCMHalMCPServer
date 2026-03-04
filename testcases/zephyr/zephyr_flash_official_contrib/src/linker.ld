/* 
 * Zephyr官方Flash驱动测试 - 链接器脚本
 * 针对STM32F103C8T6 (Blue Pill) - 64KB Flash, 20KB RAM
 * 特别注意：Flash驱动需要访问Flash控制器寄存器
 */

MEMORY
{
    FLASH (rx) : ORIGIN = 0x08000000, LENGTH = 64K
    RAM (rwx)  : ORIGIN = 0x20000000, LENGTH = 20K
    PERIPH (rw) : ORIGIN = 0x40000000, LENGTH = 512M  /* 外设区域 */
}

SECTIONS
{
    /* 中断向量表 */
    .isr_vector :
    {
        . = ALIGN(4);
        KEEP(*(.isr_vector))
        . = ALIGN(4);
    } > FLASH

    /* 代码段 */
    .text :
    {
        . = ALIGN(4);
        *(.text)
        *(.text*)
        *(.glue_7)
        *(.glue_7t)
        *(.eh_frame)
        
        KEEP (*(.init))
        KEEP (*(.fini))
        
        . = ALIGN(4);
        _etext = .;
    } > FLASH

    /* 只读数据段 */
    .rodata :
    {
        . = ALIGN(4);
        *(.rodata)
        *(.rodata*)
        . = ALIGN(4);
    } > FLASH

    /* ARM特定段 */
    .ARM.extab :
    {
        *(.ARM.extab* .gnu.linkonce.armextab.*)
    } > FLASH
    
    .ARM :
    {
        __exidx_start = .;
        *(.ARM.exidx*)
        __exidx_end = .;
    } > FLASH

    /* 预初始化数组 */
    .preinit_array :
    {
        PROVIDE_HIDDEN (__preinit_array_start = .);
        KEEP (*(.preinit_array*))
        PROVIDE_HIDDEN (__preinit_array_end = .);
    } > FLASH

    /* 初始化数组 */
    .init_array :
    {
        PROVIDE_HIDDEN (__init_array_start = .);
        KEEP (*(SORT(.init_array.*)))
        KEEP (*(.init_array*))
        PROVIDE_HIDDEN (__init_array_end = .);
    } > FLASH

    /* 结束数组 */
    .fini_array :
    {
        PROVIDE_HIDDEN (__fini_array_start = .);
        KEEP (*(SORT(.fini_array.*)))
        KEEP (*(.fini_array*))
        PROVIDE_HIDDEN (__fini_array_end = .);
    } > FLASH

    /* 数据段 (初始值在Flash，运行时在RAM) */
    _sidata = LOADADDR(.data);
    
    .data :
    {
        . = ALIGN(4);
        _sdata = .;
        *(.data)
        *(.data*)
        . = ALIGN(4);
        _edata = .;
    } > RAM AT > FLASH

    /* 未初始化数据段 (BSS) */
    .bss :
    {
        . = ALIGN(4);
        _sbss = .;
        *(.bss)
        *(.bss*)
        *(COMMON)
        . = ALIGN(4);
        _ebss = .;
    } > RAM

    /* Flash控制器寄存器段（只读） */
    .flash_registers (NOLOAD) :
    {
        . = ALIGN(4);
        KEEP(*(.flash_registers))
        . = ALIGN(4);
    } > PERIPH

    /* 用户堆栈段 */
    ._user_heap_stack :
    {
        . = ALIGN(8);
        PROVIDE ( end = . );
        PROVIDE ( _end = . );
        . = . + _Min_Heap_Size;
        . = . + _Min_Stack_Size;
        . = ALIGN(8);
    } > RAM

    /* 移除调试信息 */
    /DISCARD/ :
    {
        libc.a ( * )
        libm.a ( * )
        libgcc.a ( * )
    }

    /* 定义堆和栈大小 */
    _Min_Heap_Size = 0x200;
    _Min_Stack_Size = 0x400;
    
    /* Flash测试数据区域 */
    _flash_test_area = 0x08004000;  /* 测试区域：从16KB开始 */
    _flash_test_size = 0x1000;      /* 测试区域大小：4KB */
    
    /* 入口点 - ARM Cortex-M需要Reset_Handler */
    ENTRY(Reset_Handler)
}

/* 符号定义 */
PROVIDE(_estack = ORIGIN(RAM) + LENGTH(RAM));

/* 提供Reset_Handler的强定义，指向实际的Reset_Handler函数 */
/* Reset_Handler已经在启动文件中定义 */

/* Flash相关符号 */
PROVIDE(FLASH_BASE = 0x40022000);
PROVIDE(FLASH_ACR = FLASH_BASE);
PROVIDE(FLASH_KEYR = FLASH_BASE + 0x04);
PROVIDE(FLASH_OPTKEYR = FLASH_BASE + 0x08);
PROVIDE(FLASH_SR = FLASH_BASE + 0x0C);
PROVIDE(FLASH_CR = FLASH_BASE + 0x10);
PROVIDE(FLASH_AR = FLASH_BASE + 0x14);
PROVIDE(FLASH_OBR = FLASH_BASE + 0x1C);
PROVIDE(FLASH_WRPR = FLASH_BASE + 0x20);