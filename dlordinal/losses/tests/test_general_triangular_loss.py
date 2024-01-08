import numpy as np
import torch

from ..general_triangular_loss import GeneralTriangularCrossEntropyLoss


def test_general_triangular_loss_creation():
    # Generate 12 random values between 0.01 and 0.2
    alphas = np.array(
        [
            0.11073934,
            0.10117434,
            0.01966654,
            0.04475356,
            0.02453978,
            0.07121018,
            0.1535088,
            0.01083356,
            0.05561108,
            0.04605048,
            0.02095387,
            0.15887076,
        ]
    )

    num_classes = 6

    loss = GeneralTriangularCrossEntropyLoss(num_classes=num_classes, alphas=alphas)
    assert isinstance(loss, GeneralTriangularCrossEntropyLoss)


def test_general_triangular_loss_output():
    alphas = np.array(
        [
            0.11073934,
            0.10117434,
            0.01966654,
            0.04475356,
            0.02453978,
            0.07121018,
            0.1535088,
            0.01083356,
            0.05561108,
            0.04605048,
            0.02095387,
            0.15887076,
        ]
    )

    num_classes = 6

    loss = GeneralTriangularCrossEntropyLoss(num_classes=num_classes, alphas=alphas)

    input_data = torch.tensor(
        [
            [-1.6488, -2.5838, -2.8312, -1.9495, -2.4759, -3.4682],
            [-1.7872, -3.9560, -6.2586, -8.3967, -7.9779, -8.0079],
            [-2.4078, -2.5133, -2.5584, -1.7485, -2.3675, -2.6099],
        ]
    )
    target = torch.tensor([4, 0, 5])

    # Compute the loss
    output = loss(input_data, target)

    # Verifies that the output is a tensor
    assert isinstance(output, torch.Tensor)

    # Verifies that the loss is greater than zero
    assert output.item() > 0
