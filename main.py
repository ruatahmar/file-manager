import os 
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil

downloads_dir=r"C:\Users\VICTUS\Downloads"
audio_dir=r"C:\Users\VICTUS\downloads sorted\_downloaded audio"
torrents_dir=r"C:\Users\VICTUS\downloads sorted\_torrents"
videos_dir=r"C:\Users\VICTUS\downloads sorted\_downloaded videos"
pics_dir=r"C:\Users\VICTUS\downloads sorted\_downloaded pics"
docs_dir=r"C:\Users\VICTUS\downloads sorted\_documents"
zip_dir=r"C:\Users\VICTUS\downloads sorted\_zip files"

def make_unique(name,dest):
    base, ext = os.path.splitext(name)
    counter = 1
    print(base,ext)
    new_name = f"{base}_{counter}{ext}"
    name_to_check=os.path.join(dest, new_name)
    while os.path.exists(name_to_check):
        counter += 1
        new_name = f"{base}_{counter}{ext}"
        name_to_check=os.path.join(dest, new_name)
    return new_name

def move(dest,entry,name):
    name_to_check=os.path.join(dest, name)
    name_exists=os.path.exists(name_to_check)
    if name_exists:
        new_name = make_unique(name, dest)
        new_name_path = os.path.join(dest, new_name)
        os.rename(entry, new_name_path)
        shutil.move(new_name_path, dest)
        return None
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

def  main():
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


if __name__ == "__main__":
    main()