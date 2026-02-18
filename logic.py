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

def get_songs_from_folder(folder_path):
    songs = []
    if os.path.exists(folder_path):
        for file in os.listdir(folder_path):
            if file.endswith(".mp3"):
                full_path = os.path.join(folder_path, file)
                songs.append(Track(full_path))
    return songs



self.is_playing - False




