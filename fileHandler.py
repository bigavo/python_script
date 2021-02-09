from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import json
import time

class MyHandler(FileSystemEventHandler):
    i = 1
    def on_modified(self, event):
        new_name = "new_file_" + str(self.i) + ".txt"
        for filename in os.listdir(folder_to_track):
            file_exist = os.path.isfile(folder_destination + "/" + new_name)
            while file_exist: 
                self.i += 1
                new_name = "new_file_" + str(self.i) + ".txt"
            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + new_name
            os.rename(src, new_destination)


folder_to_track = 'Users/trinhtran/Desktop/myFolder'
folder_destination = 'Users/trinhtran/Desktop/newFolder'
event_handler  = MyHandler()
observer = Observer()
observer.schedule(event_handler,folder_to_track,recursive=True)
observer.start()
try: 
    while True: 
        time.sleep(10)
except Keyboardinterupt: 
    observer.stop()
    observer.join() 

print("123") # Linting tools