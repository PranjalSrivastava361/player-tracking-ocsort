# tracking/base_tracker.py

from abc import ABC, abstractmethod
from typing import List, Dict, Any
import numpy as np


class BaseTracker(ABC):
    """
    Abstract base class for any Multi-Object Tracker.
    Defines the required interface for OC-SORT, Deep OC-SORT,
    or any custom tracker implementation.
    """

    @abstractmethod
    def initialize(self, **kwargs):
        """
        Initialize tracker parameters, buffers, and models.
        Called once before tracking begins.
        Example: load config, allocate Kalman filters, load ReID model.
        """
        pass

    @abstractmethod
    def update(self, detections: np.ndarray, frame_info: Dict[str, Any]):
        """
        Update tracker with detections from the current frame.

        Args:
            detections: np.ndarray of shape (N, 5) → [x1, y1, x2, y2, score]
            frame_info: additional info such as frame_id, timestamp, etc.

        Returns:
            A list/array of active tracked objects in format:
            [x1, y1, x2, y2, track_id]
        """
        pass

    @abstractmethod
    def reset(self):
        """
        Reset internal state of the tracker.
        Called when a new video starts.
        """
        pass

    @abstractmethod
    def get_active_tracks(self) -> List[Dict[str, Any]]:
        """
        Returns metadata about all active tracks.
        Useful for debugging or visualization.
        Example return:
            [
                {"id": 1, "bbox": [x1,y1,x2,y2], "age": 10},
                {"id": 2, "bbox": [..], "age": 4},
            ]
        """
        pass
