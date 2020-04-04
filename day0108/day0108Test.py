# t1 = ()
# print(type(t1))
# t2 = (1)
# print(type(t2))
# t3 = ('abc')
# print(type(t3))
# t4 = (1,)
# print(type(t4))
# t5 = ('a',)
# print(type(t5))


# t1 = (1, 'a', 'bc', True, [1, 'd'])
# print(t1)


# lst = [2, 'e', False]
# t2 = tuple(lst)
# print(t2)


# t1 = (1, 'a', 'bc', True, [1, 'd'])
# print(t1[1])
# print(t1[2:3])
# print(t1[2:4])


# t = (11, 5, 2, 77, 34, 0, 0)
# print(max(t))
# print(min(t))
# print(sum(t))
# print(len(t))
# print(t.count(3))
# print(t.index(77))
# print(t.index(3))


# t = (3, 6, 1, 5)
# a, b, c, d = t
# print(a, b, c, d)
# e = t
# print(e)


# t = (1, 2, 3, 4)
# a, *b, c = t
# print(a, b, c)
# x, y, *z = t
# print(x, y, z)


# t = (1, 2)
# x, y, *z, *a = t
# print(x, y, z, a)


# lst = [1, 2, 3]
# a, b, c = lst
# print(a, b, c)
# x, *y = lst
# print(x, y)


# st = '123'
# a, b, c = st
# print(a, b, c)
# x, *y = st
# print(x, y)
# print(type(a))
# print(type(y))


# t = (1, 2)
# a, *b = t
# print(a, b)
# print(type(a))
# print(type(b))


# t = (1, 2, 3)
# *x = t
# print(x)


# print(*[1, '2', 3])


# *x = [1, 2]
# print(x)


# lst = [(1, 11), (2, 22)]
# dict1 = dict(lst)
# print(dict1)


# dic = {}
# dic['a'] = 1
# dic['b'] = '2'
# print(dic)
# dic['b'] = 3
# print(dic)


# dic = {}
# while True:
# 	username = input('请输入用户名：')
# 	pwd = input('请输入密码：')
# 	if 'q' == username:
# 		break
# 	elif username in dic:
# 		print('该用户已经存在！')
# 	else:
# 		dic[username] = pwd
# print(dic)


# dic = {1: 'a', 2: 'b', 3: 'c'}
# print(dic[2])
# print(dic[4])


# dic = {'a': 100, 'b': 89, 'c': 90}
# for key in dic:
# 	if 'c' == key:
# 		print(key, dic[key])


# dic = {'a': 100, 'b': 89, 'c': 90, 'd': 95}
# for key in dic:
# 	if dic[key] > 90:
# 		print(key, dic[key])


# dic = {'aa': 100, 'bb': 89, 'cc': 90, 'dd': 95}
# for key, value in dic.items():
# 	if value > 90:
# 		print(key, value)


# dic = {'aa': 100, 'bb': 89, 'cc': 90, 'dd': 95}
# # print(dic.values())
# for value in dic.values():
# 	print(value, end=',')


# dic = {'aa': 100, 'bb': 89, 'cc': 90, 'dd': 95}
# sum = sum(dic.values())
# avg = sum / len(dic)
# print(avg)


# dic = {'aa': 100, 'bb': 89, 'cc': 90, 'dd': 95}
# print('aa' in dic)


# dic = {'aa': 100, 'bb': 89, 'cc': 90, 'dd': 95}
# print(dic.get('aa'))
# print(dic.get('ee'))
# print(dic.get('ee', 0))


# dic = {'aa': 100, 'bb': 89, 'cc': 90, 'dd': 95}
# result = dic.pop('bb')
# print(dic)
# print(result)
# result1 = dic.pop('ee', '字典中没有该key值')
# print(dic)
# print(result1)


# dic1 = {'aa': 100, 'bb': 89}
# dic2 = {'aa': 90, 'cc': 90}
# dic1.update(dic2)
# print(dic1)


# lst = [1, 'aa', 'b']
# result = dict.fromkeys(lst)
# print(result)


# t = [1, 'aa', 'b']
# result = dict.fromkeys(t, 0)
# print(result)


# st = 'abc'
# result = dict.fromkeys(st, '字符')
# print(result)


# k = 1
# result = dict.fromkeys(k)
# print(result)


# t = (1, 'a', True, [2, 'b'], (3, 'c'))
# t[3][0] = 'bb'
# print(t)


dic = {1: 'a', 'b': 2}
for i in dic.items():
	print(i)
print(type(i))
print(dic.items())




