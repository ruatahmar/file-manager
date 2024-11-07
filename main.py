import os 
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


downloads_dir=r"C:\Users\VICTUS\Downloads"
audio_dir=r"C:\Users\VICTUS\Downloads\_downloaded audio"

class Event_Changer(FileSystemEventHandler):
    def on_modified():
        with os.scandir(downloads_dir) as download_files:
            for items in download_files:
                if items.is_file():
                    name=items.name
                    dest=downloads_dir
                    if name.endswith('.mp3'):
                        dest=audio_dir
                        move()


# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO,
#                         format='%(asctime)s - %(message)s',
#                         datefmt='%Y-%m-%d %H:%M:%S')
#     path = downloads_dir
#     event_handler = Event_Changer()
#     observer = Observer()
#     observer.schedule(event_handler, path)
#     observer.start()
#     try:
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         observer.stop()
#     observer.join()