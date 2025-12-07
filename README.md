# Player Tracking in Sports Videos Using OC-SORT  
### Assignment Submission – Multi-Object Tracking 

This project implements the **architecture, abstract classes, and pipeline design** for a real-time multi-object player tracking system based on **OC-SORT**, as required in the assignment.

Sports videos have high visual traffic — players frequently:
- cross each other  
- look very similar  
- move non-linearly  
- get partially or fully occluded  

To maintain **consistent player IDs across frames**, a robust multi-object tracker is required.

---



---

## Project Architecture

┌──────────────────────────┐
│      Input Video Frame    │
└──────────────┬───────────┘
               │
               ▼
┌──────────────────────────┐
│   1. Object Detection     │  (YOLOX)
│  - Detect players         │
│  - Output: boxes + score  │
└──────────────┬───────────┘
               │ detections
               ▼
┌──────────────────────────┐
│   2. Pre-processing       │
│  - Resize / scale boxes   │
│  - Filter low confidence  │
└──────────────┬───────────┘
               │ clean detections
               ▼
┌──────────────────────────┐
│   3. OC-SORT Tracker      │
│  - Kalman Filter (motion) │
│  - OCM: momentum from obs │
│  - OCR: recovery post-occ │
│  - OOS: smoothing         │
│  - Hungarian matching     │
└──────────────┬───────────┘
               │ tracked objects (ID + box)
               ▼
┌──────────────────────────┐
│   4. ID Assignment        │
│  - Consistent player IDs  │
│  - Handle re-appearance   │
└──────────────┬───────────┘
               │
               ▼
┌──────────────────────────┐
│   5. Visualization        │
│  - Draw boxes + IDs       │
│  - Optional output video  │
└──────────────┬───────────┘
               │
               ▼
        Final Tracked Output


