a=[]
count1=0
count2=0
n=int(input("enter limit:"))
for i in range(n):
	val=int(input())
	a.append(val)
    
	if a[i]%2==0:
			count1+=1
	else:
			count2+=1
print("evencount:",count1)
print("evencount:",count2)					
	