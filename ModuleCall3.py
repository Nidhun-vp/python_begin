#from calculatorModule import * # it import all functions in calculatorModule
from calculatorModule import add,sub # type: ignore we only use required functions from calculatorModule.
result1=add(200,400) 
result2=sub(200,100) 
print("result of add function:",result1)
print("result of mul function:",result2)