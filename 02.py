x = input('請輸入運算符號:')
a = int(input('請輸入數字:'))
b = int(input('請輸入數字:'))
if x == ('+'):
	print('答案為',a+b)
elif x ==('-'):
	print('答案為',a-b)
elif x == ('*'):
	print('答案為',a*b)
elif x == ('/'):
	print('答案為',int(a/b))
else:
	print('輸入錯誤')				