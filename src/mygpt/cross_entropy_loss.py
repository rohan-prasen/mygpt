"""Python module to initialize the `Cross Entropy Loss function with Softmax` to train myGPT."""

import numpy as np


class CrossEntropyWithSoftmax:
    """Python class to hand out the contract to initialize cross entropy loss method for any object."""

    def __init__(self):
        self.lse = None
        self.logit_flat = None
        self.labels_flat = None

    def forward(self, logits, labels):
        assert len(logits.shape) == 3
        B, T, V = logits.shape

        np.reshape(logits, (B * T), V)
        np.reshape(labels, (B * T))
