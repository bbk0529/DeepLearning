def count(filename):
	a=[]
	count={}
	for x in open(filename,'r').readlines():
		a.extend(list(x)) 
	for i in a:
		count[i]=count.get(i, 0)+1
	for x in sorted(count, key=count.get, reverse=True):
		print(x,count[x])