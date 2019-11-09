# Importing all necessary libraries
import cv2
import os
import imutils

# Read the video from specified path
cam = cv2.VideoCapture("./video/pullup3_2.mp4")

# frame
currentframe = -1

while(True):
    currentframe += 1
    if(currentframe%10!=0):
        continue
    # reading from frame
    ret,frame = cam.read()

    if ret:
        # if video is still left continue creating images
        name = './video/pullup3_2/' + str(currentframe) + '.jpg'
        print ('Creating...' + name)


        #frame = imutils.rotate(frame, -90)
        # writing the extracted images
        cv2.imwrite(name, frame)

        # increasing counter so that it will
        # show how many frames are created
    else:
        break

# Release all space and windows once done
cam.release()
cv2.destroyAllWindows()
