# this = "    ujjwal is a good boy    "
# print(this)
# print(this.strip())

def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()


this = "    ujjwal is a good boy    "
n = remove_and_split(this, "ujjwal")
print(n)
