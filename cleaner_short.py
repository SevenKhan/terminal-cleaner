import os, shutil, tempfile

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

clear_temp()
clear_cache()
