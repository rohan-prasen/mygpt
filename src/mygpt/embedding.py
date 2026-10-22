"""Python module for the embedding layer of `mygpt`."""

from typing import Any

import numpy as np
import numpy.typing as npt


class EmbeddingLayer:
    """Python class for creating and lending out embedding model contract to different instances."""

    def __init__(self, vocab_size: int, embedding_dim: int) -> None:
        """Default constructor to instantiate instance variables for any object created for this class

        Args:
        vocab_size (int): The size of the input vocabulary for this model.
        embedding_dim (int): The number of dimensions that the embedding layer generates for the given input.

        Returns:
        None. Just Instantiates the instance variables for a class's instance.

        """
        self.embeddings = np.random.randn(vocab_size, embedding_dim) * 0.02
        self.inputs = None

        # Gradients
        self.grad_embeddings = np.zeros(self.embeddings.shape)

    def forward(self, inputs: Any) -> npt.NDArray[np.float64]:
        """Forward method that processes and passes the input data to the embedding numpy array

        Args:
        inputs (Any): Didn't figure out what the input is yet.

        Returns:
        embeddings[inputs] (NDArray[float64]). A n-dimensional array of numpy's 64bit float numbers. But the n-dimension would be the same as, `embedding_dimension`.

        """
        self.inputs = inputs
        return self.embeddings[inputs]

    # TODO: implement backward() and get_params() methods to complete the EmbeddingLayer implementation
