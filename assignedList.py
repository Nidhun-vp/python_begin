original_list=[1,2,3,4]
assigned_list=original_list
print(original_list)
print(assigned_list)
assigned_list.append(5)
print(assigned_list)
print("note:assigned list is point with original list. so changes are effect in assigned list")
print(original_list)
#copy list
copyList=original_list.copy()
print(original_list)
original_list.append(6)
print(original_list)
print("appended value of original list is not affect copy list")
print(copyList)