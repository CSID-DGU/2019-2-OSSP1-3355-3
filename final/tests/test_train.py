import pytest
import torch
from torch.optim import Adam
from torch.utils.data import DataLoader

from stacked_hourglass import hg1, hg2
from stacked_hourglass.datasets.mpii import Mpii
from stacked_hourglass.train import do_training_step, do_validation_step, do_validation_epoch

ALL_DEVICES = ['cpu']
# Add available GPU devices.
ALL_DEVICES.extend(f'cuda:{i}' for i in range(torch.cuda.device_count()))


@pytest.mark.parametrize('device', ALL_DEVICES)
def test_do_training_step(device):
    device = torch.device(device)
    model = hg2(pretrained=False)
    model = model.to(device)
    model.train()
    optimiser = Adam(model.parameters())
    inp = torch.randn((1, 3, 256, 256), device=device)
    target = torch.randn((1, 16, 64, 64), device=device)
    output, loss = do_training_step(model, optimiser, inp, target)
    assert output.shape == (1, 16, 64, 64)
    assert loss > 0


@pytest.mark.parametrize('device', ALL_DEVICES)
def test_do_validation_step(device):
    device = torch.device(device)
    model = hg2(pretrained=False)
    model = model.to(device)
    model.eval()
    inp = torch.randn((1, 3, 256, 256), device=device)
    target = torch.randn((1, 16, 64, 64), device=device)
    output, loss = do_validation_step(model, inp, target)
    assert output.shape == (1, 16, 64, 64)
    assert loss > 0


def test_do_validation_epoch(mpii_image_dir):
    if not torch.cuda.is_available():
        pytest.skip('requires CUDA device')

    device = torch.device('cuda', torch.cuda.current_device())
    model = hg1(pretrained=True)
    model = model.to(device)
    val_dataset = Mpii(mpii_image_dir, is_train=False)
    val_dataset.valid_list = val_dataset.valid_list[:32]
    val_loader = DataLoader(val_dataset, batch_size=8, shuffle=False, num_workers=2,
                            pin_memory=True)
    avg_loss, avg_acc, predictions = do_validation_epoch(val_loader, model, device, flip=False)
    assert avg_loss == pytest.approx(0.00014652813479187898, abs=1e-6)
    assert avg_acc == pytest.approx(0.8879464417695999, abs=1e-6)
