import os, shutil, tempfile
from colorama import Fore, Style, init

init(autoreset=True)

def clear_temp():
    temp_dir = tempfile.gettempdir()
    print(Fore.CYAN + f"🧹 Geçici dosyalar temizleniyor: {temp_dir}")
    for item in os.listdir(temp_dir):
        item_path = os.path.join(temp_dir, item)
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
        except: pass
    print(Fore.GREEN + "✅ Geçici dosyalar temizlendi!")

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
    print(Fore.GREEN + "✅ Önbellek temizliği tamamlandı!")

def system_info():
    import platform, shutil
    print(Fore.MAGENTA + "🖥️ Sistem Bilgileri:")
    print(f"İşletim Sistemi: {platform.system()} {platform.release()}")
    print(f"Platform: {platform.platform()}")
    total, used, free = shutil.disk_usage("/")
    print(Fore.YELLOW + f"Disk Kullanımı - Toplam: {total // (2**30)} GB, Kullanılan: {used // (2**30)} GB, Boş: {free // (2**30)} GB")

def menu():
    while True:
        print(Fore.BLUE + "\n📋 Menü")
        print("1️⃣ Hızlı Temizlik")
        print("2️⃣ Full Temizlik")
        print("3️⃣ Sistem Bilgisi")
        print("4️⃣ Çıkış")
        choice = input("Seçiminiz: ")
        if choice == "1":
            clear_temp()
            clear_cache()
        elif choice == "2":
            clear_temp()
            clear_cache()
        elif choice == "3":
            system_info()
        elif choice == "4":
            break
        else:
            print(Fore.RED + "⚠️ Geçersiz seçim!")

if __name__ == "__main__":
    menu()
