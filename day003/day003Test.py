# 1
# count = 1
# while count <= 50:
# 	print(count)
# 	count += 1


# 2
# count = 1
# flag = 0
# while count <= 100:
# 	if count % 2 != 0:
# 		count += 1
# 		continue
# 	# else:
# 	# 	flag += 1
# 	# 	if flag != 0 and flag % 5 == 0:
# 	# 		print(count)
# 	# 	else:
# 	# 		print(count, end=", ")
# 	else:
# 		if count % 10 == 0:
# 			print(count)
# 		else:
# 			print(count, end=", ")
# 	count += 1


# 3
# count = 1
# sumNum = 0
# while count <= 100:
# 	if count % 2 == 0:
# 		count += 1
# 		continue
# 	else:
# 		sumNum += count
# 		count += 1
# print(sumNum)


# 4
# import random
#
# carNo = ''
# maxNo = 16
# count = 1
# while count <= maxNo:
# 	num = random.randint(0, 9)
# 	print(num)
# 	carNo = carNo + str(num)
# 	count += 1
# print(carNo)


# for i in range(2, 51, 2):
# 	print(i)


# num = 44
# while True:
# 	inputNum = int(input("请猜数字："))
# 	if num < inputNum:
# 		print("大了")
# 	elif num > inputNum:
# 		print("小了")
# 	else:
# 		print("猜对了！")
# 		break


# import random
#
# sum = 0
# count = 0
# while True:
# 	randomNum = int(random.random() * 100)
# 	print(randomNum)
# 	if randomNum == 0:
# 		break
# 	if randomNum % 15 == 0:
# 		sum += randomNum * 2
# 	else:
# 		sum += randomNum
# 	count += 1
# print("跳了%d步，跳了%d长" % (count, sum))
