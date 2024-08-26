
tup = (1,2,3,4,5,6)
print(type(tup),tup)
tup2 = ("yaswanth",18,"student","NITPY")
print(type(tup2),tup2)
print(tup2[3])
print(tup2[0])
print(tup2[2])
tup3 = tup[1:4]
print(tup3)

#manipulating tuples
tup4 = ("january","august","june","july")
l = list(tup4)
l.append("november")
l.remove("january")
tup4 = tuple(l)
print(tup4)
print(tup4.count("june"))
print(len(tup4))