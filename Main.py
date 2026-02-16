import customtkinter as ctk
import pygame
from tkinter import filedialog
from PIL import Image
import os
from logic import get_songs_from_folder

class MusicPlayer(ctk.CTk):
    # Добавляем skin_name в параметры, чтобы можно было менять скины
    def __init__(self, fg_color="#2B2B2B", skin_name="classic", **kwargs):
        super().__init__(fg_color=fg_color, **kwargs)

        # Теперь skin_name определен [cite: 05-02-26]
        self.skin_path = f"assets/{skin_name}/" 

        self.title("DanMus")
        self.geometry("680x800")

        self.playlist = []
        self.current_index = 0 # Убрал нижнее подчеркивание для простоты
        pygame.mixer.init()

        # Запуск создания интерфейса
        self.setup_ui()

    def setup_ui(self):
        """Метод для создания кнопок и надписей [cite: 05-02-26]"""
        self.label = ctk.CTkLabel(self, text="Плеер DanMus готов!", font=("Arial", 20))
        self.label.pack(pady=40)
        
        # Кнопка для теста
        self.btn_open = ctk.CTkButton(self, text="Открыть папку", command=self.open_folder)
        self.btn_open.pack(pady=10)

    def open_folder(self):
        # Открываем окно выбора папки
        folder = filedialog.askdirectory()
    
        if folder:
            # Используем твою функцию из logic.py!
            self.playlist = get_songs_from_folder(folder)
        
            # Выведем в консоль список, чтобы проверить, что всё нашлось
            print(f"Найдено песен: {len(self.playlist)}")
            for track in self.playlist:
                print(f"Трек: {track.title} - {track.artist}")

# само приложение и запускаем цикл 
if __name__ == "__main__":
    app = MusicPlayer(skin_name="classic") # Создаем объект 
    app.mainloop() # Запускаем бесконечный цикл окна 