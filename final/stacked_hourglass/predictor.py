import torch

from stacked_hourglass.datasets.mpii import Mpii
from stacked_hourglass.utils.evaluation import final_preds_untransformed
from stacked_hourglass.utils.imutils import resize
from stacked_hourglass.utils.transforms import color_normalize, fliplr, flip_back


def _check_batched(images):
    if isinstance(images, (tuple, list)):
        return True
    if images.ndimension() == 4:
        return True
    return False


class HumanPosePredictor:
    def __init__(self, model, device=None):
        if device is None:
            device = 'cuda' if torch.cuda.is_available() else 'cpu'
        device = torch.device(device)
        model.to(device)
        self.model = model
        self.device = device

    def do_forward(self, input_tensor):
        self.model.eval()
        with torch.no_grad():
            output = self.model(input_tensor)
        return output

    def prepare_image(self, image):
        was_fixed_point = not image.is_floating_point()
        image = torch.empty(image.shape, device='cpu', dtype=torch.float32).copy_(image)
        if was_fixed_point:
            image /= 255.0
        if image.shape[-2:] != (256, 256):
            image = resize(image, 256, 256)
        image = color_normalize(image, Mpii.RGB_MEAN, Mpii.RGB_STDDEV)
        return image

    def estimate_heatmaps(self, images, flip=False):
        is_batched = _check_batched(images)
        raw_images = images if is_batched else images.unsqueeze(0)
        input_tensor = torch.empty((len(raw_images), 3, 256, 256),
                                   device=self.device, dtype=torch.float32)
        for i, raw_image in enumerate(raw_images):
            input_tensor[i] = self.prepare_image(raw_image)
        heatmaps = self.do_forward(input_tensor)[-1].cpu()
        if flip:
            flip_input = fliplr(input_tensor.cpu().clone().numpy())
            flip_input = torch.as_tensor(flip_input, device=self.device, dtype=torch.float32)
            flip_heatmaps = self.do_forward(flip_input)[-1].cpu()
            heatmaps += flip_back(flip_heatmaps)
            heatmaps /= 2
        if is_batched:
            return heatmaps
        else:
            return heatmaps[0]

    def estimate_joints(self, images, flip=False):
        """Estimate human joint locations from input images.

        Images are expected to be centred on a human subject and scaled reasonably.

        Args:
            images: The images to estimate joint locations for. Can be a single image or a list
                    of images.
            flip (bool): If set to true, evaluates on flipped versions of the images as well and
                         averages the results.

        Returns:
            The predicted human joint locations.
        """
        is_batched = _check_batched(images)
        raw_images = images if is_batched else images.unsqueeze(0)
        heatmaps = self.estimate_heatmaps(raw_images, flip=flip).cpu()
        coords = final_preds_untransformed(heatmaps, (64, 64))
        # Rescale coords to pixel space of specified images.
        for i, image in enumerate(raw_images):
            coords[i, :, 0] *= image.shape[-1] / 64
            coords[i, :, 1] *= image.shape[-2] / 64
        if is_batched:
            return coords
        else:
            return coords[0]
