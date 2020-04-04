carList = []
while True:
	choice = input("请选择操作（1.入场  2.出场  3.查询  4.统计  5.退出）：")
	if '5' == choice:
		break
	elif '1' == choice:
		carIn = input("请输入进场车牌号：")
		carList.append(carIn)
		print(carIn + "入场了。")
	elif '2' == choice:
		carOut = input("请输入出场车牌号：")
		carList.remove(carOut)
		print(carOut + "出场了。")
	elif '3' == choice:
		carSearch = input("请输入查询的车牌号：")
		if carSearch in carList:
			print(carSearch + "在停车场内。")
		else:
			print(carSearch + "不在停车场内。")
	elif '4' == choice:
		print("停车场内共有%d辆车。" % (len(carList)))
	else:
		print("请重新选择操作！")


