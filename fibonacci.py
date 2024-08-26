def fibbonacci(n):
    if n<=1 :
        return 1
    return fibbonacci(n-1)+fibbonacci(n-2)

#num = int(input("Enter a number to get its fibonacci series : "))
for i in range(5):
  print(fibbonacci(i))
