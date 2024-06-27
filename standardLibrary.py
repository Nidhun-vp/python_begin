import os
path=os.getcwd()+"\\new"
print(path)
if os.path.exists(path):
    print("folder exists")
else:
    os.mkdir(path)
    print('folder doesnt exist')
    
#os.rmdir(os.getcwd()+ "\\new") or we can also use path variable  inside rmdir()

