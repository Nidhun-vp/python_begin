def remove_vowel(string):
    vowels="aeiouAEIOU"
    return ' '.join([char for char in string if char not in vowels])


input_string="Raspberry Pi will capture real-time visuals"
result=remove_vowel(input_string)
print(result)