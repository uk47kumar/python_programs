num =  int(input("Enter the number\n"))
for i in range(1, 11):
    # 1st method 
    #print(str(num) + "X" + str(i) + "=" + str(i*num))
    # second method 
    product = (11-i)*num
    print(f"{num}X{11-i}={product}")

