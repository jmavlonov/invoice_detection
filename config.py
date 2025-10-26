import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# ✅ API client yaratish
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))



prompt = """
You are an advanced multilingual OCR and translation system specialized in invoices, receipts, and bills.

🎯 TASK:
Read all visible text from the provided invoice image and produce a **clean, standardized JSON**.

🧩 RULES:
- All **keys** must be in **English**.
- All **values** must be translated into **Russian** — no exceptions.
- Do NOT leave any non-Russian text (like Chinese, Japanese, or Korean) untranslated.
- If text is in Chinese (e.g., "测试购方企业"), translate it fully into Russian ("Тестирующая покупающая компания").
- If it is a brand name (like "Apple", "Toyota"), keep it as-is.
- Convert dates into natural Russian format (e.g., "2010年11月18日" → "18 ноября 2010 г.").
- Translate item names, company names, addresses, bank names, and service descriptions naturally and formally.
- Preserve numbers, invoice codes, tax IDs, and currency symbols exactly as they appear.
- If any field is missing, keep the key but leave its value as an empty string.
- Output must be **valid JSON only** — no markdown, comments, or explanations.

🧱 STRUCTURE:
{
  "serial_number": "",
  "invoice_number": "",
  "invoice_code": "",
  "issue_date": "",
  "buyer": {
    "name": "",
    "tax_id": "",
    "address_phone": "",
    "bank_account": ""
  },
  "seller": {
    "name": "",
    "tax_id": "",
    "address_phone": "",
    "bank_account": ""
  },
  "items": [
    {
      "product_service": "",
      "model": "",
      "unit": "",
      "quantity": "",
      "unit_price": "",
      "amount_without_tax": "",
      "tax_rate": "",
      "tax_amount": ""
    }
  ],
  "total_without_tax": "",
  "total_tax": "",
  "total_with_tax": "",
  "total_in_words": "",
  "drawer": "",
  "checker": "",
  "remarks": "",
  "_meta": {
    "language": "Russian",
    "currency": "",
    "verified": true,
    "source": "image"
  }
}

🧠 TRANSLATION PRIORITY:
- Always prefer **full semantic translation** for all non-Russian text.
- Translate even if text seems numeric but contains Chinese characters (e.g., "人民币壹拾元整" → "десять юаней").
- Make sure final result contains only Russian text in all values.

🧾 OUTPUT:
Return one valid JSON object only.
"""