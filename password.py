password = 'a123456'
x = 2
while x <= 2 and x >= 0:
	password = input('please input your password:')
	if password == 'a123456':
		print('you have sucessfully logged in')
		break;
	else:
		print('please input a correct password, you have', x, 'chance left')
		x = x-1