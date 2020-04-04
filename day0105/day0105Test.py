# sum = 0
# for i in range(1, 51):
#     if i % 2 == 0:
#         sum += i
# print(sum)
# print(i)


# s1 = 'abc'
# s2 = "abc"
# s3 = '''
# abc
# '''
# print(s1 == s2)
# print(s1 is s2)
# print(s2 == s3)
# print(s2 is s3)


# s4 = input('请输入：')
# s5 = input('请输入：')
# print(s4 == s5)
# print(s4 is s5)


# s1 = 'abc'
# s2 = "abc"
# print(s1 + s2)
# print(s1 * 3)


# s1 = 'abcde'
# print('bc' in s1)
# print('ac' not in s1)


# name = 'steven'
# say = '一定要好好学习！'
# print('%s说：%s' % (name, say))
# print('你好%s！' % name)
# print('%s说：\"好好学习！\"' % name)
# print(r'%s说：\"好好学习！\"' % name)


# fileName = 'picture.png'
# print(fileName[5])
# print(fileName[1:5])
# print(fileName[:fileName.find('.')])
# print(fileName[fileName.find('.'):])
# print(fileName[-5:-1])
# print(fileName[5:1:-1])


# str1 = 'hello world'
# print(str1[-1:-6:-1])
# print(str1[0:5])
# print(str1[::-1])
# print(str1[4:1:-1])
# print(str1[2:8])


# str1 = 'abcdefg'
# print(str1.center(1, ','))
# print(str1.capitalize())


# str1 = 'aBc def ghij klm n'
# print(str1.capitalize())
# print(str1.title())
# str1.ist


# import random
#
# s = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'
# key = ''
# i = 0
# while i < 4:
# 	num = random.randint(0, len(s) - 1)
# 	key += s[num]
# 	i += 1
# print(key)


# url = 'https://www.baidu.com/img/bd_logo1.png?where=super'
# name = url[url.rfind('/') + 1: url.rfind('?')]
# print(name)
# print()


# str1 = 'aBc def ghij klm n'
# print(str1.replace(' ', '#'))




# msg = '认真学习！'
# result = msg.encode('utf-8')
# print(result)
# m = result.decode('utf-8')
# print(m)
#
# result1 = msg.encode('gbk')
# print(result1)
# m1 = result1.decode('gbk')
# print(m1)


# str1 = 'aBc def ghij klm n'
# print(str1.startswith('a'))
# print(str1.endswith('m'))


# path = ''
# while True:
# 	path = input('请输入要上传的文件路径：')
# 	if path.endswith('txt') or path.endswith('jpg') or path.endswith('png'):
# 		print('上传成功')
# 		break
# 	else:
# 		print('请重新输入：')


# oldStr = 'abc'
# newStr = '-'.join(oldStr)
# print(newStr)



# lst = ['a', 'b', 'c', '1']
# result = ''.join(lst)
# print(result)

# result = ''
# for i in lst:
# 	result += i
# print(result)



# str1 = 'aBc def ghij klm n'
# result = str1.split(' ')
# print(result)
# result2 = str1.split(' ', 10)
# print(result2)












