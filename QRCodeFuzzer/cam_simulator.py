import pyvirtualcam
import numpy as np
import cv2
import os

folder = "../FakeGreenPassGenerator/genqr"
qrcodes = []
for filename in os.listdir(folder):
    img = cv2.imread(os.path.join(folder,filename))
    if img is not None:
        qrcodes.append(img)

HW = qrcodes[0].shape[0]
print(HW)
with pyvirtualcam.Camera(width=HW, height=HW, fps=30) as cam:
    while True:
        frame = qrcodes[0]
        # frame = np.zeros((cam.height, cam.width, 3), np.uint8) # RGBA
        # frame[:,:,:3] = cam.frames_sent % 255 # grayscale animation
        # frame[:,:,2] = 255
        cam.send(frame)
        cam.sleep_until_next_frame()
        cam.sleep_until_next_frame()
        