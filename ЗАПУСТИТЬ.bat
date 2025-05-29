@echo off
python yandex_reviews_parser.py
git add reviews.json
git commit -m "обновлены отзывы"
git push origin main
pause