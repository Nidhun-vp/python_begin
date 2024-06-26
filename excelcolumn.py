#program for excel column_no. from title find       
def titleToNumber(columnTitle):
    result = 0
    for i in range(len(columnTitle)):
        result *= 26
        result += ord(columnTitle[i].upper()) - ord('A') + 1 #ord for convert a charactor into asll code
    return result    

columnTitle = "ABC"
print(titleToNumber(columnTitle))  # Expected output: 704
       
   
       