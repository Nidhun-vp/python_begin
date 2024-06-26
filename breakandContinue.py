n=[10,20,30,0,40,50]
for i in n:
    if i==0:
        break
    print(i)
print("after executing break these statement works")    
#continue
print("continue working")
n=[10,20,30,0,40,50]
for i in n:
    if i==0:#condition  is print not work again goto for loop for next value
        continue
    print(i)