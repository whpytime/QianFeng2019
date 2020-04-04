# s1 = 'this is a test of Python'
# findStr = 'test'
# s2 = s1[s1.find(findStr):s1.find(findStr)+len(findStr)]
# print(s2)


# lst1 = ['a', 'b']
# lst2 = ['c', 'd']
# lst1.insert(1, lst2)
# print(lst1)


# a = 'dfADF34dfg5dsfafDR45DFGdfDfd5sdfdds'
# newA = ''
# for i in a:
# 	if i >='a' and i <= 'z':
# 		newA += i.upper()
# 	elif i >= 'A' and i <= 'Z':
# 		newA += i.lower()
# 	else:
# 		newA += i
# print(newA)


# a = 'dfADF34dfg5dsfafDR45DFGdfDfd5sdfdds'
# for index, val in enumerate(a):
# 	if val >= 'a' and val <= 'z':
# 		tempList = list(a)
# 		tempList[index] = val.upper()
# 		a = ''.join(tempList)
# 	elif val >= 'A' and val <= 'Z':
# 		tempList = list(a)
# 		tempList[index] = val.lower()
# 		a = ''.join(tempList)
# 	else:
# 		pass
# print(a)


# a = 'dfADF34dfg5dsfafDR45DFGdfDfd5sdfdDs'
# for index, val in enumerate(a):
# 	if val >= 'a' and val <= 'z':
# 		a = a[:index] + val.upper() + a[index + 1:]
# 	elif val >= 'A' and val <= 'Z':
# 		a = a[:index] + val.lower() + a[index + 1:]
# 	else:
# 		pass
# print(a)


# a = 'abc'
# print(a[len(a):])


s = 'abc'
s1 = 'def'
lst = ['g', 'h', 'i']
print(s.join(s1))
print(s.join(lst))



