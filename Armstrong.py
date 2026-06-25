num= input("Enter a number:")


length=len(num)

num1=int(num)
num2=int(num)

# print(length)
sum=0
for i in range (0,length):
    sum += (num1%10)**length
    num1//=10
# print(sum)

if sum==num2:
    print(num , "is a Armstrong Number")
else:
    print(num, "is not an Armstrong Number")