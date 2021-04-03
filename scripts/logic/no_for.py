def listIndex(i):
	print(i,list1[-i-1])
	if i < 1:return 
	else: listIndex(i-1) ;return
listIndex(5)
