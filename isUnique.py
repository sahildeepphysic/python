def isUnique(list):
	# y=0
	# for x in list:
	# 	y=y^ord(x)
	# if y != 0 :
	# 	return True
	# return False
	count=0
	for x,y in enumerate(list):
		for z in list[x+1:]:
			if y==z:
				return False
	return True
print(isUnique("hell"))