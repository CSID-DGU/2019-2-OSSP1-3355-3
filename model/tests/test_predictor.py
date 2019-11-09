import pytest
import torch
from torch.testing import assert_allclose

from stacked_hourglass import HumanPosePredictor, hg2

ALL_DEVICES = ['cpu']
# Add available GPU devices.
ALL_DEVICES.extend(f'cuda:{i}' for i in range(torch.cuda.device_count()))


@pytest.mark.parametrize('device', ALL_DEVICES)
def test_do_forward(device, example_input):
    device = torch.device(device)
    model = hg2(pretrained=True)
    predictor = HumanPosePredictor(model, device=device)
    output = predictor.do_forward(example_input.to(device))
    assert len(output) == 2  # Expect one set of heatmaps per stack.
    heatmaps = output[-1]
    assert heatmaps.shape == (1, 16, 64, 64)


@pytest.mark.parametrize('device', ALL_DEVICES)
def test_prepare_image(device, man_running_image):
    device = torch.device(device)
    model = hg2(pretrained=True)
    predictor = HumanPosePredictor(model, device=device)
    orig_image = man_running_image.clone()
    image = predictor.prepare_image(orig_image)
    assert_allclose(orig_image, man_running_image)  # Input image should be unchanged.
    assert image.shape == (3, 256, 256)
    assert image.device.type == 'cpu'


@pytest.mark.parametrize('device', ALL_DEVICES)
def test_prepare_image_mostly_ready(device):
    # This test is for preparing an image which already has the correct dtype and size.
    device = torch.device(device)
    image_float32 = torch.empty((3, 256, 256), device=device, dtype=torch.float32).uniform_()
    model = hg2(pretrained=True)
    predictor = HumanPosePredictor(model, device=device)
    orig_image = image_float32.clone()
    image = predictor.prepare_image(orig_image)
    assert_allclose(image_float32, orig_image)  # Input image should be unchanged.
    assert image.shape == (3, 256, 256)
    assert image.device.type == 'cpu'


@pytest.mark.parametrize('device', ALL_DEVICES)
def test_estimate_heatmaps(device, man_running_image):
    device = torch.device(device)
    model = hg2(pretrained=True)
    predictor = HumanPosePredictor(model, device=device)
    heatmaps = predictor.estimate_heatmaps(man_running_image)
    assert heatmaps.shape == (16, 64, 64)


@pytest.mark.parametrize('device', ALL_DEVICES)
def test_estimate_joints(device, man_running_image, man_running_pose):
    device = torch.device(device)
    model = hg2(pretrained=True)
    predictor = HumanPosePredictor(model, device=device)
    joints = predictor.estimate_joints(man_running_image)
    assert joints.shape == (16, 2)
    assert_allclose(joints, man_running_pose, rtol=0, atol=20)


@pytest.mark.parametrize('device', ALL_DEVICES)
def test_estimate_joints_with_flip(device, man_running_image, man_running_pose):
    device = torch.device(device)
    model = hg2(pretrained=True)
    predictor = HumanPosePredictor(model, device=device)
    joints = predictor.estimate_joints(man_running_image, flip=True)
    assert joints.shape == (16, 2)
    assert_allclose(joints, man_running_pose, rtol=0, atol=20)


@pytest.mark.parametrize('device', ALL_DEVICES)
def test_estimate_joints_h36m(device, h36m_image, h36m_pose):
    device = torch.device(device)
    model = hg2(pretrained=True)
    predictor = HumanPosePredictor(model, device=device)
    joints = predictor.estimate_joints(h36m_image)
    assert joints.shape == (16, 2)
    assert_allclose(joints, h36m_pose, rtol=0, atol=15)


@pytest.mark.parametrize('device', ALL_DEVICES)
def test_estimate_joints_tensor_batch(device, h36m_image, h36m_pose):
    device = torch.device(device)
    model = hg2(pretrained=True)
    predictor = HumanPosePredictor(model, device=device)
    batch_size = 4
    joints = predictor.estimate_joints(h36m_image.repeat(batch_size, 1, 1, 1))
    assert joints.shape == (batch_size, 16, 2)
    assert_allclose(joints, h36m_pose.repeat(batch_size, 1, 1), rtol=0, atol=15)
