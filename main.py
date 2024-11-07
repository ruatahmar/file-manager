import os 
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil

downloads_dir=r"C:\Users\VICTUS\Downloads"
audio_dir=r"C:\Users\VICTUS\Downloads\_downloaded audio"
torrents_dir=r"C:\Users\VICTUS\Downloads\_torrents"
videos_dir=r"C:\Users\VICTUS\Downloads\_downloaded videos"
pics_dir=r"C:\Users\VICTUS\Downloads\_downloaded pics"
docs_dir=r"C:\Users\VICTUS\Downloads\_documents"
zip_dir=r"C:\Users\VICTUS\Downloads\_zip files"


def move(dest,entry,name):
    shutil.move(entry,dest)

class Event_Changer(FileSystemEventHandler):
    def on_modified(self,event):
        with os.scandir(downloads_dir) as download_files:
            for entry in download_files:
                if entry.is_file():
                    name=entry.name
                    dest=downloads_dir
                    if name.endswith('.mp3'):
                        dest=audio_dir
                        move(dest,entry.path,name)
                    elif name.endswith(".torrent"):
                        dest=torrents_dir
                        move(dest,entry.path,name) 
                    elif name.endswith(".mp4") or name.endswith(".MOV"):
                        dest=videos_dir
                        move(dest,entry.path,name) 
                    elif name.endswith(".jpeg") or name.endswith(".jpg") or name.endswith(".png") or name.endswith(".webp"):
                        dest=pics_dir
                        move(dest,entry.path,name) 
                    elif name.endswith(".pdf") or name.endswith(".xls") or name.endswith(".xlsx") or name.endswith(".ppt") or name.endswith(".pptx") or name.endswith(".doc") or name.endswith(".docx"):
                        dest=docs_dir
                        move(dest,entry.path,name) 
                    elif name.endswith(".rar") or name.endswith(".zip"):
                        dest=zip_dir
                        move(dest,entry.path,name)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = downloads_dir
    event_handler = Event_Changer()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()