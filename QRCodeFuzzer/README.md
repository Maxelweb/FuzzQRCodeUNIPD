## QR Fuzzer for Android

### Requirements

- Appium (testing environment)
- Nodejs (to run appium and tests)
- vl4loopback (to simulate QR code from a virtual camera)

### Usefull Commands

Add v4l2loopback mock camera to modprobe module: 
`sudo modprobe v4l2loopback video_nr=0 card_label="mockCam"`

Launch QR Code to transmit inside the `/dev/videoX` device. 
`gst-launch-1.0 filesrc location=qr.png ! pngdec ! imagefreeze ! v4l2sink device=/dev/video0`

