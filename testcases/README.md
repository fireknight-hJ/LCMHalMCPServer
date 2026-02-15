# 测试用例使用指南

本目录存放测试用例脚本信息，用于测试LCMHAL生成器的功能。

## 测试用例目录结构

```
testcases/
├── freertos_streamserver/       # FreeRTOS流服务器测试用例
├── macbook/                     # MacBook平台测试用例
│   ├── freertos_bleheartrate/   # FreeRTOS BLE心率测试用例
│   ├── freertos_streamserver/   # FreeRTOS流服务器测试用例
│   ├── freertos_uart/           # FreeRTOS UART测试用例
│   ├── nxp_bm_httpsrv/          # NXP BM HTTP服务器测试用例
│   ├── nxp_bm_uart_dma/         # NXP BM UART DMA测试用例
│   ├── nxp_freertos_httpsrv/    # NXP FreeRTOS HTTP服务器测试用例
│   ├── nxp_freertos_uart/       # NXP FreeRTOS UART测试用例
│   ├── rt-thread/               # RT-Thread测试用例
│   │   ├── file/                # RT-Thread文件系统测试用例
│   │   ├── libc/                # RT-Thread libc测试用例
│   │   ├── network/             # RT-Thread网络测试用例
│   │   ├── pm/                  # RT-Thread电源管理测试用例
│   │   ├── rt-link/             # RT-Thread rt-link测试用例
│   │   ├── test/                # RT-Thread测试测试用例
│   │   ├── ulog/                # RT-Thread日志测试用例
│   │   ├── var_export/          # RT-Thread变量导出测试用例
│   │   └── ymodem/              # RT-Thread ymodem测试用例
│   ├── rtthread_libc/           # RT-Thread libc测试用例
│   ├── zephyr_stm32eth/         # Zephyr STM32以太网测试用例
│   └── zephyr_stm32uart/        # Zephyr STM32 UART测试用例
├── README.md                    # 本说明文件
└── run_all_demos.py             # 运行所有测试用例的脚本
```

## 新建测试用例的步骤

### 1. 创建目录结构

在`testcases/macbook/`目录下创建一个新的测试用例目录，例如`my_new_demo`：

```bash
mkdir -p testcases/macbook/my_new_demo
```

### 2. 编写 lcmhal_config.yml 配置文件

在新创建的目录中创建`lcmhal_config.yml`文件，配置以下内容：

```yaml
# LCMHAL配置文件
script_path: "/Users/jie/Documents/workspace/lcmhalgen/LCMHalMCPServer/testcases/macbook/my_new_demo"
db_path: "/Users/jie/Documents/workspace/lcmhalgen/LCMHalTest_DBS/DATABASE_MyNewDemo"
src_path: "/Users/jie/Documents/workspace/lcmhalgen/[OS]/examples/my_new_demo"
proj_path: "/Users/jie/Documents/workspace/lcmhalgen/[OS]/bsp/[board]"
```

其中：
- `script_path`：测试用例脚本路径，指向新创建的目录
- `db_path`：数据库路径，用于存储分析结果
- `src_path`：源代码路径，指向示例代码所在目录
- `proj_path`：项目路径，指向BSP板级支持包目录

### 3. 编写 build.sh 构建脚本

在新创建的目录中创建`build.sh`文件，用于编译项目：

```bash
#!/bin/bash

# 测试用例构建脚本
# 用于编译指定平台的测试项目

# 设置项目构建目录路径
PWDDIR=/Users/jie/Documents/workspace/lcmhalgen/[OS]/bsp/[board]
# 获取当前shell脚本所在目录
SCRIPTDIR=/Users/jie/Documents/workspace/lcmhalgen/LCMHalMCPServer/testcases/macbook/my_new_demo

# 检查目录是否存在
if [ ! -d "$PWDDIR" ]; then
    echo "错误: 构建目录不存在: $PWDDIR"
    exit 1
fi

# 切换工作目录到项目所在目录
echo "切换到构建目录: $PWDDIR"
cd "$PWDDIR" || {
    echo "错误: 无法切换到目录 $PWDDIR"
    exit 1
}

# 编译项目
echo "开始编译项目..."
scons -j8

# 检查编译结果
if [ $? -eq 0 ]; then
    echo "编译成功完成!"
    # 移动生成的可执行文件到脚本目录
    if [ ! -d "$SCRIPTDIR" ]; then
        mkdir -p "$SCRIPTDIR"
    fi
    # 移动可执行文件到脚本目录
    mv -f "[output_file].elf" "$SCRIPTDIR/output.elf" || {
        echo "错误: 无法移动可执行文件到 $SCRIPTDIR/output.elf"
        exit 1
    }
else
    echo "编译失败!"
    exit 1
fi
```

### 4. 编写 clear.sh 清理脚本

在新创建的目录中创建`clear.sh`文件，用于清理构建缓存：

```bash
#!/bin/bash

# 测试用例清理脚本
# 用于删除构建缓存和生成的文件

# 设置项目构建目录路径
PWDDIR=/Users/jie/Documents/workspace/lcmhalgen/[OS]/bsp/[board]
# 获取当前shell脚本所在目录
SCRIPTDIR=/Users/jie/Documents/workspace/lcmhalgen/LCMHalMCPServer/testcases/macbook/my_new_demo

# 清理构建缓存
if [ -d "$PWDDIR" ]; then
    echo "清理构建缓存..."
    cd "$PWDDIR" || {
        echo "错误: 无法切换到目录 $PWDDIR"
        exit 1
    }
    scons -c
fi

# 清理生成的文件
if [ -f "$SCRIPTDIR/output.elf" ]; then
    echo "清理生成的可执行文件..."
    rm -f "$SCRIPTDIR/output.elf"
fi

echo "清理完成!"
```

### 5. 测试运行

给脚本添加执行权限：

```bash
chmod +x testcases/macbook/my_new_demo/build.sh testcases/macbook/my_new_demo/clear.sh
```

运行构建脚本：

```bash
cd testcases/macbook/my_new_demo
./build.sh
```

## 运行所有测试用例的方法

使用`run_all_demos.py`脚本可以运行所有测试用例：

```bash
python3 -m testcases.run_all_demos
```

该脚本会：
1. 自动发现所有测试用例
2. 并行运行测试用例（最多3个同时运行）
3. 将每个测试用例的输出重定向到`testcases_out`目录
4. 生成测试结果摘要

## 测试用例构建文件说明

### build.sh
- 构建脚本，用于编译项目并生成可执行文件
- 编译成功后，会将生成的可执行文件移动到测试用例目录

### clear.sh
- 清理脚本，用于删除构建缓存和生成的文件
- 可以通过运行此脚本清理测试环境

## 常见问题与解决方案

### 1. 构建失败

**症状**：运行`build.sh`时出现错误

**解决方案**：
- 检查`PWDDIR`和`SCRIPTDIR`路径是否正确
- 检查源代码是否存在且完整
- 检查编译工具链是否正确安装

### 2. 可执行文件移动失败

**症状**：编译成功但无法移动可执行文件

**解决方案**：
- 检查`SCRIPTDIR`目录是否存在
- 检查权限是否足够
- 检查目标文件名是否正确

### 3. 测试用例未被发现

**症状**：运行`run_all_demos.py`时未发现新创建的测试用例

**解决方案**：
- 确保测试用例目录结构正确
- 确保`lcmhal_config.yml`文件存在且格式正确
- 确保构建脚本和清理脚本存在且可执行

## 注意事项

1. 所有路径配置必须使用绝对路径
2. 确保测试用例目录有足够的权限
3. 编译前确保源代码和依赖项已正确安装
4. 运行测试用例前确保已安装必要的工具链

---

通过以上步骤，您可以成功创建和运行新的测试用例，验证LCMHAL生成器的功能。
