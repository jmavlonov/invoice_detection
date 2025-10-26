import cv2
import numpy as np
import pytesseract

def analyze_stamp_ordering(image_path):
    """Determine whether stamp is above or below text."""
    img = cv2.imread(image_path)
    if img is None:
        return {"ordering": "uncertain", "confidence": 0.0, "reason": "Image not found"}

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # OCR bounding boxes
    data = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
    text_mask = np.zeros(gray.shape, dtype=np.uint8)
    for i in range(len(data["text"])):
        conf_val = data["conf"][i]
        try:
            conf = float(conf_val)
        except (ValueError, TypeError):
            conf = -1
        if conf > 40:
            x, y, w, h = data["left"][i], data["top"][i], data["width"][i], data["height"][i]
            cv2.rectangle(text_mask, (x, y), (x + w, y + h), 255, -1)

    # Stamp mask
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_red1, upper_red1 = np.array([0, 50, 30]), np.array([10, 255, 255])
    lower_red2, upper_red2 = np.array([160, 50, 30]), np.array([179, 255, 255])
    mask1, mask2 = cv2.inRange(hsv, lower_red1, upper_red1), cv2.inRange(hsv, lower_red2, upper_red2)
    mask_red = cv2.bitwise_or(mask1, mask2)
    lower_blue, upper_blue = np.array([90, 40, 30]), np.array([140, 255, 255])
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    stamp_mask = cv2.bitwise_or(mask_red, mask_blue)

    # Overlap analysis
    overlap = cv2.bitwise_and(stamp_mask, text_mask)
    overlap_ratio = np.count_nonzero(overlap) / max(np.count_nonzero(stamp_mask), 1)

    # Edge analysis
    edges = cv2.Canny(gray, 100, 200)
    edges_overlap = cv2.bitwise_and(edges, overlap)
    edges_text = cv2.bitwise_and(edges, text_mask)
    ratio_edges = np.count_nonzero(edges_overlap) / max(np.count_nonzero(edges_text), 1)

    # Decision logic
    if ratio_edges > 0.35:
        ordering, confidence = "text_on_top", 0.85
    elif overlap_ratio > 0.15:
        ordering, confidence = "stamp_on_top", 0.8
    else:
        ordering, confidence = "uncertain", 0.5

    return {"ordering": ordering, "confidence": confidence}
