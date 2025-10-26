import base64

def encode_image(image_path):
    """Rasmni base64 formatga o'girish"""
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")
