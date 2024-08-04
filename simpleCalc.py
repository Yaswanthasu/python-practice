'''
num1 = int(input("Enter a : "))
num2 = int(input("Enter b : "))

op = str(input("Enter any basic operator : "))

if op == "+"  :
        print(num1 + num2)
elif op == "-":
        print(num1-num2)
elif op == "*":               
        print(num1*num2)
elif op == "/":
        print(num1/num2)
else :
        print("You choosed wrong operator. Try again!")                 
'''
num = int(eval(input("Enter the calculation : ")))
print(num)        
