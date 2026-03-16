import os
from mutagen.id3 import ID3

class Track:
    #"Класс для хранения данных об одной песне"
    def __init__(self, file_path):
        self.file_path = file_path
        self.title = os.path.basename(file_path) #имя файла по умолчанию
        self.artist = "Unknown Artist"
        self.cover_data = None
        self.extract_info()
        self.update_progress()

    def extract_info(self):
        #метод проверки метадщанных
        try:
            audio = ID3(self.file_path)
            
            # Названия тегов
            if 'TIT2' in audio:
                self.title = audio['TIT2'].text[0]  # Вот этот отступ важен!
            
            if 'TPE1' in audio:
                self.artist = audio['TPE1'].text[0] # И здесь тоже
            
            # Ищем обложку
            for tag in audio.values():
                if tag.getID() == 'APIC':
                    self.cover_data = tag.data # Двойной отступ (внутри for и внутри if)
                    break
        except:
            pass
        
        def update_progresss(self):
            if self.is_playing and pygame.mixer.music.get_busy():
                # получаем текущее время в секундах
                current_time = pygame.mixer.music.get_pos()/ 1000
                # Здесь можно добавить логику пересчета в проценты, 
                # если знать общую длину трека через mutagen
                self.progress_bar.set(current_time)
                
            self.after(1000, self.update_progress)
            

def get_songs_from_folder(folder_path):
    songs = []
    if os.path.exists(folder_path):
        for file in os.listdir(folder_path):
            # 1. Приводим всё к нижнему регистру (.MP3 -> .mp3)
            # 2. Убираем скрытые файлы (например, начинающиеся с ._)
            if file.lower().endswith(".mp3") and not file.startswith("._"):
                full_path = os.path.normpath(os.path.join(folder_path, file))
                try:
                    songs.append(Track(full_path))
                except Exception as e:
                    print(f"Не удалось загрузить {file}: {e}")
    return songs








