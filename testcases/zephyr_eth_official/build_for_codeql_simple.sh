#!/bin/bash
# Simple build script for creating CodeQL database for Zephyr ETH driver test

set -e

# Configuration
PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DB_DIR="${PROJECT_DIR}/codeql_db"

echo "Building CodeQL database for Zephyr ETH driver test"
echo "Project directory: ${PROJECT_DIR}"
echo "Database output: ${DB_DIR}"

# Clean database directory if exists
if [ -d "${DB_DIR}" ]; then
    echo "Cleaning previous database directory..."
    rm -rf "${DB_DIR}"
fi

# Create CodeQL database using the existing build.sh script
echo "Creating CodeQL database..."
codeql database create "${DB_DIR}" \
    --language=cpp \
    --source-root="${PROJECT_DIR}" \
    --command="bash build.sh" \
    --overwrite

if [ $? -eq 0 ]; then
    echo "CodeQL database created successfully at: ${DB_DIR}"
    echo "Database contents:"
    ls -la "${DB_DIR}/"
    
    # Show database configuration
    if [ -f "${DB_DIR}/codeql-database.yml" ]; then
        echo "Database configuration:"
        cat "${DB_DIR}/codeql-database.yml"
    fi
    
    # Create lcmhal_tmp directory for analysis results
    mkdir -p "${DB_DIR}/lcmhal_tmp"
    echo "Created lcmhal_tmp directory for analysis results"
else
    echo "Failed to create CodeQL database"
    exit 1
fi

echo "CodeQL database creation completed successfully"
