import pyvirtualcam
import numpy as np

with pyvirtualcam.Camera(width=1280, height=720, fps=30) as cam:
    while True:
        frame = np.zeros((cam.height, cam.width, 3), np.uint8) # RGBA
        frame[:,:,:3] = cam.frames_sent % 255 # grayscale animation
        frame[:,:,2] = 255
        cam.send(frame)
        cam.sleep_until_next_frame()
        cam.sleep_until_next_frame()