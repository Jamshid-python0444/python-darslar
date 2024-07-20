harf = input('Harf kiriting:')

unli1 = 'e'
unli2 = 'u'
unli3 = 'i'
unli4 = 'o'
unli5 = 'a'

if harf.isalpha():
	if unli1 == harf or unli2 == harf or unli3 == harf or unli4 == harf or unli5 ==harf:
		print('{} - Unli!'.format(harf))
	else:
		print('{} - Undosh!'.format(harf))
else:
	print('Harf kiriting!')

