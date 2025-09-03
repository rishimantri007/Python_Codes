# Find first non-repeating character in a string
from collections import Counter
def non_repeating_first(str):
    # str=str.lower().split()
    freq=Counter(str)

    for ch in str:
        if freq[ch]==1:
            return ch
    return None

print(non_repeating_first("what wha jtoke"))