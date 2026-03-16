import os
import pygame

# Используем нормализацию, чтобы пробелы и скобки не ломали путь
filename = os.path.normpath("Bobby Byrd - Hot Pants [Bonus Beat] (Drum Break - Loop).mp3")

if os.path.exists(filename):
    print(f"✅ Вижу файл: {filename}")
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    print("🎶 Музыка играет! Нажми Enter, чтобы остановить.")
    input()
else:
    print("❌ Файл всё еще не в папке проекта. Перетяни его в VS Code!")
    
    # В файле logic.py
def extract_info(self):
    try:
        audio = ID3(self.file_path)
        # ... твой код ...
    except Exception as e:
        print(f"⚠️ Не удалось прочитать метаданные {self.title}: {e}")