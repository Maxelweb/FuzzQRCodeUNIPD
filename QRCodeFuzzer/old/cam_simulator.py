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

h, w, _ = qrcodes[0].shape
print(h, w)
with pyvirtualcam.Camera(width=1920, height=1080, fps=30, fmt=pyvirtualcam.PixelFormat.RGB, backend="v4l2loopback") as cam:
    print('Virtual camera device: ' + cam.device)
    while True:
        # frame = qrcodes[0]
        frame = np.zeros((cam.height, cam.width, 3), np.uint8) # RGBA
        frame = cv2.copyMakeBorder(qrcodes[0], (cam.height-h)//2, (cam.height-h)//2, (cam.width-w)//2, (cam.width-w)//2, cv2.BORDER_CONSTANT)
        # frame[:,:,:3] = cam.frames_sent % 255 # grayscale animation
        # frame[:,:,2] = 255
        cam.send(frame)
        cam.sleep_until_next_frame()
