import cv2
import os

title = "풀업.mp4"
vidcap = cv2.VideoCapture(title)

#make folder
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' + directory)
createFolder('C:/Users/jw969/PycharmProjects/test/pullup')

#make frame and store folder
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    base_dir = 'C:/Users/jw969/PycharmProjects/test/pullup'
    os.chdir(base_dir)
    os.getcwd()
    if hasFrames:
        cv2.imwrite("image"+str(count)+".jpg", image)     # save frame as JPG file
    return hasFrames
sec = 0
frameRate = 0.1     #//it will capture image in each 0.5 second
count = 100
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)
