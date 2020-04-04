'''

<img class="BDE_Image" pic_type="0" width="560" height="450" src="http://tiebapic.baidu.com/forum/w%3D580/sign=b32ee2fbdeea15ce41eee00186003a25/ec8e3f6d55fbb2fbf303d46c584a20a44623dc01.jpg" size="188652" style="cursor: url(&quot;http://tb2.bdstatic.com/tb/static-pb/img/cur_zin.cur&quot;), pointer;">

'''

# s = 'abcdefg'
# index = 0
# while index < len(s):
# 	print(s[index])
# 	index += 1

# print(s[5::-2])
# print(s[3:6])
# print(s[-4:-1])
# print(s[::3])
# print(s[-2:-7:-2])
# print(s[-3:-6:-1])
# print(s[4:1:-1])
# print(s[-5::-1])
# print(s[5:0:-2])
# print(s[2:-2])
# print(s[2:5])
# print(s[-5:-2])

s = 'http://tiebapic.baidu.com/forum/w%3D580/s01.jpg'
# end = 0
# count = 3
# while count > 0:
# 	end = s.find('/', end + 1)
# 	count -= 1
# print(s[:end])

start = s.rfind('/')
print(s[start + 1:])


