mydict = {  
    "pankha": "fan",
    "dabba": "box",
    "vastu": "item",

}
print("options are", mydict.keys())
a = input("enter the hindi word \n")
print("The meaning of your word is :", mydict[a])

#below line will not throw an error if the key is not present 
# in the dictionary

# print("The meaning of your word is :", mydict.get(a))
