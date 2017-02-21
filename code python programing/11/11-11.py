#coding=utf-8
def  clear(mystring):
	return str(mystring.strip()) + 'n'

if __name__ == '__main__':
	with open('1.txt', 'r') as f:
		lines = f.readlines()
		result = map(clear, lines)
	f.close()
	choise = raw_input('Do you want to make a new file? n/y')
	if choise == 'y':
		filename = raw_input('Input your file name:')
		newfile = open(filename, 'w')
		newfile.writelines(result)
		newfile.close()
	else:
		with open('1.txt', 'w') as f:
			f.writelines(result)
		f.close()