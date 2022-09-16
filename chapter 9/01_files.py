# use open function to read the content of a file
# f = ujjwal is a good boy
# And he is the best
f = open('sample.txt', 'r')  # by default the mode is 'r'
data = f.read()
# data = f.read(5) #read first five character from the file
print(data)
f.close()
