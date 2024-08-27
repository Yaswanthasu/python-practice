dic={'name' : 'yaswanth','age': 18,'year':2,'eligibility':True}
print(dic)
# print(dic['name']) #this type is not prefferable that much
# print(dic['age'])
# print(dic['year'])
# print(dic['eligibility'])
print(dic.get('name')) #this method is more preferrable to access the dictionaries
print(dic.keys())
print(dic.values())
# for key in dic.keys():
#     print(f"The value corressponding to the key {key}is {dic[key]}")
# if dic['name'] is 'yaswanth':
#     print('name is yaswanth in the dictionary')
# else : 
#     print('name in the dictionary is not yaswanth')   
print(dic.items())
for key,value in dic.items() : 
    print(f"the corresponding value for {key} is {value} ")    