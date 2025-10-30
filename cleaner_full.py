import os, shutil, tempfile, platform

def clear_temp():
    temp_dir = tempfile.gettempdir()
    for item in os.listdir(temp_dir):
        item_path = os.path.join(temp_dir, item)
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
        except: pass
    print("✅ Geçici dosyalar temizlendi!")

def clear_cache():
    cache_dirs = [
        os.path.expanduser("~/.cache"),
        os.path.expanduser("~/.mozilla/firefox"),
        os.path.expanduser("~/.npm"),
        os.path.expanduser("~/.local/share/Trash")
    ]
    for dir_path in cache_dirs:
        if os.path.exists(dir_path):
            try: shutil.rmtree(dir_path)
            except: pass
    print("✅ Önbellek temizliği tamamlandı!")

def sys_info():
    print("\n🖥️ Sistem Bilgileri:")
    print(f"İşletim Sistemi: {platform.system()} {platform.release()}")
    print(f"Platform: {platform.platform()}")
    print(f"Python Versiyonu: {platform.python_version()}")

def disk_usage():
    total, used, free = shutil.disk_usage("/")
    print("\n💾 Disk Kullanımı:")
    print(f"Toplam: {total // (2**30)} GB")
    print(f"Kullanılan: {used // (2**30)} GB")
    print(f"Boş: {free // (2**30)} GB")

# Çalıştır
clear_temp()
clear_cache()
sys_info()
disk_usage()
