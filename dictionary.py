dic={'name' : 'yaswanth','age': 18,'year':2,'eligibility':True}
print(dic)
# print(dic['name'])
# print(dic['age'])
# print(dic['year'])
# print(dic['eligibility'])
print(dic.get('name'))
print(dic.keys())
print(dic.values())
for key in dic.keys():
    print(dic[key])
# if dic['name'] is 'yaswanth':
#     print('name is yaswanth in the dictionary')
# else : 
#     print('name in the dictionary is not yaswanth')   
 