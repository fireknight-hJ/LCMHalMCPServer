#!/bin/bash
# Build script for creating CodeQL database for Zephyr ETH driver test

set -e

# Configuration
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BUILD_DIR="${PROJECT_DIR}/build_codeql"
DB_DIR="${PROJECT_DIR}/codeql_db"
ZEPHYR_BASE="${ZEPHYR_BASE:-/home/chenkaiqiu/LCMHalMCPServer/zephyr_official}"

# Read board from lcmhal_config.yml if available
LCMHAL_CONFIG="${PROJECT_DIR}/lcmhal_config.yml"
if [ -f "${LCMHAL_CONFIG}" ]; then
    BOARD=$(grep -E "^board:" "${LCMHAL_CONFIG}" | awk '{print $2}' | tr -d '"' | tr -d "'")
    if [ -z "${BOARD}" ]; then
        BOARD="native_sim/native/64"
    fi
else
    BOARD="native_sim/native/64"
fi

echo "Building CodeQL database for Zephyr ETH driver test"
echo "Board: ${BOARD}"
echo "ZEPHYR_BASE: ${ZEPHYR_BASE}"
echo "Database output: ${DB_DIR}"

# Clean build directory if exists
if [ -d "${BUILD_DIR}" ]; then
    echo "Cleaning previous build directory..."
    rm -rf "${BUILD_DIR}"
fi

# Clean database directory if exists
if [ -d "${DB_DIR}" ]; then
    echo "Cleaning previous database directory..."
    rm -rf "${DB_DIR}"
fi

# Create directories
mkdir -p "${BUILD_DIR}"
mkdir -p "${DB_DIR}"

cd "${BUILD_DIR}"

# Create a simple build command for CodeQL
echo "Creating build command for CodeQL analysis..."

# Generate a simple CMake configuration command
BUILD_CMD_FILE="${BUILD_DIR}/build_cmd.sh"
cat > "${BUILD_CMD_FILE}" << 'EOF'
#!/bin/bash
set -e

# Set up Zephyr environment
export ZEPHYR_BASE="${ZEPHYR_BASE:-/home/chenkaiqiu/LCMHalMCPServer/zephyr_official}"
export ZEPHYR_MODULES="${ZEPHYR_MODULES:-/home/chenkaiqiu/LCMHalMCPServer/zephyr_official/modules}"
export ZEPHYR_SDK_INSTALL_DIR="${ZEPHYR_SDK_INSTALL_DIR:-/home/chenkaiqiu/zephyr-sdk-0.16.8}"

# Source Zephyr environment
if [ -f "${ZEPHYR_BASE}/zephyr-env.sh" ]; then
    source "${ZEPHYR_BASE}/zephyr-env.sh"
fi

# Configure the project
cmake -GNinja -DBOARD=native_sim/native/64 "${PROJECT_DIR}/src" 2>&1 | tee cmake.log

# Build the project (just enough for CodeQL to analyze)
ninja 2>&1 | tee build.log
EOF

chmod +x "${BUILD_CMD_FILE}"

# Create CodeQL database
echo "Creating CodeQL database..."
codeql database create "${DB_DIR}" \
    --language=cpp \
    --source-root="${PROJECT_DIR}" \
    --command="bash ${BUILD_CMD_FILE}" \
    --overwrite

if [ $? -eq 0 ]; then
    echo "CodeQL database created successfully at: ${DB_DIR}"
    echo "Database contents:"
    ls -la "${DB_DIR}/"
    
    # Copy the database configuration to match UART test structure
    if [ -f "${DB_DIR}/codeql-database.yml" ]; then
        echo "Database configuration:"
        cat "${DB_DIR}/codeql-database.yml"
    fi
else
    echo "Failed to create CodeQL database"
    exit 1
fi

echo "CodeQL database creation completed successfully"
