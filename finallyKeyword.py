try:
    l=[1,5,6,7]
    i=int(input("enter the number:"))
    print(l[i])
except  Exception as e:
    print(e)
finally:
    print("I am always executed")
#finally is used to print things which
#neccessaery to be printed after the try
#catch block even any exception is occured
