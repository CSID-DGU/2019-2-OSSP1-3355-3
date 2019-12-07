from stacked_hourglass import HumanPosePredictor, hg2, hg8
from stacked_hourglass.utils.transforms import shufflelr, crop, color_normalize, fliplr, transform
from PIL import Image
import torch
import numpy as np
import xgboost as xgb
import matplotlib.pyplot as plt
from matplotlib import collections  as mc
import time,cv2,json,os
from astropy.convolution import Gaussian1DKernel, convolve
import PIL.ExifTags as ExifTags
from predict_arm_angle import *

# ...load image of a person into a PyTorch tensor...

name = "IMG_4529"

predictor = HumanPosePredictor(hg8(pretrained=True), device='cuda')
angle_predictor = arm_angle_predict()
model = xgb.XGBClassifier(max_depth=3, learning_rate=0.1, n_estimators=100,
                      silent=True, objective='binary:logistic',
                      booster='gbtree',
                      n_jobs=1, nthread=None, gamma=0, min_child_weight=1,
                      max_delta_step=0, subsample=1, colsample_bytree=1,
                      colsample_bylevel=1, reg_alpha=0, reg_lambda=1,
                      scale_pos_weight=1, base_score=0.5, random_state=0,
                      seed=None, missing=None)
model.load_model('./xgboost.bst') # load model
g = Gaussian1DKernel(stddev=4)

print("==model loaded==")

def smoothListGaussian(list, degree=5):
    window = degree*2-1
    weight = np.array([1.0]*window)
    weightGauss = []
    for i in range(window):
        i = i-degree+1
        frac = i/float(window)
        gauss = 1/(np.exp((4*(frac))**2))
        weightGauss.append(gauss)
    weight = np.array(weightGauss)*weight
    smoothed = [0.0]*(len(list)-window)
    for i in range(len(smoothed)):
        smoothed[i] = sum(np.array(list[i:i+window])*weight)/sum(weight)
    return smoothed
def decide(past, now):
    if(past is None):
        return -1
    else:
        if((past<=0.35) and (now>0.9) ):
            #up
            return 1
        elif((past>0.9) and (now<=0.35)):
            #down
            return 0
        else:
            return -1

RGB_MEAN = torch.as_tensor([0.4404, 0.4440, 0.4327])
RGB_STDDEV = torch.as_tensor([0.2458, 0.2410, 0.2468])

images = os.listdir("./video/"+name)
images = sorted(images, key=lambda x: int(x.split(".")[0]))
print("frames : ",len(images))

result = {"name"  : name,
          "frames": dict()}


threshold = 0.4
img_array = list()
testResult = list()
for i in images:
    print("!precessing "+str(i))
    orgImg = Image.open("./video/"+name+"/"+i)
    orgImg=orgImg.rotate(270, expand=True)

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
        pass

    im = np.asarray(orgImg)
    idx = int(i[:-4])

    img = torch.tensor(im).transpose(0,2)
    img = color_normalize(img, RGB_MEAN, RGB_STDDEV)
    joints = predictor.estimate_joints(img, flip=True)
    xs,ys = list(joints[:,0].numpy()), list(joints[:,1].numpy())

    angles = angle_predictor.predictFromjoints(joints)
    prob = model.predict_proba(np.asarray(angles).reshape(1,4))[0][1]
    testResult.append(prob)
    #smoothing = convolve(testResult[:], g)
    smoothing = smoothListGaussian(testResult[:])
    ascending = True
    descending = False
    count = 0
    for p in range(1,len(smoothing)-1):
        if((smoothing[p]<threshold and smoothing[p+1]>=threshold) and ascending):
            ascending = False
            descending = True
        elif((smoothing[p]>threshold and smoothing[p+1]<=threshold) and descending):
            ascending = True
            descending = False
            count += 1

    orgImg = np.array(orgImg)
    height, width, layers = orgImg.shape
    size = (width,height)
    #orgImg = cv2.line(orgImg, (ys[0], xs[0]), (ys[1], xs[1]), (10, 255, 0), 2)
    #orgImg = cv2.line(orgImg, (ys[1], xs[1]), (ys[2], xs[2]), (50, 160, 50), 2)
    #orgImg = cv2.line(orgImg, (ys[5], xs[5]), (ys[4], xs[4]), (50, 0, 255), 2)
    #orgImg = cv2.line(orgImg, (ys[4], xs[4]), (ys[3], xs[3]), (255, 0, 0), 2)
    #orgImg = cv2.line(orgImg, (ys[3], xs[3]), (ys[6], xs[6]), (255, 0, 0), 2)
    #orgImg = cv2.line(orgImg, (ys[6], xs[6]), (ys[2], xs[2]), (30, 30, 130), 2)
    orgImg = cv2.line(orgImg, (ys[6], xs[6]), (ys[7], xs[7]), (153, 255, 255), 3) #등
    #orgImg = cv2.line(orgImg, (ys[7], xs[7]), (ys[8], xs[8]), (255, 0, 0), 2)
    #orgImg = cv2.line(orgImg, (ys[8], xs[8]), (ys[9], xs[9]), (255, 0, 0), 2)
    orgImg = cv2.line(orgImg, (ys[10], xs[10]), (ys[11], xs[11]), (153, 255, 255), 3) #왼쪽전완
    orgImg = cv2.line(orgImg, (ys[11], xs[11]), (ys[12], xs[12]), (153, 255, 255), 3)
    orgImg = cv2.line(orgImg, (ys[12], xs[12]), (ys[7], xs[7]), (153, 255, 255), 3) #왼쪽광배
    orgImg = cv2.line(orgImg, (ys[14], xs[14]), (ys[13], xs[13]), (153, 255, 255),3) #오른쪽 이두
    orgImg = cv2.line(orgImg, (ys[7], xs[7]), (ys[13], xs[13]), (153, 255, 255), 3) #오른쪽 광배
    orgImg = cv2.line(orgImg, (ys[14], xs[14]), (ys[15], xs[15]), (153, 255, 255), 3) #오른쪽 전완
    if(len(smoothing)>0):
        print(smoothing)
        orgImg = cv2.putText(orgImg, str(smoothing[-1]), (30, 30) , cv2.FONT_HERSHEY_SIMPLEX , 1, (255, 0, 0) , 2, cv2.LINE_AA)
        orgImg = cv2.putText(orgImg, "count : "+str(count), (30, 75) , cv2.FONT_HERSHEY_SIMPLEX , 1, (255, 0, 0) , 2, cv2.LINE_AA)

    cv2.imshow('image',cv2.cvtColor(orgImg, cv2.COLOR_BGR2RGB))
    img_array.append(cv2.cvtColor(orgImg, cv2.COLOR_BGR2RGB))

    result["frames"][idx] = joints.numpy().tolist()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

out = cv2.VideoWriter('seungyoun_pullup.mp4',cv2.VideoWriter_fourcc(*'mp4v'), 30, size)
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()

print(result)

with open(name+'.json', 'w') as f:
    json.dump(result, f)

cv2.destroyAllWindows()
