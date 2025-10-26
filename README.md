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


```json
{
    "vendor": "ООО ТехноТрейд",
    "invoice_number": "INV-2045",
    "date": "2025-03-12",
    "total_amount": "3 200,00 ¥",
    "stamp_analysis": {
        "seal_detected": true,
        "ordering": "stamp_on_top",
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
└── pipeline/
    └── extract_invoice.py      # Main pipeline orchestrator


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
