from PIL import Image
from numpy import array
from torch import zeros
from torch.nn import Linear
from torch.nn import Sigmoid
from torchvision.models import resnet34
from torchvision.transforms import ToTensor

from asset_loader import AssetLoader


class LabelsRecognizer:

    def __init__(self):
        self.loader = AssetLoader()
        self.text_labels = self.loader.load_text('labels_annotations.txt')
        self.text_labels = self.text_labels.splitlines()
        self.model = resnet34()
        num_features = self.model.fc.in_features
        self.model.fc = Linear(num_features, 41)
        state_dict = self.loader.load_nn_state('nn.pkl')
        self.model.load_state_dict(state_dict)
        self.model.eval()

    def get_labels(self, image_path):
        image = Image.open(image_path).convert('RGB').resize((128, 128))
        model_input = zeros((16, 3, 128, 128))
        model_input[0] = ToTensor()(image)
        model_output = self.model(model_input)
        indexes = Sigmoid()(model_output[0]) > 0.5
        result = array(self.text_labels)[indexes]
        return result.tolist()
