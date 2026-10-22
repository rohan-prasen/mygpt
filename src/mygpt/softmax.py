"""Python module to implement Softmax for the library, `mygpt`."""

import numpy as np
import numpy.typing as npt


class Softmax:
    """Python class to create and lend out Softmax contract to other instances of this class."""

    def __init__(self):
        """Default constructor to instantiate instance variables for the Softmax class instances.

        Args:
        None.

        Returns:
        None. Just instantiates the instance variable for the class's instances.

        """
        self.softmax_out = None

    def forward(self, inputs: npt.NDArray[np.float64]) -> npt.NDArray[np.float64]:
        """The passing method which computes and calculates the softmax probabilities of a given input.

        Args:
        inputs (NDArray[float64]): An n-dimensional array of inputs in np.float64 format.

        Returns:
        An n-dimensional array of inputs in np.float64 format.

        """

        # Softmax is shift-invariant so we subtract max_logit for numerical stability
        max_logit = np.max(inputs, axis=-1, keepdims=True)

        # Softmax output
        softmax_out = np.exp(inputs - max_logit) / np.sum(
            np.exp(inputs - max_logit), axis=-1, keepdims=True
        )
        self.softmax_out = softmax_out

        return softmax_out
