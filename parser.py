# parser.py
# Замените этот код на ваш рабочий парсер отзывов с Яндекс.Карт
import json
from datetime import datetime

# Пример: обновить reviews.json тестовыми данными
sample_reviews = [
    {"author": "Иван", "text": "Отличная компания!", "date": str(datetime.now())},
    {"author": "Мария", "text": "Хороший сервис, спасибо!", "date": str(datetime.now())}
]

with open("reviews.json", "w", encoding="utf-8") as f:
    json.dump(sample_reviews, f, ensure_ascii=False, indent=2)
print("reviews.json обновлён")
