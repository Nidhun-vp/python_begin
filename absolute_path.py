file_name='C:\\Users\\nidhun\\Documents\\ipl.txt'
with open(file_name,'r',encoding='utf-8') as f:
    text=f.read()
    print(text)