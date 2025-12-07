from abc import ABC, abstractmethod
from typing import Any
import numpy as np


class BaseDetector(ABC):
    """
    Abstract base class for all object detectors.
    Example detectors: YOLO, FasterRCNN, EfficientDet, etc.
    """

    @abstractmethod
    def load_model(self, **kwargs):
        """
        Load the pretrained detection model.
        Called once before inference begins.
        """
        pass

    @abstractmethod
    def detect(self, image: Any) -> np.ndarray:
        """
        Run detection on an input image.

        Args:
            image: Input frame (BGR/RGB array or tensor).

        Returns:
            detections: np.ndarray of shape (N, 5)
                Each row: [x1, y1, x2, y2, score]
        """
        pass

    @abstractmethod
    def preprocess(self, image: Any) -> Any:
        """
        Preprocess input image before sending to the model.
        Example: resizing, normalization, tensor conversion.
        """
        pass
