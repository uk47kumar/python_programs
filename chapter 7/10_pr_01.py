num =  int(input("Enter the number\n"))
for i in range(1, 11):
    # 1st method 
    #print(str(num) + "X" + str(i) + "=" + str(i*num))
    # second method 
    print(f"{num}X{i}={num*i}")

