import re
import json
from config import client,prompt
from utils.image_utils import encode_image

def extract_invoice_raw(image_path):
    image_base64 = encode_image(image_path)

    response = client.chat.completions.create(
        model="gpt-4o", 
        temperature=0,
        messages=[
            {"role": "system", "content": "You extract and translate structured invoice data accurately."},
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
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
        result = {"raw_output": content}

    print("📄 OCR + Translation completed.")
    return result
