# lst = ['a', 1, 'bc', 1, True]
# result = lst.pop()
# print(lst)
# print(result)


# lst = ['a', 1, 'bc', 1, True]
# result = lst.pop(2)
# print(lst)
# print(result)


# lst = ['a', 1, 'bc', 1, True]
# result = lst.pop('a')
# print(lst)
# print(result)


# lst = ['a', 1, 'bc', 1, True]
# lst.reverse()
# print(lst)


# lst = [5, 2, 7, 4, 87, 3]
# lst.sort()
# print(lst)
# lst.sort(reverse=True)
# print(lst)


# lst = [5, 2, 7, 4, 87, 3]
# print(sorted(lst))
# print(lst)
# print(sorted(lst, reverse=True))


# lst = [1, 2, 3, 4, 1, 5, 6]
# print(lst.count(1))


lst = [34, 46, 1, 77, 22, 8, 2, 88, 64, 9]
for i in range(0, len(lst) - 1):
	for j in range(i + 1, len(lst)):
		if lst[i] > lst[j]:
			temp = lst[i]
			lst[i] = lst[j]
			lst[j] = temp
print(lst)


lst = [34, 46, 1, 77, 22, 8, 2, 88, 64, 9]
for i in range(0, len(lst) - 1):
	for j in range(0, len(lst) - 1 - i):
		if lst[j] > lst[j + 1]:
			temp = lst[j]
			lst[j] = lst[j + 1]
			lst[j + 1] = temp
print(lst)




