/* Linker script for nRF52840 BLE test application */

MEMORY
{
    FLASH (rx) : ORIGIN = 0x00000000, LENGTH = 1024K
    RAM (rwx) : ORIGIN = 0x20000000, LENGTH = 256K
}

/* Stack pointer definition */
_estack = ORIGIN(RAM) + LENGTH(RAM);

SECTIONS
{
    /* Vector table at the beginning of FLASH */
    .isr_vector :
    {
        . = ALIGN(4);
        KEEP(*(.isr_vector))
        . = ALIGN(4);
    } > FLASH

    /* Code section */
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

    /* Constant data */
    .rodata :
    {
        . = ALIGN(4);
        *(.rodata)
        *(.rodata*)
        . = ALIGN(4);
    } > FLASH

    /* ARM exception handling */
    .ARM.extab :
    {
        *(.ARM.extab* .gnu.linkonce.armextab.*)
    } > FLASH
    
    .ARM.exidx :
    {
        __exidx_start = .;
        *(.ARM.exidx* .gnu.linkonce.armexidx.*)
        __exidx_end = .;
    } > FLASH

    /* Pre-initialization array */
    .preinit_array :
    {
        PROVIDE_HIDDEN (__preinit_array_start = .);
        KEEP (*(.preinit_array*))
        PROVIDE_HIDDEN (__preinit_array_end = .);
    } > FLASH

    /* Initialization array */
    .init_array :
    {
        PROVIDE_HIDDEN (__init_array_start = .);
        KEEP (*(SORT(.init_array.*)))
        KEEP (*(.init_array*))
        PROVIDE_HIDDEN (__init_array_end = .);
    } > FLASH

    /* Finalization array */
    .fini_array :
    {
        PROVIDE_HIDDEN (__fini_array_start = .);
        KEEP (*(SORT(.fini_array.*)))
        KEEP (*(.fini_array*))
        PROVIDE_HIDDEN (__fini_array_end = .);
    } > FLASH

    /* Used for unwinding */
    .ARM.attributes 0 : { *(.ARM.attributes) }

    /* Data section - initialized variables */
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

    /* BSS section - uninitialized variables */
    .bss :
    {
        . = ALIGN(4);
        _sbss = .;
        __bss_start__ = _sbss;
        *(.bss)
        *(.bss*)
        *(COMMON)
        . = ALIGN(4);
        _ebss = .;
        __bss_end__ = _ebss;
    } > RAM

    /* Heap */
    .heap (NOLOAD) :
    {
        . = ALIGN(8);
        __heap_start__ = .;
        end = __heap_start__;
        _end = end;
        __end = end;
        . = . + 64K; /* 64KB heap */
        __heap_end__ = .;
        __HeapLimit = __heap_end__;
    } > RAM

    /* Stack */
    .stack (NOLOAD) :
    {
        . = ALIGN(8);
        __stack_start__ = .;
        . = . + 16K; /* 16KB stack */
        __stack_end__ = .;
        __StackLimit = __stack_start__;
        __StackTop = __stack_end__;
        PROVIDE(__stack = __StackTop);
    } > RAM

    /* Check for enough RAM */
    ._check_stack :
    {
        . = ALIGN(4);
        . = . + 4K; /* Minimum stack space */
    } > RAM

    /* Discard sections */
    /DISCARD/ :
    {
        libc.a ( * )
        libm.a ( * )
        libgcc.a ( * )
    }

    /* Define symbols for startup code */
    __flash_start = ORIGIN(FLASH);
    __flash_size = LENGTH(FLASH);
    __ram_start = ORIGIN(RAM);
    __ram_size = LENGTH(RAM);
    __heap_size = __heap_end__ - __heap_start__;
    __stack_size = __stack_end__ - __stack_start__;
}