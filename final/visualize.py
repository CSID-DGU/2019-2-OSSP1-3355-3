import json
import cv2

with open('test_video/test1.json', 'r') as f:
    joints = json.load(f)

joints = joints['frames']

cap = cv2.VideoCapture('C:/Users/ysk78/PycharmProjects/3355/jin.mp4')
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print("frames : ",length)

idx = 0
while(cap.isOpened()):
    if(idx==length/10):
        break
    print(idx)
    ret, frame = cap.read()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
