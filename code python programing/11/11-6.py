#coding=utf-8
def printf(rule, *num):
	i = -1
	for j in num:
		i = rule.find('%', i+1)    #对%定位，分三种情况讨论并进行替换
		if rule[i + 1] == 'd' and type(j) == int:
			result = rule.replace('%d', str(j), 1)
		elif rule[i + 1] == 'f' and type(j) == float:
			result = rule.replace('%f', str(j), 1)
		elif rule[i + 1] == 's' and type(j) == str:
			result = rule.replace('%s', j , 1)
		else:
			print 'ERROR'   #当对应类型不正确时抛出异常
			exit(0)
		rule = result
	print result