n=int(input("enter no:"))
if n==1:
    print("not prime")
else:
    flag=0
    for i in range(2,int((n/2)+1)):
        if n%i==0:
            flag=1
            break
if flag==1:
    print('not prime')
else:
    print("prime")            