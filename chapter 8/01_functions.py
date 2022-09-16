# 1st function 
# marks1 = [45, 54, 65, 45]
# percentage1 = ((marks1[0]+marks1[1]+marks1[2]+marks1[3])/400)*100      #1st method sum

# marks2 = [54, 64, 75, 44]
# percentage2 = (sum(marks2)/400)*100        #2nd method sum
# print(percentage1, percentage2)

# 2nd and easy function

def percent(marks):
    return((sum(marks)/400)*100 )
marks1 = [45, 54, 65, 45]
percentage1 = percent(marks1)

marks2 = [54, 64, 75, 44]
percentage2 = percent(marks2)

print(percentage1, percentage2)

