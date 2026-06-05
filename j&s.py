#split 
s="catch-the-code"
new_str=s.split("-")
print(new_str)
str1='*'.join(new_str)
print(str1)
lang=["C","C++","Java"]
# for i in lang:
#     print(i,"and",end=" ")
print(' and '.join(lang))