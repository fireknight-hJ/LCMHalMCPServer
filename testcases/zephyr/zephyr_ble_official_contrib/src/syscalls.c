/*
 * System call implementations for BLE test application
 * Minimal implementations for printf and basic I/O
 */

#include <stdint.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <stdarg.h>
#include <stdio.h>
#include <sys/stat.h>
#include <sys/times.h>

/* Zephyr style types */
typedef uint32_t u32_t;
typedef int32_t s32_t;

/* Weak implementations of hardware abstraction functions */
int __attribute__((weak)) HAL_BE_return_0(void) { return 0; }
int __attribute__((weak)) HAL_BE_return_1(void) { return 1; }
int __attribute__((weak)) HAL_BE_Out(int len) { return len; }
int __attribute__((weak)) HAL_BE_In(void* buf, int len) { return len; }

/* Simple putchar implementation */
int _write(int file, char *ptr, int len)
{
    int i;
    
    if (file != 1 && file != 2) { /* stdout or stderr */
        return -1;
    }
    
    for (i = 0; i < len; i++) {
        /* Simple character output - can be replaced with UART output */
        HAL_BE_Out(ptr[i]);
    }
    
    return len;
}

/* Simple getchar implementation */
int _read(int file, char *ptr, int len)
{
    int i;
    
    if (file != 0) { /* stdin */
        return -1;
    }
    
    for (i = 0; i < len; i++) {
        /* Simple character input - can be replaced with UART input */
        int ch = HAL_BE_In(ptr + i, 1);
        if (ch <= 0) {
            break;
        }
    }
    
    return i;
}

/* Close implementation */
int _close(int file)
{
    return -1; /* Not supported */
}

/* Seek implementation */
int _lseek(int file, int ptr, int dir)
{
    return 0; /* Not supported */
}

/* Fstat implementation */
int _fstat(int file, struct stat *st)
{
    st->st_mode = S_IFCHR;
    return 0;
}

/* Isatty implementation */
int _isatty(int file)
{
    return 1; /* Treat all files as terminals */
}

/* Exit implementation */
void _exit(int status)
{
    while (1) {
        /* Infinite loop on exit */
        __asm__ volatile ("nop");
    }
}

/* Kill implementation */
int _kill(int pid, int sig)
{
    errno = EINVAL;
    return -1;
}

/* Getpid implementation */
int _getpid(void)
{
    return 1;
}

/* Sbrk implementation for heap management */
extern char _end; /* Defined by linker */
extern char _estack; /* Defined by linker */

caddr_t _sbrk(int incr)
{
    static char *heap_end = 0;
    char *prev_heap_end;
    
    if (heap_end == 0) {
        heap_end = &_end;
    }
    
    prev_heap_end = heap_end;
    
    /* Check for heap overflow */
    if (heap_end + incr > &_estack) {
        errno = ENOMEM;
        return (caddr_t)-1;
    }
    
    heap_end += incr;
    return (caddr_t)prev_heap_end;
}

/* Dummy implementations for unused system calls */
int _open(const char *name, int flags, int mode)
{
    return -1;
}

int _wait(int *status)
{
    errno = ECHILD;
    return -1;
}

int _unlink(const char *name)
{
    errno = ENOENT;
    return -1;
}

int _times(struct tms *buf)
{
    return -1;
}

int _stat(const char *file, struct stat *st)
{
    st->st_mode = S_IFCHR;
    return 0;
}

int _link(const char *old, const char *new)
{
    errno = EMLINK;
    return -1;
}

int _fork(void)
{
    errno = EAGAIN;
    return -1;
}

int _execve(const char *name, char *const *argv, char *const *env)
{
    errno = ENOMEM;
    return -1;
}

/* Simple print function for test output */
void simple_print(const char *str)
{
    _write(1, (char *)str, strlen(str));
}

/* Minimal printf implementation */
int printf(const char *format, ...)
{
    char buffer[128];
    va_list args;
    int len;
    
    va_start(args, format);
    len = vsnprintf(buffer, sizeof(buffer), format, args);
    va_end(args);
    
    if (len > 0) {
        _write(1, buffer, len);
    }
    
    return len;
}

/* Minimal puts implementation */
int puts(const char *str)
{
    int len = strlen(str);
    _write(1, (char *)str, len);
    _write(1, "\n", 1);
    return len + 1;
}

/* Minimal putchar implementation */
int putchar(int ch)
{
    char c = ch;
    _write(1, &c, 1);
    return ch;
}