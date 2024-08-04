import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)

if(timestamp<'12') : 
    print("gud mrng")
elif(timestamp<'18') :
    print("gud afternoon")
elif(timestamp<'22') :       
    print("gud evng")
else:
    print("gud nght")    