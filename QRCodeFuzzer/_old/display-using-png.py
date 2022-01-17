import os
import cv2
import json
import time
# import pyqrcode

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

fuzzer_file = "./data/fuzzer.json"
qr_folder = "../FakeGreenPassGenerator/genqr"
qr_imgs = []
qr_files = []


# ---------------- EDIT EVENT HANDLER ----------------
class MyHandler(FileSystemEventHandler):
    def __init__(self):
        self.count = 0

    def on_modified(self, event):
        if event.src_path == fuzzer_file:
            # Read JSON file
            f = open(fuzzer_file, 'r', encoding='utf-8')
            string = f.read()
            try: 
                # Decode from JSON
                fuzzer = json.loads(string)

                if fuzzer["status"] == 1:
                    # Update image and counter
                    image = qr_imgs[self.count]

                    # Set "status" back to 0 and update file name
                    fuzzer["status"] = 0
                    fuzzer["file"] = qr_files[self.count]

                    # Update JSON file
                    f = open(fuzzer_file, 'w', encoding='utf-8')
                    json.dump(fuzzer, f, ensure_ascii=False, indent=4)
                    f.close()

                    # Update image
                    cv2.imwrite("qr_result.png", image)
                    print("> Ok:", qr_files[self.count])

                    if self.count >= len(qr_imgs)-1:
                        self.count = 0
                    else:
                        self.count += 1
            except:
                # JSON decoding throws some errors, but then works, dunno why
                pass


# --------------------- MAIN ---------------------
def main():

    # Load all images
    for filename in sorted(os.listdir(qr_folder), key=len):
        img = cv2.imread(os.path.join(qr_folder,filename))
        if img is not None:
            qr_imgs.append(img)
            qr_files.append(filename.replace(".png", ""))

    # Save img with the 1st qr-code
    cv2.imwrite("qr_result.png", qr_imgs[0])
    
    # Initialize JSON file
    fuzzer = {}
    fuzzer["status"] = 0
    fuzzer["file"] = qr_files[0]
    fuzzer["size"] = len(qr_files)
    f = open(fuzzer_file, 'w', encoding='utf-8')
    json.dump(fuzzer, f, ensure_ascii=False, indent=4)
    f.close()

    # Start edit event-handler on the folder
    # (didn't work with the single file, dunno why)
    file_modified_event = MyHandler()
    observer = Observer()
    observer.schedule(file_modified_event, "./")
    observer.start()
    try:
        while True:
            # Check every 1 sec
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    main()