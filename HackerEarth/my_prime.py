def my_prime(n,lists):
	plist=[]
	for i in range(n):
		index=i
		flag= True
		for j in range(n):
			if j==index:
				continue
			if lists[i] % lists[j] == 0:
				flag = False
		if flag:
			plist.append(str(lists[i]))
	return " ".join(plist)
			
	

n=5
lst=[10,5,3,15,16]

print my_prime(n,lst)
