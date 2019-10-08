# pytorch-stacked-hourglass

This is a fork of [bearpaw/pytorch-pose](https://github.com/bearpaw/pytorch-pose) which is modified
for use as a Python package.


## Usage

This library is designed to make including human pose estimation into an application as simple
as possible. Here's an example:

```python
from stacked_hourglass import HumanPosePredictor, hg2

# ...load image of a person into a PyTorch tensor...

model = hg2(pretrained=True)
predictor = HumanPosePredictor(model, device='cpu')
joints = predictor.estimate_joints(my_image_tensor, flip=True)
```

`joints` will be a 16x2 tensor representing joint locations in input image space.
The joints are ordered according to the MPII Human Pose dataset:

```python
from stacked_hourglass.datasets.mpii import MPII_JOINT_NAMES

for i, name in enumerate(MPII_JOINT_NAMES):
    print(i, name)

# 0 right_ankle   # 4 left_knee     # 8 neck            # 12 right_shoulder
# 1 right_knee    # 5 left_ankle    # 9 head_top        # 13 left_shoulder
# 2 right_hip     # 6 pelvis        # 10 right_wrist    # 14 left_elbow
# 3 left_hip      # 7 spine         # 11 right_elbow    # 15 left_wrist

print('Right elbow location: ', joints[MPII_JOINT_NAMES.index('right_elbow')])
```


## Example scripts


### Evaluation on the MPII validation set

Here's a quick example of evaluating the pretrained 2-stack hourglass model on the MPII Human
Pose validation set.

```bash
$ python scripts/evaluate_mpii.py --arch=hg2 --image-path=/path/to/mpii/images
```

Output:

```
Final validation PCKh scores:

  Head    Shoulder    Elbow    Wrist    Hip    Knee    Ankle    Mean
------  ----------  -------  -------  -----  ------  -------  ------
 96.15       94.89    88.14    83.78  87.43   82.19    77.87   87.33
```


### Train an 8-stack hourglass model

```bash
$ python scripts/train_mpii.py \
    --arch=hg8 \
    --image-path=/path/to/mpii/images \
    --checkpoint=checkpoint/hg8 \
    --epochs=220 \
    --train-batch=6 \
    --test-batch=6 \
    --lr=5e-4 \
    --schedule 150 175 200
```
