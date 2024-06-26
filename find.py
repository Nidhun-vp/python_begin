s='IT ALWAYS SEEMS IMPOSSIBLE UNTIL IT IS DONE'
#find is case sensitive used for search a string if found return start index
find_check=s.find("ALWAYS")
print(find_check)# return start index of ALWAYS that is 3
find_check=s.find("always")
print(find_check)# return -1 denote not found
find_check=s.lower().find("it")
print(find_check)
find_check=s.lower().find("it",find_check+1) #2nd parameter means adhayam kittiya "it" value nday aviday ne searching onnuday start cheyyan parayan
print(find_check)# return repeating "it" on string by passing other argument of ALWAYS that is 3

#count method 
# for take of string
no=s.count("IT")
print(no)