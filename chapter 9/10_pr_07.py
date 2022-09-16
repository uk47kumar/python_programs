content = True
i = 1

with open("log.txt") as f:
    while content:
        content = f.readline().lower()

        if "python" in content:
            print(content)
            print(f"yes python is present on line number {i}")
        i += 1
