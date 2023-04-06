dict1 = {'a': 1, 'b': 2, 'c': 3}
print(dict1['a'])
print(dict1.items())
print((list(dict1.items()))[0])
# clear
dict1.clear()
print(dict1)
# get
dict1 = {'a': 1, 'b': 2, 'c': 3}
val = dict1.get('c')
print(val)
# items
print(list(dict1.items()))
print(list(dict1.items())[1][0])
# keys
print(dict1.keys())
print(list(dict1.keys()))
# values
print(dict1.values())
print(list(dict1.values())[1])
# pop
print(dict1.pop('a'))
print(dict1)
dict1['a'] = 1
print(dict1)
# update
dict1['a'] = 4
print(dict1)