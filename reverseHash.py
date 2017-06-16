def reverse_hash(hash):
	code=[]
	index=0
	while(hash>7):
		if(hash%37 == 0):
			code.append(letters[index])
			index=0
			hash=hash/37
		else:
			hash=hash-1
			index=index+1
	return code
	

def Unhash(str):
	h=7
	for i in range(len(str)):
		h=h*37+letters.index(str[i])
	return h
	

print "enter the numeric value"
letters="acdegilmnoprstuw"
hash_num=int(raw_input())
ans=reverse_hash(hash_num)
print "enter the string"
hash_str=raw_input()
ans2=Unhash(hash_str)
l=''
for i in range(len(ans)-1,-1,-1):
	l+=ans[i]
print "Hashed answer:"
print l
print "Unhashed answer:"
print ans2							