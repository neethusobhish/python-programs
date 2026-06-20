# Basic calculator using function

# addition
def add(num1,num2):
    return num1+num2

# substraction
def sub(num1,num2):
    return num1-num2

# multiplication
def mul(num1,num2):
    return num1*num2

# division
def div(num1,num2):
    return num1/num2

# exponentiation
def expo(num1,num2):
    return num1**num2

# floor division
def floor(num1,num2):
    return num1//num2

# modulus
def mod(num1,num2):
    return num1%num2

# pattern
def pattern(patern):
    for i in range(1,patern+1):
        for j in range (1,i+1):
            print(i ,' ', end='')
            i=i-1
        print()

def main():
    while True:
        patern=int(input("Enter your Number for pattern: "))
        pattern(patern)
        input(" Welcome to your calculator: ")
        num1= float(input("enter a number : "))
        num2= float(input("enter a number : "))
         
        
        opertn=int(input("enter your choice \n1.Addition\n2.substraction\n3.Multiplication\n4.Division\n5.Exponentiation\n6.Floor Division\n7.Modulus\n8.Exit \nChoose: "))


        if opertn==1:
            print("addition" ,add(num1,num2))
        elif opertn==2:
            print("substraction" ,sub(num1,num2))
        elif opertn==3:
            print("Multiplication" ,mul(num1,num2))
        elif opertn==4:
            print("Division" ,div(num1,num2))
        elif opertn==5:
            print("Exponential" ,expo(num1,num2))
        elif opertn==6:
            print("Floor Division" ,floor(num1,num2))
        elif opertn==7:
            print("Modulus" ,mod(num1,num2))
        elif opertn==8:
            break
        else:
            print("Your choice is wrong")
            
    
main()




