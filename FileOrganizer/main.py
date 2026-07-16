import organizer
from pathlib import Path
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import time

SOURCE_DIR = Path().home()/"Downloads"
DESTINATION_DIR = Path("D:/AllDocuments")

class FolderHandler(FileSystemEventHandler):
#     def on_created(self, event):
#         if event.is_directory:
#             return
#         time.sleep(5)
#         organize()
#         time.sleep(5)
    def on_modified(self, event):
        if event.is_directory:
            return
        time.sleep(5)
        organize()
        time.sleep(5)

def watchdog_observer():
    event_handler = FolderHandler() # instance of handler
    observer = Observer()           # instance of observer
    observer.schedule(event_handler, path=str(SOURCE_DIR), recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt: # ctrl + c
        observer.stop()
    observer.join()     # Wait until the background thread finishes cleaning up

def organize():  
    organizer.organise_folder(SOURCE_DIR, DESTINATION_DIR)

def main():
    organize()
    watchdog_observer()

if __name__ == "__main__":
    main()




