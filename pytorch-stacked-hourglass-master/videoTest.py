from stacked_hourglass import HumanPosePredictor, hg2
from stacked_hourglass.utils.transforms import shufflelr, crop, color_normalize, fliplr, transform
from PIL import Image
import torch
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections  as mc
import time,cv2,json

# ...load image of a person into a PyTorch tensor...

model = hg2(pretrained=True)
predictor = HumanPosePredictor(model, device='cpu')

print("==model loaded==")

RGB_MEAN = torch.as_tensor([0.4404, 0.4440, 0.4327])
RGB_STDDEV = torch.as_tensor([0.2458, 0.2410, 0.2468])

cap = cv2.VideoCapture('./test_video/test1.mp4')
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print("frames : ",length)

result = {"name"  : "test1",
          "frames": dict()}

idx = 0
while(cap.isOpened()):
    if(idx==length/10):
        break
    print(idx)
    ret, frame = cap.read()

    img = torch.tensor(frame).transpose(0,2)
    img = color_normalize(img, RGB_MEAN, RGB_STDDEV)
    joints = predictor.estimate_joints(img, flip=True)

    result["frames"][idx] = joints.numpy().tolist()
    idx += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print(result)

with open('test1.json', 'w') as f:
    json.dump(result, f)

cap.release()
cv2.destroyAllWindows()
