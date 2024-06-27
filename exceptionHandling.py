file_name='C:\\Users\\nidhun\\Documents\\hello.txt'
try:
    file=open(file_name,'r')
    t=file.read()
    print(t)
except FileNotFoundError: #fException(here we use FileNotFound) keyword for all type of generic exception
    print("sorry",file_name,'not found')    
else:
    print("thank you") # if not exception work these    