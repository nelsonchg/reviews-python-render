import json

data = {"reviews": ["Great!", "Could be better.", "Excellent!"]}
with open("reviews.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("reviews.json обновлён")
