#!/bin/bash
echo "🔄 Terminal Cleaner güncelleniyor..."
cd ~/terminal-cleaner || exit
git pull origin main
chmod +x setup_cleaner.sh
echo "✅ Güncelleme tamamlandı!"
