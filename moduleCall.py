import calculatorModule  # type: ignore
print(type(calculatorModule))

print("sum:")
result=calculatorModule.add(3,5)# add function get from calculatorModule we saved in same location of these file
print(result)
print("subtract:")
result=calculatorModule.sub(8,5)
print(result)
print("product:")
result=calculatorModule.mul(3,5)
print(result)
print("division:")
result=calculatorModule.div(10,5)
print(result)

