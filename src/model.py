import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision.models import efficientnet_b4


class BaseModule(nn.Module):
    def save(self, path):
        torch.save(self.state_dict(), path)

        return

    def load(self, path):
        checkpoint = torch.load(path)
        self.load_state_dict(checkpoint)

        return


class EfficientNet_b4(BaseModule):
    def __init__(self, num_classes=219):
        super(EfficientNet_b4, self).__init__()
        self.model = efficientnet_b4(pretrained=True)
        self.model.classifier[1] = torch.nn.Linear(
            self.model.classifier[1].in_features, num_classes)

    def forward(self, inputs, *args, **kwargs):
        outputs = self.model(inputs)

        return outputs


class MCEfficientNet_b4(BaseModule):
    def __init__(self, num_classes=219):
        super(MCEfficientNet_b4, self).__init__()
        model = efficientnet_b4(pretrained=True)
        model.classifier[1] = torch.nn.Linear(
            model.classifier[1].in_features, num_classes)
        model_child = list(model.children())
        self.feature_extr = nn.Sequential(*model_child[:-2])
        self.avgpool = model_child[-2]
        self.classifier = model_child[-1]

    def forward(self, inputs, training=False, *args, **kwargs):
        feature = self.feature_extr(inputs)
        x = self.avgpool(feature)
        x = x.view(x.size(0), -1)
        outputs = self.classifier(x)

        if training:
            return outputs, feature

        else:
            return outputs

if __name__ == '__main__':
    model = MCEfficientNet_b4(219)
    #print(model)