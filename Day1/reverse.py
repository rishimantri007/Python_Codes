# Reverse a number without converting to string.

def reverse_number(n):
    rev=0
    negative= n<0
    n=abs(n)

    while n>0:
        digit=n%10
        rev=rev*10+digit
        n=n//10
    return -rev if negative else rev

print(reverse_number(12345))    
print(reverse_number(-2345))

# reverse string without using slicing

def reverse_string(s):
    result = ""
    for ch in s:
        result = ch + result
    return result

print(reverse_string("hello"))  # olleh