import cv2
import numpy as np
from detectors.base_detector import BaseDetector
from tracking.base_tracker import BaseTracker


class PlayerTrackingPipeline:
    """
    End-to-end pipeline for running:
    1. Detection (YOLO, etc.)
    2. Tracking (OC-SORT)
    3. Outputting tracked players with consistent IDs
    """

    def __init__(self, detector: BaseDetector, tracker: BaseTracker):
        """
        Initializes the tracking pipeline.

        Args:
            detector: Instance of a detector class
            tracker: Instance of a tracker class
        """
        self.detector = detector
        self.tracker = tracker

    def load_components(self):
        """Load detector + tracker components."""
        print("[INFO] Loading detector model...")
        self.detector.load_model()

        print("[INFO] Tracker initialized...")

    def run_on_video(self, video_path: str, output_path: str = None):
        """
        Run player tracking on a video file.

        Args:
            video_path: path to input sports video
            output_path: optional path to save the output visualized video
        """

        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            raise ValueError(f"Cannot open video: {video_path}")

        # Video writer if saving output
        writer = None
        if output_path:
            fps = cap.get(cv2.CAP_PROP_FPS)
            w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            writer = cv2.VideoWriter(
                output_path,
                cv2.VideoWriter_fourcc(*"mp4v"),
                fps, (w, h)
            )

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Step 1: Detect players
            detections = self.detector.detect(frame)  # Nx5

            # Step 2: Run OC-SORT tracking
            tracks = self.tracker.update(detections)

            # Step 3: Draw results
            output_frame = self._draw_tracks(frame, tracks)

            if writer:
                writer.write(output_frame)

            cv2.imshow("Player Tracking", output_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        if writer:
            writer.release()
        cv2.destroyAllWindows()

    def _draw_tracks(self, frame, tracks):
        """
        Draw bounding boxes & IDs on frame.
        tracks: Nx5 → [x1, y1, x2, y2, ID]
        """
        for x1, y1, x2, y2, track_id in tracks:
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)),
                          (0, 255, 0), 2)
            cv2.putText(frame, f"ID: {int(track_id)}",
                        (int(x1), int(y1)-5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6,
                        (0, 255, 0), 2)
        return frame

