def sum(a,b):
    c=a+b
    return c
    
    
result=sum(10,20)#return carry value of c to result assign to it
print(result)    

#optional parameters-last parameters of function definion is set as optional parameter first parameter canot possible to set optional parameter
def greet(name,greet="hello"):
    print("{},{}!*".format(name,greet))
greet("alice")#assign only to name parameter in line 10 greet use default value
greet("bob","hi")   #value of name,greet are updated 