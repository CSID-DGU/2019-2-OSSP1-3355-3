from stacked_hourglass import HumanPosePredictor, hg2, hg8
from stacked_hourglass.utils.transforms import shufflelr, crop, color_normalize, fliplr, transform
from PIL import Image
import torch
import numpy as np
import time,cv2,json,os
import shutil


# ...load image of a person into a PyTorch tensor...
class test_plank:
    # make folder
    def createFolder(self, directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print('Error: Creating directory. ' + directory)

    # make frame and store folder
    def getFrame(self, sec, vidcap, viddir, count):
        vidcap.set(cv2.CAP_PROP_POS_MSEC, sec * 1000)
        hasFrames, image = vidcap.read()
        base_dir = viddir + '/tmp+img'
        os.chdir(base_dir)
        os.getcwd()
        if hasFrames:
            img_name = str(count) + ".jpg"
            cv2.imwrite(img_name, image)  # save frame as JPG file
        return hasFrames

    def __init__(self, fn):

        filename = fn
        # get video and slice into frame
        viddir = filename
        vidcap = cv2.VideoCapture(viddir)
        vidlen = len(viddir)
        except_filename = 0
        for i in range(vidlen - 1, -1, -1):
            if viddir[i] == '/':
                except_filename = i
                break
        viddir = viddir[0:except_filename + 1]

        img_name = " "

        paradir = viddir + '/tmp+img'
        self.createFolder(paradir)

        sec = 0
        frameRate = 0.1  # //it will capture image in each 0.5 second
        count = 100
        success = self.getFrame(sec, vidcap, viddir, count)
        while success:
            count = count + 1
            sec = sec + frameRate
            sec = round(sec, 2)
            success = self.getFrame(sec, vidcap, viddir, count)

        name = ""

        model = hg8(pretrained=True)
        predictor = HumanPosePredictor(model, device='cpu')

        print("==model loaded==")

        RGB_MEAN = torch.as_tensor([0.4404, 0.4440, 0.4327])
        RGB_STDDEV = torch.as_tensor([0.2458, 0.2410, 0.2468])

        images = os.listdir(paradir + "/" + name)
        images = sorted(images, key=lambda x: int(x.split(".")[0]))
        print("frames : ", len(images))

        result = {"name": name,
                  "frames": dict()}

        img_array = list()
        for i in images:
            c = ([(0, 0, 255),
                  (0, 0, 255),
                  (0, 0, 255),
                  (0, 0, 255),
                  (0, 0, 255),
                  (0, 0, 255),
                  (0, 0, 255),
                  (0, 0, 255),
                  (0, 0, 255),
                  (0, 0, 255),
                  (0, 0, 255),
                  (0, 0, 255),
                  (0, 0, 255),
                  (0, 0, 255),
                  (0, 0, 255)])

            print("!precessing " + str(i))
            orgImg = Image.open("./" + name + "/" + i)
            im = np.asarray(orgImg)
            idx = int(i[:-4])

            img = torch.tensor(im).transpose(0, 2)
            img = color_normalize(img, RGB_MEAN, RGB_STDDEV)
            joints = predictor.estimate_joints(img, flip=True)
            xs, ys = list(joints[:, 0].numpy()), list(joints[:, 1].numpy())

            orgImg = np.array(orgImg)
            height, width, layers = orgImg.shape
            size = (width, height)

            head_neck = np.array([ys[9] - ys[8], xs[9] - xs[8]])
            chest_neck = np.array([ys[7] - ys[8], xs[7] - xs[8]])

            neck_chest = np.array([ys[8] - ys[7], xs[8] - xs[7]])
            hip_chest = np.array([ys[6] - ys[7], xs[6] - xs[7]])

            chest_hip = np.array([ys[7] - ys[6], xs[7] - xs[6]])
            knee_plevis = np.array([ys[4] - ys[3], xs[4] - xs[3]])

            try:
                neck_angle = np.inner(head_neck, chest_neck) / (np.linalg.norm(head_neck) * np.linalg.norm(chest_neck))
            except RuntimeWarning:
                neck_angle = 0
            try:
                chest_angle = np.inner(neck_chest, hip_chest) / (np.linalg.norm(neck_chest) * np.linalg.norm(hip_chest))
            except RuntimeWarning:
                chest_angle = 0
            try:
                hip_angle = np.inner(chest_hip, knee_plevis) / (np.linalg.norm(chest_hip) * np.linalg.norm(knee_plevis))
            except RuntimeWarning:
                hip_angle = 0


            neck_angle_result = round(np.arccos(neck_angle) * 360 / (np.pi * 2), 2)
            check_angle_result = round(np.arccos(chest_angle) * 360 / (np.pi * 2), 2)
            hip_angle_result = round(np.arccos(hip_angle) * 360 / (np.pi * 2))

            print("목 각    : ", neck_angle_result)
            print("가슴 각   : ", check_angle_result)
            print("엉덩이 각    : ", hip_angle_result)

            if (160 > neck_angle_result or neck_angle_result > 180):  # 목 각도가 오차 범위를 벗어난 경우
                c[8] = (255, 0, 0)  # line color = red
                c[7] = (255, 0, 0)  # line color = red
            if (160 > check_angle_result or check_angle_result > 180):  # 가슴 각도가 오차 범위를 벗어난 경우
                c[7] = (255, 0, 0)  # line color = red
                c[6] = (255, 0, 0)  # line color = red
            if (160 > hip_angle_result or hip_angle_result >= 175):  # 엉덩이 각도가 오차 범위를 벗어난 경우
                c[6] = (255, 0, 0)  # line color = red
                c[5] = (255, 0, 0)  # line color = red
                c[4] = (255, 0, 0)  # line color = red
                c[3] = (255, 0, 0)  # line color = red
                c[1] = (255, 0, 0)  # line color = red

            orgImg = cv2.line(orgImg, (ys[0], xs[0]), (ys[1], xs[1]), c[0], 2)
            orgImg = cv2.line(orgImg, (ys[1], xs[1]), (ys[2], xs[2]), c[1], 2)
            orgImg = cv2.line(orgImg, (ys[5], xs[5]), (ys[4], xs[4]), c[2], 2)
            orgImg = cv2.line(orgImg, (ys[4], xs[4]), (ys[3], xs[3]), c[3], 2)
            orgImg = cv2.line(orgImg, (ys[3], xs[3]), (ys[6], xs[6]), c[4], 2)
            orgImg = cv2.line(orgImg, (ys[6], xs[6]), (ys[2], xs[2]), c[5], 2)
            orgImg = cv2.line(orgImg, (ys[6], xs[6]), (ys[7], xs[7]), c[6], 2)  # 등
            orgImg = cv2.line(orgImg, (ys[7], xs[7]), (ys[8], xs[8]), c[7], 2)
            orgImg = cv2.line(orgImg, (ys[8], xs[8]), (ys[9], xs[9]), c[8], 2)
            orgImg = cv2.line(orgImg, (ys[10], xs[10]), (ys[11], xs[11]), c[9], 2)  # 왼쪽전완
            orgImg = cv2.line(orgImg, (ys[11], xs[11]), (ys[12], xs[12]), c[10], 2)
            orgImg = cv2.line(orgImg, (ys[12], xs[12]), (ys[7], xs[7]), c[11], 2)  # 왼쪽광배
            orgImg = cv2.line(orgImg, (ys[14], xs[14]), (ys[13], xs[13]), c[12], 2)  # 오른쪽 이두
            orgImg = cv2.line(orgImg, (ys[7], xs[7]), (ys[13], xs[13]), c[13], 2)  # 오른쪽 광배
            orgImg = cv2.line(orgImg, (ys[14], xs[14]), (ys[15], xs[15]), c[14], 2)

            # image show
            # cv2.imshow('image', cv2.cvtColor(orgImg, cv2.COLOR_BGR2RGB))
            img_array.append(cv2.cvtColor(orgImg, cv2.COLOR_BGR2RGB))

            result["frames"][idx] = joints.numpy().tolist()

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        out = cv2.VideoWriter('result.avi', cv2.VideoWriter_fourcc(*'mp4v'), 30, size)
        for i in range(len(img_array)):
            out.write(img_array[i])
        out.release()

        print(result)

        with open(name + '.json', 'w') as f:
            json.dump(result, f)

        #shutil.rmtree('C:/Users/ysk78/PycharmProjects/3355/tmp+img')  #### 이 부분 수정하자

        cv2.destroyAllWindows()
