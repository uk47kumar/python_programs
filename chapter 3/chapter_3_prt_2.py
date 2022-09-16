letter = '''Dear <|NAME|>,
Greetings,
You are selected!
for the Owner of the best coader
<|DATE|> 
'''
name = input("Enter your name\n")
date = input("Enter date\n")

letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)

print(letter)