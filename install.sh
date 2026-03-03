#!/bin/bash
# install.sh - setup environment SpeedHubX

echo "[*] Setup environment SpeedHubX..."

# Pastikan Python & pip ada
pkg install python git -y 2>/dev/null || echo "Gunakan apt jika bukan Termux"

# Jalankan downloader di folder tools
bash tools/download_tools.sh

# Install package dari folder tools
pip install tools/requests-2.31.0-py3-none-any.whl
pip install tools/pyfiglet-0.8.post1-py3-none-any.whl

echo "[*] Semua package-tools terpasang. Jalankan: python generator.py"