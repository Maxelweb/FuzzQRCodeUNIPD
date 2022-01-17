#
# Display for FakeGreenPass generation
# --------------------


#from watchdog.observers import Observer
#from watchdog.events import FileSystemEventHandler

from qrgen import *
from passgen import *
from datetime import datetime

import sys
import argparse
import json
import pyqrcode
import tkinter as tk


fuzzer_file = "../QRCodeFuzzer/data/fuzzer.json"
qr_imgs = []
qr_files = []


# ---------------- EDIT EVENT HANDLER ----------------
#class MyHandler(FileSystemEventHandler):
class FileHandler():
    def __init__(self):
        self.count = 0
        self.initialize()
        self.iterator = 0

    def next(self):
        if(len(qr_files)-1 > self.iterator):
            self.iterator += 1
            return True
        return False

    def currentFilename(self):
        return qr_files[self.count]

    def initialize(self):
        # Initialize JSON file
        fuzzer = {}
        fuzzer["status"] = 0
        fuzzer["file"] = qr_files[0]
        fuzzer["size"] = len(qr_files)
        f = open(fuzzer_file, 'w', encoding='utf-8')
        json.dump(fuzzer, f, ensure_ascii=False, indent=4)
        f.close()

    def on_modified(self):
            # Read JSON file
            f = open(fuzzer_file, 'r', encoding='utf-8')
            string = f.read()
            try: 
                # Decode from JSON
                fuzzer = json.loads(string)

                if fuzzer["status"] == 1:
                    # Update image and counter
                    #image = qr_imgs[self.count]

                    # Set "status" back to 0 and update file name
                    fuzzer["status"] = 0
                    fuzzer["file"] = qr_files[self.count]

                    # Update JSON file
                    f = open(fuzzer_file, 'w', encoding='utf-8')
                    json.dump(fuzzer, f, ensure_ascii=False, indent=4)
                    f.close()

                    # Update image
                    # cv2.imwrite("qr_result.png", image)
                    print("> Ok:", qr_files[self.count])

                    if self.count >= len(qr_files)-1:
                        self.count = 0
                    else:
                        self.count += 1
            except:
                # JSON decoding throws some errors, but then works, dunno why
                pass


# --------------------- MAIN ---------------------
def main():

    # Load all images
    # for filename in sorted(os.listdir(qr_folder), key=len):
    #     img = cv2.imread(os.path.join(qr_folder,filename))
    #     if img is not None:
    #         qr_imgs.append(img)
    #         qr_files.append(filename.replace(".png", ""))

    # # Save img with the 1st qr-code
    # cv2.imwrite("qr_result.png", qr_imgs[0])
    
    
    opt = cmd()
    payloads = get_words(opt)

    for i in payloads:
        qr_files.append(fuzz_type[opt.list] + "-" + i)

    file = FileHandler()

    def gengp():
        msg = get_cose(get_pass(payloads[file.iterator]))
        msg = add_cose_key(msg, PRIVKEY)
        msg = flynn(msg.encode(), HEADER)
        msg = b45(msg)
        msg = b"HC1:" + msg
        print("RAW certificate: ", msg)
        print("-"*20)
        return msg, file.next()


    def update():
        gp, status = gengp()
        img2 = genqr(gp)
        panel.config(image=img2)
        panel.image = img2 #IPER MEGA IMPORTANT
        if not status:
            print("End of QR codes")
            window.destroy()
        else:
            window.after(1000, update)

    def genqr(text="test"):
        qrcode = pyqrcode.create(text)
        return tk.BitmapImage(data = qrcode.xbm(scale=8))

    

    window = tk.Tk()
    window.title("Display FakeGreenPass")
    window.geometry("800x800")
    window.configure(background='white')

    img = genqr("Test")
    panel = tk.Label(window, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")

    window.after(1000, update)
    window.mainloop()

   

    # # Start edit event-handler on the folder
    # # (didn't work with the single file, dunno why)
    # file_modified_event = MyHandler()
    # observer = Observer()
    # observer.schedule(file_modified_event, "./")
    # observer.start()
    # try:
    #     while True:
    #         # Check every 1 sec
    #         time.sleep(1)
    # except KeyboardInterrupt:
    #     observer.stop()
    # observer.join()


def cmd():
    parser = argparse.ArgumentParser(
        description="Display FakeGreenPass while scanning with Appium-controlled app",
        usage=f"main-display.py -l [number]\nusage: main-display.py -w [/path/to/custom/wordlist]\n\nPayload lists: \n {fuzz_type}"
    )
    sgroup = parser.add_argument_group("Options available")
    sgroup.add_argument(
        "--list",
        "-l",
        type=int,
        help="Set wordlist to use",
        choices=fuzz_type.keys(),
    )
    opt = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    return opt


if __name__ == "__main__":
    main()