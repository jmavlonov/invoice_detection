import re
import json
from config import client
from utils.image_utils import encode_image

def detect_stamp_in_invoice(image_path):
    """GPT orqali muhr bor/yo'qligini aniqlash"""
    image_base64 = encode_image(image_path)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert in document visual analysis. "
                    "Your task is to determine whether an invoice image contains a company stamp or seal. "
                    "Return strictly a JSON object with 'seal_detected': true or false."
                ),
            },
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Analyze this image and say if there is a visible company seal or stamp on it."},
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_base64}"}}
                ],
            },
        ],
    )

    content = response.choices[0].message.content.strip()
    if content.startswith("```"):
        content = re.sub(r"^```(json)?", "", content)
        content = re.sub(r"```$", "", content)
        content = content.strip()

    try:
        result = json.loads(content)
    except json.JSONDecodeError:
        result = {"seal_detected": None, "raw_output": content}

    return result
