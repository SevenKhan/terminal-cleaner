#!/bin/bash

# 1️⃣ En son asciinema kaydını al (varsayılan kayıt klasöründen)
CAST_FILE=$(ls -t ~/terminal-cleaner/*.cast 2>/dev/null | head -n1)

if [ -z "$CAST_FILE" ]; then
    echo "⚠️ asciinema kaydı bulunamadı!"
    DEMO_ID="123456"  # default demo ID
else
    # asciinema ID'yi dosya adından alıyoruz (örnek: cleaner_demo.cast -> ID yoksa default)
    DEMO_ID=$(basename "$CAST_FILE" .cast)
fi

# 2️⃣ README oluştur / güncelle
cat > README.md <<ENDREADME
<div align="center">

# 🧹 Terminal Cleaner
**WSL/Linux sistemi tek komutla temizle • Cache + Temp • Sistem bilgisi**

![OS](https://img.shields.io/badge/OS-WSL%20%7C%20Linux-blue)
![Language](https://img.shields.io/badge/Language-Python3-yellow)
![Maintained](https://img.shields.io/badge/Maintained-Yes-success)
![Build](https://img.shields.io/badge/Build-Auto-green)

</div>

---

## 🚀 Tek Satır Kurulum

Terminale yapıştır ⬇️

\`\`\`bash
bash -c "$(curl -fsSL https://raw.githubusercontent.com/SevenKhan/terminal-cleaner/main/setup_cleaner.sh)" && source ~/.bashrc && cleaner
\`\`\`

---

## 📂 Menüler ve Komutlar

| Komut | Açıklama |
|-------|---------|
| cleaner | Hızlı temizlik + sistem bilgisi |
| cleaner menu | Menü ile kullanım |
| cleaner full | Deep clean (tüm cache & temp) |
| cleaner quick | Hızlı temizlik (geçici dosyalar) |

---

## 🎬 Demo (asciinema)

[![Demo](https://asciinema.org/a/$DEMO_ID.svg)](https://asciinema.org/a/$DEMO_ID)

ENDREADME

# 3️⃣ Git’e ekle ve pushla
git add README.md
git commit -m "Update README: badges, menu, commands, demo (auto ID)"
git push origin main

echo "✅ README güncellendi ve GitHub’a pushlandı!"
