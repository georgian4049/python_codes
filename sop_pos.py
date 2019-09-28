sop=input("Enter SOP\n")
lis=sop.split("+")
count=0
for item in lis:
	a='('
	j=item.replace(' ','')
	for items in j:
		a=a+items+"+"
	lis[count]=a[0:-1]+')'

	count+=1
lis.sort()
a=''
for j in lis:
	a=a+'.'+j
a=a[1:]
b=a.replace('+\'','\'')
print(b)