![Invoice Detection Logo](images/logo/invoice_logo.jpeg)

# 💼 Invoice Detection — Intelligent Invoice Analyzer

![build](https://badgen.net/badge/status/stable/green?icon=github)
![AI](https://badgen.net/badge/powered%20by/OpenAI-GPT4o/purple)
![python](https://badgen.net/badge/python/3.10+/blue)
![license](https://badgen.net/badge/license/MIT/yellow)

**Invoice Detection** is a lightweight AI-based Python project that automatically extracts structured data from invoice images, translates it, and verifies the presence and authenticity of company stamps.  
It combines OCR, image processing, and GPT-based vision analysis into one powerful yet easy-to-use tool.

---

## Installation

```shell
pip install -r requirements.txt
```

### Also, create a .env file and add your OpenAI API key:

```shell
OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXX
```


## How to use it

### Basic usage:
```python

from pipeline.extract_invoice import extract_invoice_data

image_path = "images/sample_invoice.webp"
target_language = "ru"

extract_invoice_data(image_path, target_language)
```

### After running:

```shell
python main.py
```

```bash
🔍 Processing invoice: sample_invoice.webp
📄 OCR + Translation completed.
✅ JSON saved to output_images/sample_invoice_ru.json
```

### Output json data :

```json
{
    "serial_number": "661618766971",
    "invoice_number": "50843024",
    "invoice_code": "033001600211",
    "issue_date": "1 апреля 2017 г.",
    "buyer": {
        "name": "Ханчжоу Тяньжань Газовая Группа ООО",
        "tax_id": "",
        "address_phone": "",
        "bank_account": ""
    },
    "seller": {
        "name": "Ханчжоу Айсинь Ханчжоу Тяньжань Информация ООО",
        "tax_id": "91330106555199156Q",
        "address_phone": "Ханчжоу, район Цзянган, улица Миньцзянь, 30, 0571-81029350",
        "bank_account": "Ханчжоу Банк, 1202000590090032278"
    },
    "items": [
        {
            "product_service": "Сервисный сбор",
            "model": "",
            "unit": "",
            "quantity": "10",
            "unit_price": "0.94393623",
            "amount_without_tax": "9.43",
            "tax_rate": "6%",
            "tax_amount": "0.57"
        }
    ],
    "total_without_tax": "¥9.43",
    "total_tax": "¥0.57",
    "total_with_tax": "¥10.00",
    "total_in_words": "",
    "drawer": "Айсиньчжу",
    "checker": "",
    "remarks": "",
    "_meta": {
        "language": "Russian",
        "currency": "¥",
        "verified": true,
        "source": "image"
    },
    "stamp_analysis": {
        "seal_detected": true,
        "ordering": "stamp_on_top",
        "confidence": 0.8,
        "authenticity": "likely_genuine",
        "authenticity_score": 0.9
    }
}
```


```bash

invoice_parser/
│
├── main.py                     # Entry point
├── config.py                   # Environment + OpenAI setup
│
├── utils/
│   ├── file_utils.py           # JSON saving logic
│   ├── image_utils.py          # Converts image to Base64
│   └── json_utils.py           # Converts NumPy types to JSON
│
├── ocr/
│   └── extractor.py            # GPT-4o OCR + translation
│
├── stamp/
│   ├── detector.py             # Detects whether a stamp exists
│   └── ordering.py             # Determines stamp/text layer order
│
├── pipeline/
│   └── extract_invoice.py      # Main pipeline orchestrator
│
├── images/                     # Folder for input invoice images
│   ├── sample_invoice.webp
│   ├── invoice_test1.jpg
│   └── invoice_test2.png
│
└── output_json_data/              # Folder for AI-generated JSON results
    ├── sample_invoice_ru.json
    ├── invoice_test1_ru.json
    └── invoice_test2_ru.json

```


## Features

 - 🤖 AI-based OCR & Translation with GPT-4o

 - 🖋️ Stamp Detection & Authenticity Analysis

 - 💾 Automatic JSON Export

 - 🧠 OpenCV + Tesseract Integration

 - ⚙️ Modular, Clean Architecture

 - 🧩 Expandable for Future AI Tasks


## License

 - This project is licensed under the MIT License.
 - Copyright © 2025
 - Developed by [Jasur Mavlonov]



 ### ⭐ If you find this project useful, please give it a Star on GitHub!
