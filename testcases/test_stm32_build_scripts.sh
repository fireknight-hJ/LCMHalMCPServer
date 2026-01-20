#!/bin/bash

# STM32构建脚本测试工具
# 用于验证新创建的STM32外设构建脚本

echo "========================================"
echo "STM32构建脚本测试工具"
echo "========================================"
echo "测试时间: $(date)"
echo "工作目录: $(pwd)"
echo "========================================"

# 检查构建脚本是否存在
echo ""
echo "1. 检查构建脚本是否存在..."
echo "----------------------------------------"

SCRIPTS=(
    "uart_driver/build.sh"
    "uart_driver/clear.sh"
    "flash_driver/build.sh"
    "flash_driver/clear.sh"
    "eth_driver/build.sh"
    "eth_driver/clear.sh"
    "ble_driver/build.sh"
    "ble_driver/clear.sh"
)

ALL_EXIST=true
for script in "${SCRIPTS[@]}"; do
    if [ -f "$script" ]; then
        echo "✅ $script - 存在"
        # 检查文件权限
        if [ -x "$script" ]; then
            echo "   ✅ 可执行权限已设置"
        else
            echo "   ⚠️  缺少可执行权限"
            chmod +x "$script"
            echo "   ✅ 已添加可执行权限"
        fi
    else
        echo "❌ $script - 不存在"
        ALL_EXIST=false
    fi
done

if [ "$ALL_EXIST" = false ]; then
    echo ""
    echo "错误: 部分构建脚本不存在!"
    exit 1
fi

echo ""
echo "2. 检查构建脚本语法..."
echo "----------------------------------------"

ALL_SYNTAX_OK=true
for script in "${SCRIPTS[@]}"; do
    if bash -n "$script"; then
        echo "✅ $script - 语法正确"
    else
        echo "❌ $script - 语法错误"
        ALL_SYNTAX_OK=false
    fi
done

if [ "$ALL_SYNTAX_OK" = false ]; then
    echo ""
    echo "错误: 部分构建脚本语法错误!"
    exit 1
fi

echo ""
echo "3. 检查构建脚本内容..."
echo "----------------------------------------"

# 检查关键配置
echo "检查UART驱动脚本配置:"
grep -n "BOARD.*stm32f4_disco" uart_driver/build.sh || echo "⚠️  未找到stm32f4_disco开发板配置"
grep -n "APP.*echo_bot" uart_driver/build.sh || echo "⚠️  未找到echo_bot应用配置"

echo ""
echo "检查Flash驱动脚本配置:"
grep -n "BOARD.*stm32f4_disco" flash_driver/build.sh || echo "⚠️  未找到stm32f4_disco开发板配置"
grep -n "APP.*flash_shell" flash_driver/build.sh || echo "⚠️  未找到flash_shell应用配置"

echo ""
echo "检查以太网驱动脚本配置:"
grep -n "BOARD.*stm32f7_disco" eth_driver/build.sh || echo "⚠️  未找到stm32f7_disco开发板配置"
grep -n "APP.*ethernet" eth_driver/build.sh || echo "⚠️  未找到ethernet应用配置"

echo ""
echo "检查BLE驱动脚本配置:"
grep -n "BOARD.*stm32wb55rg_nucleo" ble_driver/build.sh || echo "⚠️  未找到stm32wb55rg_nucleo开发板配置"
grep -n "APP.*peripheral" ble_driver/build.sh || echo "⚠️  未找到peripheral应用配置"

echo ""
echo "4. 显示构建脚本摘要..."
echo "----------------------------------------"

for script in "${SCRIPTS[@]}"; do
    echo ""
    echo "脚本: $script"
    echo "文件大小: $(du -h "$script" | cut -f1)"
    echo "行数: $(wc -l < "$script")"
    echo "关键功能:"
    
    case "$script" in
        *uart/build*)
            echo "  - STM32F4 Discovery开发板"
            echo "  - UART驱动示例 (echo_bot)"
            echo "  - Zephyr构建系统"
            echo "  - 自动环境检测"
            ;;
        *uart/clear*)
            echo "  - 清理构建目录和中间文件"
            echo "  - 删除ELF/二进制文件"
            echo "  - 准备重新构建"
            ;;
        *flash/build*)
            echo "  - STM32F4 Discovery开发板"
            echo "  - Flash驱动示例 (flash_shell)"
            echo "  - Zephyr构建系统"
            echo "  - 自动环境检测"
            ;;
        *flash/clear*)
            echo "  - 清理构建目录和中间文件"
            echo "  - 删除ELF/二进制文件"
            echo "  - 准备重新构建"
            ;;
        *eth/build*)
            echo "  - STM32F7 Discovery开发板"
            echo "  - Ethernet驱动示例"
            echo "  - Zephyr构建系统"
            echo "  - 自动环境检测"
            ;;
        *eth/clear*)
            echo "  - 清理构建目录和中间文件"
            echo "  - 删除ELF/二进制文件"
            echo "  - 准备重新构建"
            ;;
        *ble/build*)
            echo "  - STM32WB55RG Nucleo开发板"
            echo "  - BLE驱动示例 (peripheral)"
            echo "  - Zephyr构建系统"
            echo "  - 自动环境检测"
            ;;
        *ble/clear*)
            echo "  - 清理构建目录和中间文件"
            echo "  - 删除ELF/二进制文件"
            echo "  - 准备重新构建"
            ;;
    esac
done

echo ""
echo "========================================"
echo "测试完成!"
echo "========================================"
echo ""
echo "下一步:"
echo "1. 确保Zephyr环境已正确安装 (/root/zephyr)"
echo "2. 设置ZEPHYR_BASE环境变量"
echo "3. 运行构建脚本:"
echo "   cd testcases/uart_driver && ./build.sh"
echo "   cd testcases/flash_driver && ./build.sh"
echo "   cd testcases/eth_driver && ./build.sh"
echo "   cd testcases/ble_driver && ./build.sh"
echo "4. 运行清理脚本:"
echo "   cd testcases/uart_driver && ./clear.sh"
echo "   cd testcases/flash_driver && ./clear.sh"
echo "   cd testcases/eth_driver && ./clear.sh"
echo "   cd testcases/ble_driver && ./clear.sh"
echo ""
echo "注意: 这些脚本需要Zephyr SDK和west工具才能实际构建。"
echo "========================================"
