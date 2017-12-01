def lhs(a,b):
    equ= (a-b)**2
    return equ

def rhs(a,b):
    eq= (a**2)-(2*a*b)+(b**2)
    return eq

num_a = int(input("Enter a number"))
num_b = int(input("Enter second number"))
num1= lhs(num_a,num_b)
num2 = rhs(num_a,num_b)

if(num1==num2):
    print("Hence proved")
