with open("log.txt") as f:
    content = f.read().lower()

if "python" in content:
    print("yes python is present")
else:
    print("python is not present")
