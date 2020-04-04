# 1
# month28 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# month29 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
# day = input("请输入日期：")
# dayFormat = day.split(".")
# dayYear = int(dayFormat[0])
# dayMonth = int(dayFormat[1])
# dayDay = int(dayFormat[2])
# count = 0
# if dayYear % 4 == 0 and dayYear % 100 != 0:
# 	temp = 0
# 	while dayMonth - 1 > temp:
# 		count += month29[temp]
# 		temp += 1
# else:
# 	temp = 0
# 	while dayMonth - 1 > temp:
# 		count += month28[temp]
# 		temp += 1
# count += dayDay
# print(count)


# 3
# receive = input("请输入计算式：")
# result = 0
# if '+' in receive:
# 	receiveList = receive.split('+')
# 	result = int(receiveList[0]) + int(receiveList[1])
# elif '-' in receive:
# 	receiveList = receive.split('-')
# 	result = int(receiveList[0]) - int(receiveList[1])
# elif '*' in receive:
# 	receiveList = receive.split('*')
# 	result = int(receiveList[0]) * int(receiveList[1])
# elif '/' in receive:
# 	receiveList = receive.split('/')
# 	if receiveList[1] != 0:
# 		result = int(receiveList[0]) / int(receiveList[1])
# print(result)




