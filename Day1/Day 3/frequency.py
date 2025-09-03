

from collections import Counter

def feq_counter(str):
    words=str.lower().split()
    # words=words.strip(".,!?;:")
    freq=Counter(words)
    return freq

print(feq_counter("hi rishi rishi is fine hi"))