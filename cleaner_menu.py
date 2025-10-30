import os, shutil, tempfile, platform

# Renkler
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

def clear_temp():
    temp_dir = tempfile.gettempdir()
    print(f"{CYAN}🧹 Geçici dosyalar temizleniyor: {temp_dir}{RESET}")
    for item in os.listdir(temp_dir):
        item_path = os.path.join(temp_dir, item)
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
        except: pass
    print(f"{GREEN}✅ Geçici dosyalar temizlendi!{RESET}")

def clear_cache():
    cache_dirs = [
        os.path.expanduser("~/.cache"),
        os.path.expanduser("~/.mozilla/firefox"),
        os.path.expanduser("~/.npm"),
        os.path.expanduser("~/.local/share/Trash")
    ]
    print(f"{CYAN}🧹 Önbellek temizleniyor...{RESET}")
    for dir_path in cache_dirs:
        if os.path.exists(dir_path):
            try: shutil.rmtree(dir_path)
            except: pass
    print(f"{GREEN}✅ Önbellek temizliği tamamlandı!{RESET}")

def sys_info():
    print(f"{YELLOW}\n🖥️ Sistem Bilgileri:{RESET}")
    print(f"İşletim Sistemi: {platform.system()} {platform.release()}")
    print(f"Platform: {platform.platform()}")
    print(f"Python Versiyonu: {platform.python_version()}")

def disk_usage():
    total, used, free = shutil.disk_usage("/")
    print(f"{YELLOW}\n💾 Disk Kullanımı:{RESET}")
    print(f"Toplam: {total // (2**30)} GB")
    print(f"Kullanılan: {used // (2**30)} GB")
    print(f"Boş: {free // (2**30)} GB")

# Menü
while True:
    print(f"""{CYAN}
================= TERMINAL CLEANER =================
1. Geçici dosyaları temizle
2. Önbelleği temizle
3. Sistem bilgilerini göster
4. Disk kullanımını göster
5. Çıkış
====================================================
{RESET}""")
    choice = input("Bir seçenek gir (1-5): ")
    if choice == "1":
        clear_temp()
    elif choice == "2":
        clear_cache()
    elif choice == "3":
        sys_info()
    elif choice == "4":
        disk_usage()
    elif choice == "5":
        print(f"{CYAN}👋 Görüşürüz dostum!{RESET}")
        break
    else:
        print(f"{RED}⚠️ Geçersiz seçim!{RESET}")
