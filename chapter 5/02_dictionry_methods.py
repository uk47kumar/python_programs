mydict = {
   "fast": " In a quick manner",
   "ujjwal": "A coder",
   "Marks": [1, 2, 3],
   "anotherdict": {'ujjwal': 'player'}

}
#  dictionary methods 
# print(list(mydict.keys())) # print the keys of the dictionary
# print(mydict.values()) # print the values of the dictionary 
# print(mydict.items()) # print the(key, value)  for all content of the dictionary 
print(mydict)
mydict2 = {
     "ujjwal": "friend"
     }
mydict.update(mydict2) #update the dictionary by adding  key value pairs from update dict 
print(mydict)

print(mydict.get("ujjwal")) #print value associated with the key
print(mydict["ujjwal"]) #print value associated with the key

#the difference between .get and [ ] syntax in dictionary?
print(mydict.get("ujjwal2")) # return none as ujjwal2 is not present in the dictionary  
#print(mydict.get("ujjwal2") # return  an error as ujjwal2 is not present in the dictionary  