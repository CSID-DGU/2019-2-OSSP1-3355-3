#!/usr/bin/env python
# coding: utf-8

# In[17]:


from stacked_hourglass import HumanPosePredictor, hg2, hg8, hg1
from stacked_hourglass.utils.transforms import shufflelr, crop, color_normalize, fliplr, transform
from PIL import Image
import torch
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections  as mc
import time, math,os
import PIL.ExifTags as ExifTags
from tqdm import tqdm
import seaborn as sns


# In[18]:


# ...load image of a person into a PyTorch tensor...

model = hg8(pretrained=True)
predictor = HumanPosePredictor(model, device='cpu')
root = "/Users/seungyoun/Desktop/DGU/2/공개SW/pytorch-stacked-hourglass-master/dataset"

print("==model loaded==")

RGB_MEAN = torch.as_tensor([0.4404, 0.4440, 0.4327])
RGB_STDDEV = torch.as_tensor([0.2458, 0.2410, 0.2468])
#im = np.asarray(Image.open("./images/test14.jpeg"))
up = os.listdir(root + "/up")
down = os.listdir(root + "/down")
print("up   samples : ",len(up),"\ndown samples : ",len(down))


# In[43]:


def predict(path):
    orgImg = Image.open(path)

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
    img = torch.tensor(im).transpose(0,2)
    img = color_normalize(img, RGB_MEAN, RGB_STDDEV)
    if(img.size(0)==4):
        img = img[:3]

    c,h,w = img.size()
    start = time.time()
    joints = predictor.estimate_joints(img, flip=True)
    end = time.time()
    xs,ys = list(joints[:,0].numpy()), list(joints[:,1].numpy())
    #print("infer time : ",end-start)


    left_antebrachial   = np.array([ys[15]-ys[14],xs[15]-xs[14]])
    left_forearm        = np.array([ys[13]-ys[14],xs[13]-xs[14]])
    left_back           = np.array([ys[7]-ys[13], xs[7]-xs[13]])
    left_arm_angle      = np.inner(left_antebrachial, left_forearm)/(np.linalg.norm(left_antebrachial)*np.linalg.norm(left_forearm))
    left_back_angle     = np.inner(left_forearm, left_back)/(np.linalg.norm(left_forearm)*np.linalg.norm(left_back))

    right_antebrachial  = np.array([ys[10]-ys[11],xs[10]-xs[11]])
    right_forearm       = np.array([ys[12]-ys[11],xs[12]-xs[11]])
    right_back          = np.array([ys[7]-ys[12], xs[7]-xs[12]])
    right_arm_angle     = np.inner(right_antebrachial, right_forearm)/(np.linalg.norm(right_antebrachial)*np.linalg.norm(right_forearm))
    right_back_angle    = np.inner(right_back, right_forearm)/(np.linalg.norm(right_back)*np.linalg.norm(right_forearm))

    left_arm_angle   = np.arccos(left_arm_angle)*360/(np.pi*2)
    left_back_angle  = 180-np.arccos(left_back_angle)*360/(np.pi*2)
    right_arm_angle  = np.arccos(right_arm_angle)*360/(np.pi*2)
    right_back_angle = 180-np.arccos(right_back_angle)*360/(np.pi*2)

    return left_arm_angle,left_back_angle,right_arm_angle,right_back_angle


# In[44]:


upDist   = list()
downDist = list()

for i in tqdm(up):
    left_arm_angle,left_back_angle,right_arm_angle,right_back_angle = predict(root+"/up/"+i)
    upDist.append([left_arm_angle, left_back_angle, right_arm_angle, right_back_angle])

for i in tqdm(down):
    left_arm_angle,left_back_angle,right_arm_angle,right_back_angle = predict(root+"/down/"+i)
    downDist.append([left_arm_angle, left_back_angle, right_arm_angle, right_back_angle])


# In[45]:


get_ipython().run_line_magic('matplotlib', 'inline')


# ## 올라간 동작 

# In[46]:


left_arm_angle   = [theta[0] for theta in upDist]
left_back_angle  = [theta[1] for theta in upDist]
right_arm_angle  = [theta[2] for theta in upDist]
right_back_angle = [theta[3] for theta in upDist]


# In[47]:


sns.distplot(left_arm_angle)


# In[48]:


sns.distplot(left_back_angle)


# In[49]:


sns.distplot(right_arm_angle)


# In[50]:


sns.distplot(right_back_angle)


# ## 내려간 동작

# In[51]:


left_arm_angle0   = [theta[0] for theta in downDist]
left_back_angle0  = [theta[1] for theta in downDist]
right_arm_angle0  = [theta[2] for theta in downDist]
right_back_angle0 = [theta[3] for theta in downDist]


# In[52]:


sns.distplot(left_arm_angle0)


# In[53]:


sns.distplot(left_back_angle0)


# In[54]:


sns.distplot(right_arm_angle0)


# In[55]:


sns.distplot(right_back_angle0)


# ## 같이 비교해볼까요~?

# In[56]:


kwargs = dict(alpha=0.5, bins=20)


# 왼쪽 팔 각

# In[57]:


plt.hist(left_arm_angle , **kwargs, color='g', label='Ideal')
plt.hist(left_arm_angle0, **kwargs, color='b', label='Fair')
plt.gca().set(title='left arm angle')


# 오른쪽 팔 각

# In[58]:


plt.hist(right_arm_angle , **kwargs, color='g', label='Ideal')
plt.hist(right_arm_angle0, **kwargs, color='b', label='Fair')
plt.gca().set(title='right arm angle')


# 왼쪽 광배 각

# In[59]:


plt.hist(left_back_angle , **kwargs, color='g', label='Ideal')
plt.hist(left_back_angle0, **kwargs, color='b', label='Fair')
plt.gca().set(title='left back angle')


# 오른쪽 광배 각

# In[60]:


plt.hist(right_back_angle , **kwargs, color='g', label='Ideal')
plt.hist(right_back_angle0, **kwargs, color='b', label='Fair')
plt.gca().set(title='right back angle')


# ## Prediction Model

# In[61]:


X = upDist+downDist
upCount   = len(upDist)
downCount = len(downDist)
Y = list()
for i in range(upCount):
    Y.append(1)
for i in range(downCount):
    Y.append(0)
X = np.asarray(X)
Y = np.asarray(Y)


# In[62]:


import xgboost as xgb
from sklearn.metrics import accuracy_score


model = xgb.XGBClassifier(max_depth=3, learning_rate=0.1, n_estimators=100,
                      silent=True, objective='binary:logistic',
                      booster='gbtree',
                      n_jobs=1, nthread=None, gamma=0, min_child_weight=1,
                      max_delta_step=0, subsample=1, colsample_bytree=1,
                      colsample_bylevel=1, reg_alpha=0, reg_lambda=1,
                      scale_pos_weight=1, base_score=0.5, random_state=0,
                      seed=None, missing=None)


# In[63]:


model.fit(X,Y)


# In[64]:


model.predict_proba(X[122].reshape(1,4))


# In[65]:


model.save_model('xgboost.bst')


# In[66]:


y_pred = model.predict(X)
predictions = [round(value) for value in y_pred]

# evaluate predictions
accuracy = accuracy_score(Y, predictions)
print("Accuracy: %.2f%%" % (accuracy * 100.0))


# ## Test image

# In[67]:


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import pickle

#testImage = root+ '/updowntest/test3.jpg'
testImage = '/Users/seungyoun/Desktop/DGU/2/공개SW/pytorch-stacked-hourglass-master/video/pullup/67.jpg'
plt.imshow(mpimg.imread(testImage))

model.load_model('./xgboost.bst')  # load data


# In[68]:


angles = predict(testImage)


# In[9]:


pred = model.predict_proba(np.asarray(angles).reshape(1,4))
#pred_cls = model.predict(np.asarray(angles).reshape(1,4))

print(pred)


# ## 올라갔다 내려갔다~ (up and down probability change)

# test1

# In[10]:


testDir = '/Users/seungyoun/Desktop/DGU/2/공개SW/pytorch-stacked-hourglass-master/video/pullup'
testInd = os.listdir(testDir)
testInd = sorted(testInd, key=lambda x: int(x.split(".")[0])) 
testImagesPaths = [testDir + "/" + i for i in testInd]


# In[13]:


testResults=list()
for i in tqdm(testImagesPaths):
    theta = predict(i)
    prob = model.predict_proba(np.asarray(theta).reshape(1,4))[0]
    testResults.append(prob[1])


# In[14]:


sns.lineplot(x = [i for i in range(len(testResults))], y= testResults)


# test2

# In[15]:


testDir2 = '/Users/seungyoun/Desktop/DGU/2/공개SW/pytorch-stacked-hourglass-master/video/pullup2'
testInd2 = os.listdir(testDir2)
testInd2 = sorted(testInd2, key=lambda x: int(x.split(".")[0])) 
testImagesPaths2 = [testDir2 + "/" + i for i in testInd2]


# In[16]:


testResults2=list()
for i in tqdm(testImagesPaths2):
    theta = predict(i)
    prob = model.predict_proba(np.asarray(theta).reshape(1,4))[0]
    testResults2.append(prob[1])


# In[ ]:


sns.lineplot(x = [i for i in range(len(testResults2))], y= testResults2)


# In[28]:


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


# In[118]:


for i in range(len(testResults)-1):
    if(decide(testResults[i], testResults[i+1]) != -1):
        print(decide(testResults[i], testResults[i+1]))


# ## video2count

# In[38]:


import cv2

path      = '/Users/seungyoun/Desktop/DGU/2/공개SW/pytorch-stacked-hourglass-master/video/pullup2.mp4'
save_path = '/Users/seungyoun/Desktop/DGU/2/공개SW/pytorch-stacked-hourglass-master/results'


# In[39]:


from PIL import ImageFont
from PIL import ImageDraw 

cap = cv2.VideoCapture(path)

RGB_MEAN = torch.as_tensor([0.4404, 0.4440, 0.4327])
RGB_STDDEV = torch.as_tensor([0.2458, 0.2410, 0.2468])

idx = 1
count = 0
past = None

while(cap.isOpened()):
    ret, frame = cap.read()
    img = torch.tensor(frame).transpose(0,2)
    img = color_normalize(img, RGB_MEAN, RGB_STDDEV)

    PILImage = Image.fromarray(frame, 'RGB')
    draw = ImageDraw.Draw(PILImage)
    #font_type = ImageFont.truetype("arial.ttf", 18)
    
    if(img.size(0)==4):
        img = img[:3]

    c,h,w = img.size()
    start = time.time()
    joints = predictor.estimate_joints(img, flip=True)
    end = time.time()
    xs,ys = list(joints[:,0].numpy()), list(joints[:,1].numpy())
    #print("infer time : ",end-start)


    left_antebrachial   = np.array([ys[15]-ys[14],xs[15]-xs[14]])
    left_forearm        = np.array([ys[13]-ys[14],xs[13]-xs[14]])
    left_back           = np.array([ys[7]-ys[13], xs[7]-xs[13]])
    left_arm_angle      = np.inner(left_antebrachial, left_forearm)/(np.linalg.norm(left_antebrachial)*np.linalg.norm(left_forearm))
    left_back_angle     = np.inner(left_forearm, left_back)/(np.linalg.norm(left_forearm)*np.linalg.norm(left_back))

    right_antebrachial  = np.array([ys[10]-ys[11],xs[10]-xs[11]])
    right_forearm       = np.array([ys[12]-ys[10],xs[12]-xs[10]])
    right_back          = np.array([ys[7]-ys[12], xs[7]-xs[12]])
    right_arm_angle     = np.inner(right_antebrachial, right_forearm)/(np.linalg.norm(right_antebrachial)*np.linalg.norm(right_forearm))
    right_back_angle    = np.inner(right_back, right_forearm)/(np.linalg.norm(right_back)*np.linalg.norm(right_forearm))

    left_arm_angle   = np.arccos(left_arm_angle)*360/(np.pi*2)
    left_back_angle  = 180-np.arccos(left_back_angle)*360/(np.pi*2)
    right_arm_angle  = np.arccos(right_arm_angle)*360/(np.pi*2)
    right_back_angle = 180-np.arccos(right_back_angle)*360/(np.pi*2)
    
    prob = model.predict_proba(np.asarray([left_arm_angle, left_back_angle, right_arm_angle, right_back_angle]).reshape(1,4))[0][1]
    
    print(left_arm_angle,right_arm_angle,prob)
    if(decide(past,prob)!= -1):
        count+=1
        print(count)
    
    past = prob
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    idx+=1
    
    draw.text((0, 0),str(count),(255,255,255))
    draw.text((0, 0),str(count),(255,255,255))
    PILImage.save(save_path+"/"+str(idx)+".jpg")
    
cap.release()
cv2.destroyAllWindows()


# In[ ]:





# In[52]:


from torch import nn

class DepthToSpace(nn.Module):

    def __init__(self, block_size):
        super().__init__()
        self.bs = block_size

    def forward(self, x):
        N, C, H, W = x.size()
        x = x.view(N, self.bs, self.bs, C // (self.bs ** 2), H, W)  # (N, bs, bs, C//bs^2, H, W)
        x = x.permute(0, 3, 4, 1, 5, 2).contiguous()  # (N, C//bs^2, H, bs, W, bs)
        x = x.view(N, C // (self.bs ** 2), H * self.bs, W * self.bs)  # (N, C//bs^2, H * bs, W * bs)
        return x


class SpaceToDepth(nn.Module):

    def __init__(self, block_size):
        super().__init__()
        self.bs = block_size

    def forward(self, x):
        N, C, H, W = x.size()
        x = x.view(N, C, H // self.bs, self.bs, W // self.bs, self.bs)  # (N, C, H//bs, bs, W//bs, bs)
        x = x.permute(0, 3, 5, 1, 2, 4).contiguous()  # (N, bs, bs, C, H//bs, W//bs)
        x = x.view(N, C * (self.bs ** 2), H // self.bs, W // self.bs)  # (N, C*bs^2, H//bs, W//bs)
        return x


import tensorflow as tf
import torch

# pytorch
x1 = torch.rand(2, 1024, 256, 256)
x2 = DepthToSpace(4)(x1)
x3 = SpaceToDepth(2)(x2)
print(x1.size())
print(x2.size())
print(x3.size())

# tensorflow
y1 = tf.transpose(x1.numpy(), [0, 2, 3, 1])  # NCHW -> NHWC
y2 = tf.depth_to_space(y1, 2)
y3 = tf.space_to_depth(y2, 2)

y1 = tf.transpose(y1, [0, 3, 1, 2])  # NHWC -> NCHW
y2 = tf.transpose(y2, [0, 3, 1, 2])
y3 = tf.transpose(y3, [0, 3, 1, 2])

y1, y2, y3 = tf.Session().run([y1, y2, y3])
print("="*30)
print(y1.shape)
print(y2.shape)
print(y3.shape)
print((y1 == y3).all())

# check consistency
print((x1.numpy() == y1).all())
print((x2.numpy() == y2).all())
print((x3.numpy() == y3).all())


# In[ ]:




