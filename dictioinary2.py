ep1 = {220:91,221:85,222:90,223:96}
ep2 = {210:98,211:86,212:76,213:69}

# ep1.update(ep2) #merges ep2 with ep1
print(ep1)
# ep1.clear() #clears the whole dictionary and while printing shows empty dictionary
# print(ep1)
ep1.pop(220)
print(ep1)
ep2.popitem()
print(ep2)
# del ep1 #deletes the whole dictionary
# del ep1(222) #deletes key 222 from ep1
