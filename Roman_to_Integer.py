#Roman_to_Integer.py
dict = {'I':1,'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

roman_num = input()
roman_num = roman_num.replace("IV","IIII").replace("IX","VIIII")
roman_num = roman_num.replace("XL","XXXX").replace("XC","LXXXX")
roman_num = roman_num.replace("CD","CCCC").replace("CM","DCCCC")
a = 0

for num in roman_num:
    if num in dict.keys():
        print(dict[num])
        a = a+dict[num]
print(a)