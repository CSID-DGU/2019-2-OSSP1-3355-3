from stacked_hourglass.model import hg2, hg8, hg1
from stacked_hourglass.predictor import  HumanPosePredictor
from stacked_hourglass.utils.transforms import shufflelr, crop, color_normalize, fliplr, transform
from PIL import Image
import torch
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections  as mc
import time, math
import PIL.ExifTags as ExifTags

# ...load image of a person into a PyTorch tensor...

model = hg8(pretrained=True)
predictor = HumanPosePredictor(model, device='cpu')

print("==model loaded==")

RGB_MEAN = torch.as_tensor([0.4404, 0.4440, 0.4327])
RGB_STDDEV = torch.as_tensor([0.2458, 0.2410, 0.2468])
#im = np.asarray(Image.open("./images/test14]].jpeg"))
orgImg = Image.open("./stacked_hourglass/datasets/up/f/3.jpg")
try:
    for orientation in ExifTags.TAGS.keys() :
            if ExifTags.TAGS[orientation]=='Orientation' : break
    exif=dict(orgImg._getexif().items())
    if exif[orientation] == 3:
        orgImg=orgImg.rotate(180, expand=True)
    elif exif[orientation] == 6 :
        orgImg=orgImg.rotate(270, expand=True)
    elif exif[orientation] == 8 :
        orgImg=orgImg.rotate(90, expand=True)

except:
    print("no metadata")
im = np.asarray(orgImg)
img = torch.tensor(im).transpose(0,2)
img = color_normalize(img, RGB_MEAN, RGB_STDDEV)
if(img.size(0)==4):
    img = img[:3]

c,h,w = img.size()
print("image size : ",h,w)
start = time.time()
joints = predictor.estimate_joints(img, flip=True)
end = time.time()
xs,ys = list(joints[:,0].numpy()), list(joints[:,1].numpy())
print(joints)
print("infer time : ",end-start)

fig, ax = plt.subplots()
plt.imshow(im)
c = np.array([(0, 1, 1, 0.5),
              (0, 1, 1, 0.5),
              (0, 0, 1, 0.5),
              (0, 0, 1, 0.5),
              (0, 0.3, 0.7, 0.5),
              (0, 0.3, 0.7, 0.5),
              (0.1, 0.6, 0.7, 0.5),
              (0.1, 0, 0.2, 0.5),
              (0, 0.5, 0.5, 0.5),
              (0.1, 0.6, 0.2, 0.5),
              (0, 1, 0.15, 0.5),
              (0, 1, 0.15, 0.5),
              (0, 0, 1, 0.5),
              (0, 0, 1, 0.5),
              (0, 0.3, 0.5, 0.5)])  # RGBA color
lines = [[(ys[0], xs[0]), (ys[1], xs[1])],
         [(ys[1], xs[1]), (ys[2], xs[2])],
         [(ys[5], xs[5]), (ys[4], xs[4])],  # left leg to left knee
         [(ys[4], xs[4]), (ys[3], xs[3])],  # right lef to right knee
         [(ys[3], xs[3]), (ys[6], xs[6])],  # plevis to right leg
         [(ys[6], xs[6]), (ys[2], xs[2])],  # plevis to left leg
         [(ys[6], xs[6]), (ys[7], xs[7])],  # chest to hip
         [(ys[7], xs[7]), (ys[8], xs[8])],  # neck to chest
         [(ys[8], xs[8]), (ys[9], xs[9])],  # head to neck
         [(ys[10], xs[10]), (ys[11], xs[11])],
         [(ys[11], xs[11]), (ys[12], xs[12])],
         [(ys[12], xs[12]), (ys[ 7], xs[ 7])],
         [(ys[ 7], xs[ 7]), (ys[13], xs[13])],
         [(ys[14], xs[14]), (ys[13], xs[13])],
         [(ys[14], xs[14]), (ys[15], xs[15])]]

lc = mc.LineCollection(lines, colors=c,linewidths=2)
ax.add_collection(lc)
plt.scatter(ys, xs)


# 플랭크를 위한 각도 계산
"""
head_neck           = np.array([ys[9]-ys[8],xs[9]-xs[8]])
neck_chest          = np.array([ys[7]-ys[8],xs[7]-xs[8]])
chest_spine         = np.array([ys[6]-ys[7],xs[6]-xs[7]])
hip                 = np.array([ys[6]-ys[7],xs[6]-xs[7]])
leg                 = np.array([ys[4]-ys[3],xs[4]-xs[3]])

neck_angle          = np.inner(head_neck, neck_chest)/(np.linalg.norm(head_neck)*np.linalg.norm(neck_chest))
chest_angle         = np.inner(neck_chest, chest_spine)/(np.linalg.norm(neck_chest)*np.linalg.norm(chest_spine))
hip_angle           = np.inner(hip, leg)/(np.linalg.norm(hip)*np.linalg.norm(leg))

print("목 각    : ",np.arccos(neck_angle)*360/(np.pi*2))
print("명치 각   : ",180-np.arccos(chest_angle)*360/(np.pi*2))
print("엉덩이 각    : ",180-np.arccos(hip_angle)*360/(np.pi*2))
"""

head_neck           = np.array([ys[9]-ys[8],xs[9]-xs[8]])
chest_neck          = np.array([ys[7]-ys[8],xs[7]-xs[8]])

neck_chest          = np.array([ys[8]-ys[7],xs[8]-xs[7]])
hip_chest           = np.array([ys[6]-ys[7],xs[6]-xs[7]])

chest_hip           = np.array([ys[7]-ys[6],xs[7]-xs[6]])
knee_plevis         = np.array([ys[4]-ys[3],xs[4]-xs[3]])

neck_angle          = np.inner(head_neck, chest_neck)/(np.linalg.norm(head_neck)*np.linalg.norm(chest_neck))
chest_angle         = np.inner(neck_chest, hip_chest)/(np.linalg.norm(neck_chest)*np.linalg.norm(hip_chest))
hip_angle           = np.inner(chest_hip, knee_plevis)/(np.linalg.norm(chest_hip)*np.linalg.norm(knee_plevis))

print("목 각    : ",np.arccos(neck_angle)*360/(np.pi*2))
print("가슴 각   : ",np.arccos(chest_angle)*360/(np.pi*2))
print("엉덩이 각    : ",np.arccos(hip_angle)*360/(np.pi*2))

neck  = np.arccos(neck_angle)*360/(np.pi*2)
chest = np.arccos(chest_angle)*360/(np.pi*2)
hip   = np.arccos(hip_angle)*360/(np.pi*2)

if(170 <= neck < 180):   # 목 각도가 오차 범위를 벗어난 경우
    np[8] = [1, 0, 0, 0.5]  # line color = red
    np[7] = [1, 0, 0, 0.5]  # line color = red
if(165 <= chest < 180):  # 가슴 각도가 오차 범위를 벗어난 경우
    np[7] = [1, 0, 0, 0.5]  # line color = red
    np[6] = [1, 0, 0, 0.5]  # line color = red
if(165 <= hip < 180):    # 엉덩이 각도가 오차 범위를 벗어난 경우
    np[6] = [1, 0, 0, 0.5]  # line color = red
    np[5] = [1, 0, 0, 0.5]  # line color = red
    np[4] = [1, 0, 0, 0.5]  # line color = red
    np[3] = [1, 0, 0, 0.5]  # line color = red
    np[2] = [1, 0, 0, 0.5]  # line color = red


plt.show()  # keypoint detection 이미지로 출력