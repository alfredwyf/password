password = 'a123456'
x = 3
while x > 0:
	pwd = input('please input your password:')
	if pwd == password:
		print('you have sucessfully logged in')
		break;
	else:
		x = x - 1
		print('please input a correct password, you have', x, 'chance left')