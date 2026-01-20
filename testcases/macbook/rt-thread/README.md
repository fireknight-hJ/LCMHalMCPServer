# RT-Thread Examples Build Configuration

This directory contains build scripts and configuration files for RT-Thread examples.

## Directory Structure

```
examples-builds/
├── libc/              # libc example
│   ├── build.sh       # Build script
│   ├── clear.sh       # Clear script
│   ├── lcmhal_config.yml  # Configuration file
│   └── emulate/       # Output directory
└── README.md          # This file
```

## Usage

### 1. Build Script (build.sh)

The build script is responsible for:
- Building the project and generating the ELF file
- Moving the generated ELF file to the script's directory (renamed as output.elf)

To use it:
```bash
cd /Users/jie/Documents/workspace/lcmhalgen/rt-thread/examples-builds/libc
chmod +x build.sh
./build.sh
```

### 2. Clear Script (clear.sh)

The clear script deletes build cache, including compiled ELF, object files, etc.

To use it:
```bash
cd /Users/jie/Documents/workspace/lcmhalgen/rt-thread/examples-builds/libc
chmod +x clear.sh
./clear.sh
```

### 3. Configuration File (lcmhal_config.yml)

Contains configuration items:
- script_path: Script path
- db_path: Database path
- src_path: Source code path
- proj_path: Project path

## Moving to Target Directory

Due to permission restrictions, you need to manually copy these files to the target directory:

```bash
mkdir -p /Users/jie/Documents/workspace/lcmhalgen/LCMHalMCPServer/testcases/macbook/rtthread_libc/emulate

cp /Users/jie/Documents/workspace/lcmhalgen/rt-thread/examples-builds/libc/build.sh /Users/jie/Documents/workspace/lcmhalgen/LCMHalMCPServer/testcases/macbook/rtthread_libc/
cp /Users/jie/Documents/workspace/lcmhalgen/rt-thread/examples-builds/libc/clear.sh /Users/jie/Documents/workspace/lcmhalgen/LCMHalMCPServer/testcases/macbook/rtthread_libc/
cp /Users/jie/Documents/workspace/lcmhalgen/rt-thread/examples-builds/libc/lcmhal_config.yml /Users/jie/Documents/workspace/lcmhalgen/LCMHalMCPServer/testcases/macbook/rtthread_libc/

chmod +x /Users/jie/Documents/workspace/lcmhalgen/LCMHalMCPServer/testcases/macbook/rtthread_libc/build.sh
chmod +x /Users/jie/Documents/workspace/lcmhalgen/LCMHalMCPServer/testcases/macbook/rtthread_libc/clear.sh
```

## Testing the Build Script

To test the build script:
```bash
cd /Users/jie/Documents/workspace/lcmhalgen/rt-thread/examples-builds/libc
./build.sh
```

This will build the RT-Thread hifive1 BSP and copy the resulting rtthread.elf to the emulate directory as output.elf.