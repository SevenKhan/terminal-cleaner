import os
import shutil
import tempfile
import platform

def clear_temp():
    temp_dir = tempfile.gettempdir()
    print(f"🧹 Geçici dosyalar temizleniyor: {temp_dir}")
    try:
        for item in os.listdir(temp_dir):
            item_path = os.path.join(temp_dir, item)
            try:
                if os.path.isfile(item_path) or os.path.islink(item_path):
                    os.unlink(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
            except Exception as e:
                print(f"⚠️ {item_path} silinemedi: {e}")
        print("✅ Geçici dosyalar temizlendi!")
    except Exception as e:
        print(f"Hata: {e}")

def clear_cache():
    cache_dirs = [
        os.path.expanduser("~/.cache"),
        os.path.expanduser("~/.mozilla/firefox"),
        os.path.expanduser("~/.npm"),
        os.path.expanduser("~/.local/share/Trash")
    ]
    print("🧹 Önbellek klasörleri temizleniyor...")
    for dir_path in cache_dirs:
        if os.path.exists(dir_path):
            try:
                shutil.rmtree(dir_path)
                print(f"✅ {dir_path} temizlendi")
            except Exception as e:
                print(f"⚠️ {dir_path} silinemedi: {e}")
        else:
            print(f"⚠️ {dir_path} bulunamadı")
    print("🎉 Önbellek temizliği tamamlandı!")

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

if __name__ == "__main__":
    print("""
    ============ TERMINAL CLEANER ============
    1. Geçici dosyaları temizle
    2. Sistem bilgilerini göster
    3. Disk kullanımını göster
    4. Önbellek temizle
    5. Çıkış
    ==========================================
    """)
    while True:
        choice = input("Bir seçenek gir (1-5): ")
        if choice == "1":
            clear_temp()
        elif choice == "2":
            sys_info()
        elif choice == "3":
            disk_usage()
        elif choice == "4":
            clear_cache()
        elif choice == "5":
            print("👋 Görüşürüz dostum!")
            break
        else:
            print("Geçersiz seçim!")
