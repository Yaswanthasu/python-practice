a=input("Enter the number : ")
print(f'Multiplication tale of {a} is :')
try:
    for i in range (1,11):
     print(f'{int(a)} X {i} = {int(a)*i}')
except Exception as e:
    print('sorry some error occured')
    print(e)

print('End of the code')
