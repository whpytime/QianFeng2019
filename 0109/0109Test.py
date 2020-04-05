# s1 = set()
# s2 = {}
# s3 = {1,}
# print(type(s1))
# print(type(s2))
# print(type(s3))


# lst = [2, 6, 3, 1, 6, 2, 4, 5]
# s1 = set(lst)
# print(s1)


# set1 = set()
# lst = [2, 'a']
# t = (3, 'b')
# dic = {4: 'a'}
# set2 = {5, 'c'}
# set1.add(1)
# set1.add('a')
# set1.add(1)
# # set1.add(lst)
# # set1.add(dic)
# # set1.add(set2)
# set1.add(t)
# print(set1)


# set1 = set()
# lst = [2, 'a']
# t = (3, 'b')
# dic = {4: 'a'}
# set2 = {5, 'c'}
# # set1.update(1)
# set1.update('a')
# print(set1)
# set1.update(lst)
# print(set1)
# set1.update(t)
# print(set1)
# set1.update(dic)
# print(set1)
# set1.update(set2)
# print(set1)


# set1 = {1, 'a', (2, 'b')}
# set1.remove('a')
# set1.remove('b')
# print(set1)
# set1.discard(2)
# print(set1)
# set1.pop()
# print(set1)
# set1.clear()
# print(set1)


# lst = [2, 6, 3, 1, 6, 2, 4, 5]
# s1 = set(lst)
# print(s1)
# lst = list(s1)
# print(lst)


# set1 = set()
# lst = [1, 'a']
# set1.update(lst)
# print(set1)
# lst2 = [1, [2, 'b']]
# set1.update(lst2)
# print(set1)


# import random
#
# set1 = set()
# while True:
# 	set1.add(random.randint(1, 20))
# 	if len(set1) == 10:
# 		break
# print(set1)


# set1 = {1, 'a'}
# print(1 in set1)
# print('a' not in set1)

# set2 = {2, 'b'}
# print(set1 == set2)
# print(set1 != set2)


# set1 = {1, 'a'}
# set2 = {2, 'b'}
# set3 = {1, 'a', 'b'}
# print(set1 - set2)
# print(set2 - set1)
# print(set1 - set3)
# print(set3 - set1)


# set1 = {1, 'a'}
# set2 = {2, 'b'}
# set3 = {1, 'a', 'b'}
# print(set1 & set2)
# print(set1 & set3)


# set1 = {1, 'a'}
# set2 = {1, 'a', 'b'}
# print(set1 | set2)
# print(set1.union(set2))


# lst1 = [5, 1, 2, 9, 0, 3]
# lst2 = [7, 2, 5, 7, 9]
# # 找出两个列表的不同元素
# set1 = set(lst1)
# set2 = set(lst2)
# # 并集 - 交集
# print(set1.union(set2) - set1.intersection(set2))
# # 两个差集的并集
# print(set1.difference(set2) | set2.difference(set1))
# print(set1.intersection(set2))


# set1 = {5, 1, 2, 9, 0, 3}
# set2 = {2, 5, 7, 9}
# print(set1 ^ set2)
# print(set1.symmetric_difference(set2))


lst = list('abc')
print(lst)


