# Check if two strings are anagrams.

def isanagram(str1,str2):
    str1=sorted(str1.lower().replace(" ",""))
    str2=sorted(str2.lower().replace(" ",""))
    return str1==str2

print(isanagram("str","trs"))