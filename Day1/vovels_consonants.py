# Count vowels/consonants in a string.

def count_vowels_consonants(str):
    vowels="aeiouAEIOU"
    v_count=0
    c_count=0

    for ch in str:
        if ch.isalpha():
            if ch in vowels:
                v_count+=1
            else:
                c_count+=1
    return v_count,c_count

v,c=count_vowels_consonants("ramraoadik")
print(v,c)                