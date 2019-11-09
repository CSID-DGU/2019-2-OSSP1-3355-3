from stacked_hourglass import HumanPosePredictor, hg2, hg8
from stacked_hourglass.utils.transforms import shufflelr, crop, color_normalize, fliplr, transform
from PIL import Image
import torch
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections  as mc
import time,cv2,json,os

# ...load image of a person into a PyTorch tensor...

name = "pullup3_2"

model = hg8(pretrained=True)
predictor = HumanPosePredictor(model, device='cpu')

print("==model loaded==")

RGB_MEAN = torch.as_tensor([0.4404, 0.4440, 0.4327])
RGB_STDDEV = torch.as_tensor([0.2458, 0.2410, 0.2468])

images = os.listdir("./video/"+name)
images = sorted(images, key=lambda x: int(x.split(".")[0]))
print("frames : ",len(images))

result = {"name"  : name,
          "frames": dict()}

img_array = list()
for i in images:
    print("!precessing "+str(i))
    orgImg = Image.open("./video/"+name+"/"+i)
    im = np.asarray(orgImg)
    idx = int(i[:-4])

    img = torch.tensor(im).transpose(0,2)
    img = color_normalize(img, RGB_MEAN, RGB_STDDEV)
    joints = predictor.estimate_joints(img, flip=True)
    xs,ys = list(joints[:,0].numpy()), list(joints[:,1].numpy())

    orgImg = np.array(orgImg)
    height, width, layers = orgImg.shape
    size = (width,height)
    orgImg = cv2.line(orgImg, (ys[0], xs[0]), (ys[1], xs[1]), (10, 255, 0), 2)
    orgImg = cv2.line(orgImg, (ys[1], xs[1]), (ys[2], xs[2]), (50, 160, 50), 2)
    orgImg = cv2.line(orgImg, (ys[5], xs[5]), (ys[4], xs[4]), (50, 0, 255), 2)
    orgImg = cv2.line(orgImg, (ys[4], xs[4]), (ys[3], xs[3]), (255, 0, 0), 2)
    orgImg = cv2.line(orgImg, (ys[3], xs[3]), (ys[6], xs[6]), (255, 0, 0), 2)
    orgImg = cv2.line(orgImg, (ys[6], xs[6]), (ys[2], xs[2]), (30, 30, 130), 2)
    orgImg = cv2.line(orgImg, (ys[6], xs[6]), (ys[7], xs[7]), (30, 30, 50), 2) #등
    orgImg = cv2.line(orgImg, (ys[7], xs[7]), (ys[8], xs[8]), (255, 0, 0), 2)
    orgImg = cv2.line(orgImg, (ys[8], xs[8]), (ys[9], xs[9]), (255, 0, 0), 2)
    orgImg = cv2.line(orgImg, (ys[10], xs[10]), (ys[11], xs[11]), (30, 10, 100), 2) #왼쪽전완
    orgImg = cv2.line(orgImg, (ys[11], xs[11]), (ys[12], xs[12]), (255, 0, 0), 2)
    orgImg = cv2.line(orgImg, (ys[12], xs[12]), (ys[7], xs[7]), (10, 70, 200), 2) #왼쪽광배
    orgImg = cv2.line(orgImg, (ys[14], xs[14]), (ys[13], xs[13]), (255, 0, 0),2) #오른쪽 이두
    orgImg = cv2.line(orgImg, (ys[7], xs[7]), (ys[13], xs[13]), (10, 250, 70), 2) #오른쪽 광배
    orgImg = cv2.line(orgImg, (ys[14], xs[14]), (ys[15], xs[15]), (255, 0, 0), 2)
    cv2.imshow('image',orgImg)
    img_array.append(orgImg)

    result["frames"][idx] = joints.numpy().tolist()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

out = cv2.VideoWriter('seungyoun_pullup.avi',cv2.VideoWriter_fourcc(*'DIVX'), 15, size)
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()

print(result)

with open(name+'.json', 'w') as f:
    json.dump(result, f)

cap.release()
cv2.destroyAllWindows()
