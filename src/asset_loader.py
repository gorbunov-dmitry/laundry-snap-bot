import torch


class AssetLoader:

    ASSETS_PATH = 'assets\\'

    TEXTS_PATH = ASSETS_PATH + 'text\\'
    IMAGES_PATH = ASSETS_PATH + 'images\\'
    NN_PATH = ASSETS_PATH + 'nn\\'

    def load_text(self, file_name):
        with open(self.TEXTS_PATH + file_name, encoding='utf-8') as f:
            return f.read()

    def load_image(self, file_name):
        return open(self.IMAGES_PATH + file_name, 'rb')

    def load_nn_state(self, file_name):
        return torch.load(self.NN_PATH + file_name, torch.device('cpu'))
