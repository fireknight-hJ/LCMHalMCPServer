// 简单的系统调用桩函数
// 用于嵌入式系统，避免链接标准库

#include <errno.h>
#include <sys/stat.h>
#include <sys/types.h>

// 内存分配
void *_sbrk(int incr) {
    extern char _end; // 由链接器脚本定义
    static char *heap_end = 0;
    char *prev_heap_end;

    if (heap_end == 0) {
        heap_end = &_end;
    }
    prev_heap_end = heap_end;

    // 简单的堆实现，不检查边界
    heap_end += incr;
    return (void *)prev_heap_end;
}

// 退出
void _exit(int status) {
    (void)status;
    while (1) {
        // 无限循环
    }
}

// 写入
int _write(int file, char *ptr, int len) {
    (void)file;
    (void)ptr;
    (void)len;
    return -1; // 不支持
}

// 文件状态
int _fstat(int file, struct stat *st) {
    (void)file;
    st->st_mode = S_IFCHR;
    return 0;
}

// 是否为终端
int _isatty(int file) {
    (void)file;
    return 1;
}

// 关闭文件
int _close(int file) {
    (void)file;
    return -1;
}

// 杀死进程
int _kill(int pid, int sig) {
    (void)pid;
    (void)sig;
    errno = EINVAL;
    return -1;
}

// 获取进程ID
int _getpid(void) {
    return 1;
}

// 读取
int _read(int file, char *ptr, int len) {
    (void)file;
    (void)ptr;
    (void)len;
    return -1;
}

// 查找
int _lseek(int file, int ptr, int dir) {
    (void)file;
    (void)ptr;
    (void)dir;
    return 0;
}