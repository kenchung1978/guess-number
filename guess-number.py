import random

r = random.randint(1, 100)
count = 0
while True:
	count += 1 # count = count + 1 的快寫法
	num = input('猜猜數字:')
	num = int(num)
	if num == r:
		print('恭喜猜對了')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('這是你猜的第', count, '次')
