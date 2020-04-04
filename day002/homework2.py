# 2
# import os
#
# SHITOU = 1
# JIANDAO = 2
# BU = 3
#
# player1 = int(input("player1请输入选择："))
# os.system("cls")
# player2 = int(input("player2请输入选择："))
# os.system("cls")
#
# if player1 == SHITOU:
# 	if player2 == SHITOU:
# 		print("和局")
# 	if player2 == JIANDAO:
# 		print("player1赢了")
# 	if player2 == BU:
# 		print("player2赢了")
# if player1 == JIANDAO:
# 	if player2 == SHITOU:
# 		print("player2赢了")
# 	if player2 == JIANDAO:
# 		print("和局")
# 	if player2 == BU:
# 		print("player1赢了")
# if player1 == BU:
# 	if player2 == SHITOU:
# 		print("player1赢了")
# 	if player2 == JIANDAO:
# 		print("player2赢了")
# 	if player2 == BU:
# 		print("和局")


# 3
import random

amount = 100.00
PASSWORD = '123456'

pay = int(input("请输入支付金额："))
pwd = input("请输入支付密码：")
choice = ''
if PASSWORD == pwd and pay <= amount:
	choice = input("支付成功。是否参加\"摇一摇\"活动？")
	if 'y' == choice or 'Y' == choice:
		ran = random.random()
		if 0 == ran:
			print("免单！！")
			print("您的余额为：", amount, "元")
		else:
			print("减免折扣为", ran, "折")
			pay1 = pay * (1 - ran)
			print("减免了", pay1, "元，本次消费", pay - pay1, "元，余额为", amount - pay + pay1, "元")
	else:
		print("放弃参加\"摇一摇\"活动。")
		print("您消费了", pay, "元，您的余额为：", amount - pay, "元")
