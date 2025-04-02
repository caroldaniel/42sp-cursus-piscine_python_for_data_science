#!/bin/bash

set -e  # Exit on any error

# --- Styling Helpers ---
RED='\033[1;31m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
BLUE='\033[1;34m'
BOLD='\033[1m'
RESET='\033[0m'

VENV_NAME="venv"
PYTHON_VERSION="python3.10"

echo -e -e "${BLUE}🔍 Checking if ${PYTHON_VERSION} is installed...${RESET}"
if ! command -v $PYTHON_VERSION &> /dev/null; then
    echo -e "${RED}❌ ${PYTHON_VERSION} not found. Installing...${RESET}"
    echo -e -n "   🔧 Installing packages..."
    sudo apt update > /dev/null 2>&1
    sudo apt install software-properties-common -y > /dev/null 2>&1
    sudo add-apt-repository ppa:deadsnakes/ppa -y > /dev/null 2>&1
    sudo apt update > /dev/null 2>&1
    sudo apt install $PYTHON_VERSION $PYTHON_VERSION-venv $PYTHON_VERSION-dev -y > /dev/null 2>&1
    echo -e " ${GREEN}done${RESET}"
else
    echo -e "${GREEN}✅ ${PYTHON_VERSION} is already installed.${RESET}"
    echo -e -n "   📦 Checking venv/dev packages..."
    sudo apt install $PYTHON_VERSION-venv $PYTHON_VERSION-dev -y > /dev/null 2>&1
    echo -e " ${GREEN}ok${RESET}"
fi

echo -e -n "${BLUE}📁 Creating virtual environment...${RESET}"
$PYTHON_VERSION -m venv $VENV_NAME > /dev/null 2>&1
echo -e " ${GREEN}done${RESET}"

echo -e -n "${BLUE}⬆️  Upgrading pip...${RESET}"
source $VENV_NAME/bin/activate
pip install --upgrade pip > /dev/null 2>&1
deactivate
echo -e " ${GREEN}done${RESET}"

if [ -f "requirements.txt" ]; then
    echo -e -n "${BLUE}📦 Installing dependencies...${RESET}"
    source $VENV_NAME/bin/activate
    pip install -r requirements.txt > /dev/null 2>&1
    deactivate
    echo -e " ${GREEN}done${RESET}"
else
    echo -e "${YELLOW}⚠️  requirements.txt not found. Skipping dependency installation.${RESET}"
fi

echo -e ""
echo -e "${GREEN}${BOLD}🎉 Environment setup complete!${RESET}"
echo -e ""
echo -e "${BOLD}${YELLOW}🔔 To activate the virtual environment, run:${RESET}"
echo -e ""
echo -e "    ${BOLD}source $VENV_NAME/bin/activate${RESET}"
echo -e ""
echo -e "${YELLOW}💡 Run this in your current shell to start using Python 3.10 + dependencies.${RESET}"
