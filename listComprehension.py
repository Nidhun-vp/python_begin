numbers=[1,2,3,4,5,6,7,8,9,10]
even_list=[x for x in numbers if x%2==0 ] #first x accept values in numbers which satisfy the if condition.2nd x check each values of numbers.
print(even_list)
old_list=[x for x in numbers if x%2!=0]
print(old_list)