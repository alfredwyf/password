password = 'a123456'
x = 3
while x > 0:
	x = x - 1
	pwd = input('please input your password:')
	if pwd == password:
		print('you have sucessfully logged in')
		break;
	else:
		print('please input a correct password')
		if x > 0:
			print('you have', x, 'chance left')
		else:
			print('you have no chance left, your account is logged')