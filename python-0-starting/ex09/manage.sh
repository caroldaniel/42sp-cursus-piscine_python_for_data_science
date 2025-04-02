#!/bin/bash

PACKAGE_NAME="ft_package"
LOG_FILE="install_error.log"
DIST_DIR="./dist"
TEST_SCRIPT="python3 test/test.py"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[1;34m'
NC='\033[0m'

clear_log() {
    rm -f "$LOG_FILE"
}

print_header() {
    echo -e "\n${BLUE}==> $1${NC}"
}

print_success() {
    echo -e "${GREEN}✔ $1${NC}"
}

print_failure() {
    echo -e "${RED}✘ $1${NC}"
    if [ -f "$LOG_FILE" ]; then
        echo -e "${YELLOW}--- Error log ---${NC}"
        cat "$LOG_FILE"
    fi
}

run_safe() {
    "$@" > /dev/null 2>>"$LOG_FILE"
    return $?
}

build_package() {
    print_header "Building the package"
    clear_log
    pip install -r requirements.txt > /dev/null 2>>"$LOG_FILE"
    rm -rf build dist "${PACKAGE_NAME}.egg-info"
    if run_safe python3 setup.py sdist bdist_wheel; then
        print_success "Build complete"
    else
        print_failure "Build failed"
    fi
}

install_package() {
    print_header "Installing the package"
    echo "Choose file type:"
    echo "1. .tar.gz"
    echo "2. .whl"
    read -rp "Type: " type

    FILE=""
    if [ "$type" == "1" ]; then
        FILE=$(find "$DIST_DIR" -name "${PACKAGE_NAME}-*.tar.gz" | head -n1)
    elif [ "$type" == "2" ]; then
        FILE=$(find "$DIST_DIR" -name "${PACKAGE_NAME}-*.whl" | head -n1)
    fi

    if [ -z "$FILE" ]; then
        print_failure "Package file not found. Build it first."
        return
    fi

    clear_log
    if run_safe pip install "$FILE"; then
        print_success "Installed $FILE"
    else
        print_failure "Installation failed"
    fi
}

run_tests() {
    print_header "Running test script"
    LOG_FILE="test_log.txt"
    echo -e "${YELLOW}--- Capturing output to $LOG_FILE ---${NC}"
    echo ">>> python3 $TEST_SCRIPT" > "$LOG_FILE"

    if python3 "$TEST_SCRIPT" 2>&1 | tee -a "$LOG_FILE"; then
        print_success "Tests passed"
    else
        print_failure "Tests failed"
        echo -e "${YELLOW}--- See full test log: $LOG_FILE ---${NC}"
    fi
}


uninstall_package() {
    print_header "Uninstalling $PACKAGE_NAME"
    clear_log
    if run_safe pip uninstall -y "$PACKAGE_NAME"; then
        print_success "Uninstalled $PACKAGE_NAME"
    else
        print_failure "Uninstallation failed"
    fi
}

clean_build() {
    print_header "Cleaning build artifacts"
    rm -rf build dist "${PACKAGE_NAME}.egg-info"
    print_success "Cleaned"
}

show_package_info() {
    print_header "Installed package info"
    pip show -v "$PACKAGE_NAME"
}

# Interactive menu
while true; do
    echo -e "\n${YELLOW}====== FT PACKAGE MANAGER ======${NC}"
    echo "1. Build package"
    echo "2. Install package"
    echo "3. Run tests"
    echo "4. Uninstall package"
    echo "5. Show package info"
    echo "6. Clean build files"
    echo "7. Exit"
    echo -en "${BLUE}Choose an option: ${NC}"
    read -r choice


    case $choice in
        1) build_package ;;
        2) install_package ;;
        3) run_tests ;;
        4) uninstall_package ;;
        5) show_package_info ;;
        6) clean_build ;;
        7) echo -e "${YELLOW}Exiting. Bye! 👋${NC}"; break ;;
        *) echo -e "${RED}Invalid option. Try again.${NC}" ;;
    esac
done
