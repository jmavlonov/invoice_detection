import os
import json
from .json_utils import json_converter

def save_json(result, image_path, target_language="ru"):
    """Natijani JSON formatda saqlash"""
    os.makedirs("output_images", exist_ok=True)
    base_name = os.path.splitext(os.path.basename(image_path))[0]
    output_path = f"output_json_data/{base_name}_{target_language}.json"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=4, default=json_converter)

    print(f"✅ JSON saved to {output_path}")
