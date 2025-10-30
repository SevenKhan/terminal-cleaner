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
        print("✅ Temizlik tamamlandı!")
    except Exception as e:
        print(f"Hata: {e}")

def sys_info():
    print("\n🖥️ Sistem Bilgileri:")
    print(f"İşletim Sistemi: {platform.system()} {platform.release()}")
    print(f"Platform: {platform.platform()}")
    print(f"Python Versiyonu: {platform.python_version()}")

if __name__ == "__main__":
    print("""
    ============ TERMINAL CLEANER ============
    1. Geçici dosyaları temizle
    2. Sistem bilgilerini göster
    3. Çıkış
    ==========================================
    """)
    
    while True:
        choice = input("Bir seçenek gir (1-3): ")
        if choice == "1":
            clear_temp()
        elif choice == "2":
            sys_info()
        elif choice == "3":
            print("👋 Görüşürüz dostum!")
            break
        else:
            print("Geçersiz seçim!")
