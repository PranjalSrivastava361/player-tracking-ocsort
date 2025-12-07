from detectors.base_detector import BaseDetector
from tracking.base_tracker import BaseTracker
from pipeline.player_tracking_pipeline import PlayerTrackingPipeline

class DummyDetector(BaseDetector):
    def load_model(self): pass
    def detect(self, frame): return []

class DummyTracker(BaseTracker):
    def update(self, detections): return []
    def reset(self): pass

if __name__ == "__main__":
    detector = DummyDetector()
    tracker = DummyTracker()

    pipeline = PlayerTrackingPipeline(detector, tracker)
    print("Pipeline initialized successfully!")
