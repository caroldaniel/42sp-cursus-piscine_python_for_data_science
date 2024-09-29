#!/bin/bash

# Define color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No color

# Function to print status with colors
print_status() {
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}$1 succeeded.${NC}"
    else
        echo -e "${RED}$1 failed.${NC}"
        exit 1
    fi
}

# Delete the previous build
echo -e "${YELLOW}Cleaning previous build...${NC}"
rm -rf build dist ft_package.egg-info > /dev/null 2>&1
print_status "Cleaning"

# Uninstall the package (if installed)
echo -e "${YELLOW}Uninstalling existing ft_package...${NC}"
pip uninstall -y ft_package > /dev/null 2>&1
print_status "Uninstallation"

# Build the package
echo -e "${YELLOW}Building the package...${NC}"
python3 setup.py sdist bdist_wheel > /dev/null 2>&1
print_status "Build"

# Install the package
echo -e "${YELLOW}Installing the package...${NC}"
pip install ./dist/ft_package-0.0.1.tar.gz > /dev/null 2>&1
print_status "Installation"

# Show the installed package
echo -e "${YELLOW}Displaying installed package info...${NC}"
pip show -v ft_package > /dev/null 2>&1
print_status "Show package"

# Test the package
echo -e "${YELLOW}Running tests...${NC}"
python3 test/test.py

# Delete the package and test again
echo -e "${YELLOW}Uninstalling the package...${NC}"
pip uninstall -y ft_package > /dev/null 2>&1
print_status "Uninstallation"

echo -e "${YELLOW}Running tests again...${NC}"
python3 test/test.py
