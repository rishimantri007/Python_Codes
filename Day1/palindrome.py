# Check if string is palindrome.

def pallindrome(str):
    left,right=0,len(str)-1

    while left<right:
        if str[left]!=str[right]:
            return False
        left+=1
        right-=1
    return True    


print(pallindrome("strts"))