password = 'a123456'
x = 2
while x <= 2 and x >= 0:
	pwd = input('please input your password:')
	if pwd == password:
		print('you have sucessfully logged in')
		break;
	else:
		print('please input a correct password, you have', x, 'chance left')
		x = x-1