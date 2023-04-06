list1 = ['a','b','d','c']
list2 = ['p','r','q']
# Append
list1.append('e')
print(list1)
# Copy
x = list1.copy()
print(x)
# Count
list1.append(6)
print(list1.count(6))
print(list1)
# Extend
list3 = [20,30, 40, 50, 60]
list3.extend(list1)
print(list3)
# pop
print(list1.pop(2))
print(list1)
# reverse
list1.reverse()
print(list1)
# Sort
list4 = [200, 100, 300, 500, 400]
list4.sort()
print(list4)
# Insert
list1.insert(6,7)
list1.insert(4,5)
print(list1)
# Count
list1.count(4)
print(list1)
# Update
print(list1[4])
print(list1)

