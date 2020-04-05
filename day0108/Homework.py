# dic = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
# for i in dic.keys():
# 	print(i)

# for i in dic.values():
# 	print(i)

# for e in dic.items():
# 	print(e[0], e[1])

# for key, value in dic.items():
# 	print(key, value)

# dic['k4'] = 'v4'
# print(dic)

# dic.pop('k1')
# print(dic)

# result = dic.pop('k5', None)
# print(result)

# print(dic['k2'])

# dic = {'k1': 'v1', 'k2': 'v2', 'k3': 'v3'}
# dic2 = {'k1': 'v11', 'a': 'b'}
# dic2.update(dic)
# print(dic2)


# import random
#
# lst = []
# for c in range(100):
# 	lst.append(random.randint(20, 100))
# print(lst)
# lst.sort()
# print(lst)

# dic = {}
# for i in range(1, 16):
# 	dic[i] = i * i
# print(dic)

s = 'a b c ab a b a c a d'
lst = s.split(' ')
dic = {}
for e in lst:
	if e in dic.keys():
		dic[e] = dic.get(e) + 1
	else:
		dic[e] = 1
for key, value in dic.items():
	print(key, value)




