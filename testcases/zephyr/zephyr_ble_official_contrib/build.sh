#!/bin/bash

# Zephyr BLE驱动测试构建脚本
# 目标：nRF52840 Development Kit

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# 项目根目录
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC_DIR="$PROJECT_ROOT/src"
BUILD_DIR="$PROJECT_ROOT/build"

# 工具链配置
# 使用ARM GCC工具链
ARM_TOOLCHAIN_PREFIX="arm-none-eabi"
CC="${ARM_TOOLCHAIN_PREFIX}-gcc"
CXX="${ARM_TOOLCHAIN_PREFIX}-g++"
AS="${ARM_TOOLCHAIN_PREFIX}-as"
LD="${ARM_TOOLCHAIN_PREFIX}-ld"
OBJCOPY="${ARM_TOOLCHAIN_PREFIX}-objcopy"
OBJDUMP="${ARM_TOOLCHAIN_PREFIX}-objdump"
SIZE="${ARM_TOOLCHAIN_PREFIX}-size"

# 检查工具链
check_toolchain() {
    echo -e "${YELLOW}检查工具链...${NC}"
    
    local missing_tools=()
    
    for tool in "$CC" "$CXX" "$AS" "$LD" "$OBJCOPY" "$OBJDUMP" "$SIZE"; do
        if ! command -v "$tool" &> /dev/null; then
            missing_tools+=("$tool")
        fi
    done
    
    if [ ${#missing_tools[@]} -ne 0 ]; then
        echo -e "${RED}错误：缺少以下工具：${NC}"
        for tool in "${missing_tools[@]}"; do
            echo "  $tool"
        done
        echo -e "\n请安装ARM GCC工具链："
        echo "  Ubuntu/Debian: sudo apt install gcc-arm-none-eabi"
        echo "  macOS: brew install arm-none-eabi-gcc"
        echo "  Windows: 下载并安装ARM GCC工具链"
        exit 1
    fi
    
    echo -e "${GREEN}工具链检查通过${NC}"
}

# 清理构建目录
clean_build() {
    echo -e "${YELLOW}清理构建目录...${NC}"
    rm -rf "$BUILD_DIR"
    mkdir -p "$BUILD_DIR"
}

# 编译源文件
compile_sources() {
    echo -e "${YELLOW}编译源文件...${NC}"
    
    # 编译器标志
    CFLAGS="\
        -mcpu=cortex-m4 \
        -mthumb \
        -mfloat-abi=hard \
        -mfpu=fpv4-sp-d16 \
        -ffunction-sections \
        -fdata-sections \
        -Wall \
        -Wextra \
        -Werror \
        -Wno-unused-parameter \
        -Wno-unused-variable \
        -Wno-unused-function \
        -Os \
        -std=c11 \
        -I$SRC_DIR"
    
    # 汇编器标志
    ASFLAGS="\
        -mcpu=cortex-m4 \
        -mthumb \
        -mfloat-abi=hard \
        -mfpu=fpv4-sp-d16"
    
    # 编译C文件
    for c_file in "$SRC_DIR"/*.c; do
        if [ -f "$c_file" ]; then
            local obj_file="$BUILD_DIR/$(basename "${c_file%.c}").o"
            echo "  编译: $(basename "$c_file")"
            $CC $CFLAGS -c "$c_file" -o "$obj_file"
        fi
    done
    
    # 编译汇编文件
    for s_file in "$SRC_DIR"/*.s; do
        if [ -f "$s_file" ]; then
            local obj_file="$BUILD_DIR/$(basename "${s_file%.s}").o"
            echo "  汇编: $(basename "$s_file")"
            $AS $ASFLAGS "$s_file" -o "$obj_file"
        fi
    done
}

# 链接目标文件
link_objects() {
    echo -e "${YELLOW}链接目标文件...${NC}"
    
    # 链接器标志
    LDFLAGS="\
        -mcpu=cortex-m4 \
        -mthumb \
        -mfloat-abi=hard \
        -mfpu=fpv4-sp-d16 \
        -T$SRC_DIR/linker.ld \
        -nostartfiles \
        -nostdlib \
        -Wl,--gc-sections \
        -Wl,--print-memory-usage \
        -Wl,-Map=$BUILD_DIR/zephyr_ble_test.map"
    
    # 收集所有目标文件
    local obj_files=()
    for obj_file in "$BUILD_DIR"/*.o; do
        if [ -f "$obj_file" ]; then
            obj_files+=("$obj_file")
        fi
    done
    
    if [ ${#obj_files[@]} -eq 0 ]; then
        echo -e "${RED}错误：没有找到目标文件${NC}"
        exit 1
    fi
    
    # 链接
    $CC $LDFLAGS "${obj_files[@]}" -o "$BUILD_DIR/zephyr_ble_test.elf"
    
    # 生成二进制文件
    $OBJCOPY -O binary "$BUILD_DIR/zephyr_ble_test.elf" "$BUILD_DIR/zephyr_ble_test.bin"
    
    # 生成反汇编文件
    $OBJDUMP -d "$BUILD_DIR/zephyr_ble_test.elf" > "$BUILD_DIR/zephyr_ble_test.dis"
    
    # 生成hex文件
    $OBJCOPY -O ihex "$BUILD_DIR/zephyr_ble_test.elf" "$BUILD_DIR/zephyr_ble_test.hex"
}

# 显示构建信息
show_build_info() {
    echo -e "${YELLOW}构建信息：${NC}"
    
    # 显示文件大小
    echo -e "\n${GREEN}文件大小：${NC}"
    $SIZE "$BUILD_DIR/zephyr_ble_test.elf"
    
    # 显示生成的文件
    echo -e "\n${GREEN}生成的文件：${NC}"
    ls -la "$BUILD_DIR"/*.elf "$BUILD_DIR"/*.bin "$BUILD_DIR"/*.hex 2>/dev/null || true
    
    # 显示内存使用情况
    echo -e "\n${GREEN}内存使用情况：${NC}"
    if [ -f "$BUILD_DIR/zephyr_ble_test.map" ]; then
        grep -E "(Memory Configuration|__heap_start__|__heap_end__|__stack_start__|__stack_end__|_estack)" "$BUILD_DIR/zephyr_ble_test.map" | head -20
    fi
}

# 验证构建
validate_build() {
    echo -e "${YELLOW}验证构建...${NC}"
    
    if [ ! -f "$BUILD_DIR/zephyr_ble_test.elf" ]; then
        echo -e "${RED}错误：ELF文件未生成${NC}"
        exit 1
    fi
    
    if [ ! -f "$BUILD_DIR/zephyr_ble_test.bin" ]; then
        echo -e "${RED}错误：BIN文件未生成${NC}"
        exit 1
    fi
    
    # 检查ELF文件格式
    local file_type=$(file "$BUILD_DIR/zephyr_ble_test.elf")
    if ! echo "$file_type" | grep -q "ARM" || ! echo "$file_type" | grep -q "ELF"; then
        echo -e "${RED}错误：ELF文件格式不正确${NC}"
        echo "文件类型: $file_type"
        exit 1
    fi
    
    echo -e "${GREEN}构建验证通过${NC}"
}

# 主构建函数
main_build() {
    echo -e "${GREEN}========================================${NC}"
    echo -e "${GREEN}Zephyr BLE驱动测试构建${NC}"
    echo -e "${GREEN}目标：nRF52840 Development Kit${NC}"
    echo -e "${GREEN}========================================${NC}\n"
    
    # 检查工具链
    check_toolchain
    
    # 清理并创建构建目录
    clean_build
    
    # 编译源文件
    compile_sources
    
    # 链接目标文件
    link_objects
    
    # 验证构建
    validate_build
    
    # 显示构建信息
    show_build_info
    
    echo -e "\n${GREEN}========================================${NC}"
    echo -e "${GREEN}构建成功完成！${NC}"
    echo -e "${GREEN}输出文件位于：$BUILD_DIR${NC}"
    echo -e "${GREEN}========================================${NC}"
}

# 处理命令行参数
case "$1" in
    "clean")
        echo -e "${YELLOW}清理构建目录...${NC}"
        rm -rf "$BUILD_DIR"
        echo -e "${GREEN}清理完成${NC}"
        ;;
    "info")
        if [ -f "$BUILD_DIR/zephyr_ble_test.elf" ]; then
            show_build_info
        else
            echo -e "${RED}错误：请先运行构建${NC}"
            exit 1
        fi
        ;;
    "help"|"-h"|"--help")
        echo "用法: $0 [选项]"
        echo "选项:"
        echo "  clean   清理构建目录"
        echo "  info    显示构建信息"
        echo "  help    显示此帮助信息"
        echo ""
        echo "如果没有提供选项，则执行完整构建"
        ;;
    *)
        main_build
        ;;
esac