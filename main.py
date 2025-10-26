from pipeline.extract_invoice import extract_invoice_data

if __name__ == "__main__":
    image_path = "images/ms.jpg"
    target_language = "ru"
    extract_invoice_data(image_path, target_language)
