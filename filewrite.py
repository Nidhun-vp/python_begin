t=input("enter the text:")
file=open('engg_colleges.txt','w')
file.write(t)# write mode clear existing content then add new content
file.close()
print("file writed successfully")