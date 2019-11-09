from stacked_hourglass import HumanPosePredictor, hg2
from stacked_hourglass.utils.transforms import shufflelr, crop, color_normalize, fliplr, transform
from PIL import Image
import torch
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import collections  as mc
import time,cv2,json,os

# ...load image of a person into a PyTorch tensor...

name = "pullup"

model = hg2(pretrained=True)
predictor = HumanPosePredictor(model, device='cpu')

print("==model loaded==")

RGB_MEAN = torch.as_tensor([0.4404, 0.4440, 0.4327])
RGB_STDDEV = torch.as_tensor([0.2458, 0.2410, 0.2468])

images = os.listdir("./video/"+name)
print("frames : ",len(images))

result = {"name"  : name,
          "frames": dict()}

for i in images:
    orgImg = Image.open("./video/"+name+"/"+i)
    im = np.asarray(orgImg)
    idx = int(i[:-4])

    img = torch.tensor(im).transpose(0,2)
    img = color_normalize(img, RGB_MEAN, RGB_STDDEV)
    joints = predictor.estimate_joints(img, flip=True)
    xs,ys = list(joints[:,0].numpy()), list(joints[:,1].numpy())

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
                  (0, 0, 0.5, 0.5)])
    lines = [[(ys[0], xs[0]), (ys[1], xs[1])],
             [(ys[1], xs[1]), (ys[2], xs[2])],
             [(ys[5], xs[5]), (ys[4], xs[4])],
             [(ys[4], xs[4]), (ys[3], xs[3])],
             [(ys[3], xs[3]), (ys[6], xs[6])],
             [(ys[6], xs[6]), (ys[2], xs[2])],
             [(ys[6], xs[6]), (ys[7], xs[7])],
             [(ys[7], xs[7]), (ys[8], xs[8])],
             [(ys[8], xs[8]), (ys[9], xs[9])],
             [(ys[10], xs[10]), (ys[11], xs[11])],
             [(ys[11], xs[11]), (ys[12], xs[12])],
             [(ys[12], xs[12]), (ys[ 7], xs[ 7])],
             [(ys[ 7], xs[ 7]), (ys[13], xs[13])],
             [(ys[14], xs[14]), (ys[13], xs[13])],
             [(ys[14], xs[14]), (ys[15], xs[15])]]

    lc = mc.LineCollection(lines, colors=c,linewidths=2)
    ax.add_collection(lc)

    plt.show()


    result["frames"][idx] = joints.numpy().tolist()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print(result)

with open(name+'.json', 'w') as f:
    json.dump(result, f)

cap.release()
cv2.destroyAllWindows()
