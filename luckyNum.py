n=int(input())
sum1,sum2=0,0
for i in range(len(str(n))//2):
    sum1=sum1+int(str(n)[i])
for i in range(len(str(n))//2,len(str(n))):
    sum2=sum2+int(str(n)[i])
if sum1==sum2:
    print("yes")
else:
    print("No")        
    
