def main():
    with open("reviews.json", "w", encoding="utf-8") as f:
        f.write('{"status": "updated"}')
    print("reviews.json обновлён")

if __name__ == '__main__':
    main()
