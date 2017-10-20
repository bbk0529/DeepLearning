

def run():

	import numpy as np
	fr = open('jung.txt', encoding='utf-8')
	problem=[]
	arrLine=[]
	for line in fr.readlines() :
		line=line.replace('\ufeff','')
		line=line.replace('\n','')
		arrLine=line.split(sep=':')
		problem.append(arrLine)

	no=np.arange(0,len(problem))
	while True:
		n=np.random.randint(0,len(no))
		print('================================================')
		print(problem[no[n]][1])
		a=input()
		if a=='q' : break
		print(problem[no[n]][0] + '\n\n')
		no=np.delete (no,n)
