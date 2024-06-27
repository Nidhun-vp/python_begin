file_name='tourist_places.txt'# relative path same folder has the txt file.if other location use path in quotes
file=open(file_name,'r')  #file object created we can only open files by using file object
places=file.read()  #read all content using read method and assign to places
print(places)
file.close()# close file file for avoid memory leakage

