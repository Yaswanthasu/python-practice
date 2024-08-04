for i in range(5):
    print(i)
while(i<=10):
    i=i+1
    print(i)
match(i):
    case 10 :
        print("number is less than or equal to 10")    
    case 20 :
        print("number is equal to 20")
    case 30 :
        print("number is equal to 30") 
    case _:
        print("number is ", i)
