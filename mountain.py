def chkMountain(list):
	start=0
	end=len(list)-1
	pointerStart=0
	pointerEnd=len(list)-1
	print(list[pointerEnd])
	print(start,end,pointerStart,pointerEnd)
	print("========")
	while list[pointerStart]!=list[pointerEnd]:
		print(str(pointerStart)+" and "+str(pointerEnd))
		if list[pointerStart]>list[pointerStart+1]:
			start=pointerStart+1
		if list[pointerEnd]>list[pointerEnd-1]:
			end=pointerEnd-1
		pointerStart+=1
		pointerEnd-=1
	print(start,end)
	print(list[start:end+1])
chkMountain([1, 3, 1, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5])