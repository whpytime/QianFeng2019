# lst = ['a', 1, 'bc', 2, True, ['d', 'ef', 3]]
# print(lst[0])
# print(lst[1])
# print(lst[-1])

# for i in lst:
# 	print(i, end='')

# i = 0
# while True:
# 	if i < len(lst) - 1:
# 		print(lst[i], ', ', end='')
# 	else:
# 		print(lst[i])
# 		break
# 	i += 1


# lst = ['a', 1, 'bc', 2, True, ['d', 'ef', 3]]
# if 'bc' in lst:
# 	lst[lst.index('bc')] = '百度'
# print(lst)


# lst[2] = '百度'
# print(lst)


# for i in range(len(lst)):
# 	if type(lst[i]) == str:
# 		if 'bc' in lst[i]:
# 			lst[i] = '谷歌'
# print(lst)


# lst = ['a', 1, 'bc', 'b', True, ['d', 'ef', 3]]
# del lst[2]
# print(lst)

# tempList = []
# for i in lst:
# 	if 'bc' != i:
# 		tempList.append(i)
# print(tempList)


# lst = ['a', '1', 'b', 'bc', 'True']
# length = len(lst)
# i = 0
# while i < length:
# 	if 'b' in lst[i]:
# 		del lst[i]
# 		length -= 1
# 		continue
# 	i += 1
# print(lst)


# lst = ['a', 1, 'bc', 'b', True, ['d', 'ef', 3]]
# print(lst[2:5])
# print(lst[-1])
# print(lst[-1::-1])


# lst = []
# lst.append('a')
# lst.append(1)
# print(lst)


# lst = ['a', 'b']
# lst1 = ['c', 'd']
# str1 = 'efg'
# lst = lst + str1
# print(lst)


# lst = ['a', 'b']
# str1 = 'ef'
# lst.insert(3, str1)
# print(lst)


# lst = [2, 6, 3, 88, 35, 11]
# print(sorted(lst, reverse=True))


# lst = ['abc']
# print(lst)


# lst = ['a', 'b', 'c']
# for index, val in enumerate(lst):
# 	print(index, val)
#
#
# for index, val in enumerate(lst):
# 	if 'b' == val:
# 		lst[index] = 1
# print(lst)


# lst = ['a', 1, 'bc', 2, True, ['d', 'ef', 3]]
# for index, val in enumerate(lst):
# 	if type(val) == str:
# 		if 'b' in val:
# 			lst[index] = '谷歌'
# print(lst)


print([3] in [1, 2, [3]])



