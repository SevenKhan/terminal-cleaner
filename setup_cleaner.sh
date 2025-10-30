#!/bin/bash
echo "📦 Terminal Cleaner kuruluyor..."
# Python package kontrol
if ! command -v python3 &> /dev/null; then
    echo "Python3 bulunamadı. Lütfen kurun!"
    exit 1
fi
pip3 install --user colorama
echo "🧹 Kurulum tamamlandı!"
echo "🔗 Alias ekleniyor..."
echo "alias cleaner='python3 ~/terminal-cleaner/cleaner_menu.py'" >> ~/.bashrc
source ~/.bashrc
echo "✅ Artık terminalde 'cleaner' yazabilirsiniz!"
