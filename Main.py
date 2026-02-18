import customtkinter as ctk
import pygame
from tkinter import filedialog
from PIL import Image
import os
from logic import get_songs_from_folder

class MusicPlayer(ctk.CTk):
    def __init__(self, fg_color="#2B2B2B", skin_name="classic", **kwargs):
        super().__init__(fg_color=fg_color, **kwargs)

        self.skin_path = f"assets/{skin_name}/" 
        self.title("DanMus")
        self.geometry("680x800")

        self.playlist = []
        self.current_index = 0 
        self.is_playing = False # Состояние плеера
        
        pygame.mixer.init()
        self.setup_ui()

    def setup_ui(self):
        """Создание интерфейса"""
        self.label = ctk.CTkLabel(self, text="Плеер DanMus готов!", font=("Arial", 20))
        self.label.pack(pady=40)
        
        self.btn_open = ctk.CTkButton(self, text="Открыть папку", command=self.open_folder)
        self.btn_open.pack(pady=10)

        # Кнопка Play/Pause
        self.btn_play = ctk.CTkButton(self, text="Play", command=self.toggle_playback)
        self.btn_play.pack(pady=10)

    def open_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.playlist = get_songs_from_folder(folder)
            print(f"Найдено песен: {len(self.playlist)}")
            self.current_index = 0
            self.is_playing = False
            self.btn_play.configure(text="Play")
            
            # Показываем список в консоли для проверки
            for track in self.playlist:
                print(f"Трек: {track.title} - {track.artist}")

    def toggle_playback(self):
        """Метод переключения проигрывания"""
        if not self.playlist:
            print("Playlist is empty!") 
            return
        
        if not self.is_playing:
            if not pygame.mixer.music.get_busy():
                track = self.playlist[self.current_index]
                pygame.mixer.music.load(track.file_path)
                pygame.mixer.music.play()
                self.label.configure(text=f"Играет: {track.title}")
            else:
                pygame.mixer.music.unpause()

            self.is_playing = True
            self.btn_play.configure(text="Pause") 
        else:
            pygame.mixer.music.pause()
            self.is_playing = False
            self.btn_play.configure(text="Play")

if __name__ == "__main__":
    app = MusicPlayer(skin_name="classic")
    app.mainloop()