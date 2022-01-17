import os
import cv2
import json
import time
import numpy as np

import matplotlib as mpl
mpl.rcParams['toolbar'] = 'None' 
from matplotlib import pyplot as plt

fuzzer_file = "./fuzzer.json"
qr_folder = "../FakeGreenPassGenerator/genqr"
qr_imgs = []
qr_files = []

# --------------------- MAIN ---------------------
def main():
    # Load all images
    for filename in sorted(os.listdir(qr_folder), key=len):
        img = cv2.imread(os.path.join(qr_folder,filename))
        if img is not None:
            qr_imgs.append(img)
            qr_files.append(filename.replace(".png", ""))

    # Last file edit
    last_modified  = time.ctime(os.path.getmtime(fuzzer_file))

    # Current QR-code index
    count = 0

    # Setup plt
    fig,ax = plt.subplots(1,1)
    image = np.array([[1,1,1], [2,2,2], [3,3,3]])
    im = ax.imshow(image)
    plt.axis('off')

    while True:
        time.sleep(1)

        if last_modified != time.ctime(os.path.getmtime(fuzzer_file)):
            f = open(fuzzer_file, 'r', encoding='utf-8')
            string = f.read()
            try: 
                # Decode from JSON
                fuzzer = json.loads(string)

                if fuzzer["status"] == 1:
                    # Update image and counter
                    image = qr_imgs[count]

                    # Set "status" back to 0 and update file name
                    fuzzer["status"] = 0
                    fuzzer["file"] = qr_files[count]

                    # Update JSON file
                    f = open(fuzzer_file, 'w', encoding='utf-8')
                    json.dump(fuzzer, f, ensure_ascii=False, indent=4)
                    f.close()

                    # Update image
                    im.set_data(image)
                    fig.canvas.draw_idle()
                    plt.pause(1)  # FIXME? This block the UI after 1s

                    print("> Ok:", qr_files[count])

                    count += 1
            except:
                pass

        last_modified = time.ctime(os.path.getmtime(fuzzer_file))


if __name__ == "__main__":
    main()