# list is a collection of non repeating value
b= set()
print(type(b))


# adding values to an empty set
b.add(4)
b.add(7)
b.add(9)
b.add(5)
b.add(5) # adding a value repeatedly does not changes a set 
b.add((1, 2, 3,))

# b.add({4:5 }) # cannot add list or dictionary to set 

# length of the set 
print(b)
print(len(b)) #print the length of the set 

#removal of the item 
b.remove(5) # remove 5 from set b
#b.remove(15) # throws an error while trying to remove 15 which is not present in the set 
print(b)

print(b.pop()) #remove any number 
print(b)