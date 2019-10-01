import cv2

videoCapture = cv2.VideoCapture('video.h264')
success, image = videoCapture.read()
count = 0
while success:
    cv2.imwrite("frame%d.jpg" % count, image)
    success, image = videoCapture.read()
    print('Read a new frame: ', success)
    count += 1
