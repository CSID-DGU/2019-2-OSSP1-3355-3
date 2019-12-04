from stacked_hourglass import HumanPosePredictor, hg2, hg8, hg1
from stacked_hourglass.utils.transforms import shufflelr, crop, color_normalize, fliplr, transform
from PIL import Image
import torch
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections  as mc
import time, math,os
import PIL.ExifTags as ExifTags

class arm_angle_predict():
    def __init__(self):
        self.predictor = HumanPosePredictor(hg8(pretrained=True), device='cpu')
        print("==model loaded==")

    def predictfromDir(self,path):
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
        joints = self.predictor.estimate_joints(img, flip=True)
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

        #angle predict
        left_arm_angle   = np.arccos(left_arm_angle)*360/(np.pi*2)
        left_back_angle  = 180-np.arccos(left_back_angle)*360/(np.pi*2)
        right_arm_angle  = np.arccos(right_arm_angle)*360/(np.pi*2)
        right_back_angle = 180-np.arccos(right_back_angle)*360/(np.pi*2)

        return left_arm_angle,left_back_angle,right_arm_angle,right_back_angle

    def predictFromjoints(self,joints):

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

        #angle predict
        left_arm_angle   = np.arccos(left_arm_angle)*360/(np.pi*2)
        left_back_angle  = 180-np.arccos(left_back_angle)*360/(np.pi*2)
        right_arm_angle  = np.arccos(right_arm_angle)*360/(np.pi*2)
        right_back_angle = 180-np.arccos(right_back_angle)*360/(np.pi*2)

        return left_arm_angle,left_back_angle,right_arm_angle,right_back_angle
