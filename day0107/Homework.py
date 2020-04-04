# 1
# lst = [1, 1, 2, 1, 'a', 'a', 'b', 2, 'a']
# length = len(lst)
# i = 0
# while i < length - 1:
# 	j = i + 1
# 	while j < length:
# 		if lst[i] == lst[j]:
# 			lst.pop(j)
# 			length -= 1
# 		else:
# 			j += 1
# 	i += 1
# print(lst)


# 2
# names = []
# while True:
# 	name = input('请输入：')
# 	if 'q' == name:
# 		break
# 	else:
# 		# i = 0
# 		# while i < len(names):
# 		# 	if names[i] == name:
# 		# 		print('此姓名已经存在')
# 		# 		break
# 		# 	else:
# 		# 		i += 1
# 		# if i == len(names):
# 		# 	names.append(name)
#
# 		flag = 0
# 		for i in names:
# 			if i == name:
# 				print('此姓名已经存在')
# 				flag = 1
# 				break
# 		if flag == 0:
# 			names.append(name)
# print(names)


# 3
# lst1 = [1, 5, 7, 9]
# lst2 = [2, 2, 6, 8]
# lst1.extend(lst2)
# print(lst1)
# for i in range(0, len(lst1) - 1):
# 	for j in range(i + 1, len(lst1)):
# 		if lst1[i] > lst1[j]:
# 			lst1[i], lst1[j] = lst1[j], lst1[i]
# print(lst1)


# 4
# lst = [[6, 2], [8, 4, 2], [5, 6, 1]]
# newLst = []
# for i in lst:
# 	newLst.extend(i)
# print(newLst)
# for i in range(0, len(newLst) - 1):
# 	for j in range(i + 1, len(newLst)):
# 		if newLst[i] > newLst[j]:
# 			newLst[i], newLst[j] = newLst[j], newLst[i]
# print(newLst)


# 5
names = []
while True:
	print('=' * 6, '通讯录管理系统', '=' * 6)
	print('1.增加姓名和手机')
	print('2.删除姓名')
	print('3.修改手机')
	print('4.查询所有用户')
	print('5.根据姓名查找手机号')
	print('6.退出')
	choice = input('请选择：')

	# 6.退出
	if choice == '6':
		print('退出系统')
		break

	# 1.增加姓名和手机
	elif choice == '1':
		while True:
			e = input('请输入：')
			if 'q' == e:
				break
			else:
				name = e.split(',')
				flag = 0
				for i in names:
					if name[0] == i[0]:
						print('已经存在该用户')
						flag = 1
						break
				if flag == 0:
					names.append(name)

	# 2.删除姓名
	elif choice == '2':
		while True:
			delName = input('请输入要删除的姓名：')
			if 'q' == delName:
				break
			else:
				flag = 0
				for i in names:
					if delName == i[0]:
						names.remove(i)
						flag = 1
						print('已经删除{}'.format(delName))
						break
				if flag == 0:
					print('未找到姓名{}'.format(delName))

	# 3.修改手机
	elif choice == '3':
		while True:
			changeNames = input('请输入要修改手机号的姓名：')
			changeName = changeNames.split(',')
			if 'q' == changeName[0]:
				break
			else:
				flag = 0
				for i in names:
					if changeName[0] == i[0]:
						i[1] = changeName[1]
						flag = 1
						print('已经修改姓名{}的手机号'.format(changeName[0]))
				if flag == 0:
					print('未找到{}'.format(changeName[0]))

	# 4.查询所有用户
	elif choice == '4':
		for i in names:
			print(i)


	# 5.根据姓名查找手机号
	elif choice == '5':
		while True:
			findName = input('请输入查找的姓名：')
			if 'q' == findName:
				break
			else:
				flag = 0
				for i in names:
					if findName == i[0]:
						print('姓名：{}，手机号：{}'.format(i[0], i[1]))
						flag = 1
						break
				if flag == 0:
					print('未找到{}'.format(findName))
