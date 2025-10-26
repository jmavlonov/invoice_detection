from ocr.extractor import extract_invoice_raw
from stamp.detector import detect_stamp_in_invoice
from stamp.ordering import analyze_stamp_ordering
from utils.file_utils import save_json

def extract_invoice_data(image_path, target_language="ru"):
    print(f"🔍 Processing invoice: {image_path}")

    result = extract_invoice_raw(image_path)
    stamp_result = detect_stamp_in_invoice(image_path)

    if stamp_result.get("seal_detected"):
        ordering_result = analyze_stamp_ordering(image_path)
        stamp_result.update(ordering_result)

        if ordering_result["ordering"] == "stamp_on_top":
            stamp_result["authenticity"] = "likely_genuine"
            stamp_result["authenticity_score"] = 0.9
        elif ordering_result["ordering"] == "text_on_top":
            stamp_result["authenticity"] = "likely_fake"
            stamp_result["authenticity_score"] = 0.8
        else:
            stamp_result["authenticity"] = "uncertain"
            stamp_result["authenticity_score"] = 0.5
    else:
        stamp_result["authenticity"] = "no_stamp_detected"
        stamp_result["authenticity_score"] = 0.0

    result["stamp_analysis"] = stamp_result
    save_json(result, image_path, target_language)
