# Rotate list k times.

def rotate_list(lst, k, direction="right"):
    n = len(lst)
    k %= n  # handle k > n
    
    if direction == "right":
        return lst[-k:] + lst[:-k]
    else:  # left
        return lst[k:] + lst[:k]


# Example
print(rotate_list([1,2,3,4,5], 2, "right"))  # [4, 5, 1, 2, 3]
print(rotate_list([1,2,3,4,5], 2, "left"))   # [3, 4, 5, 1, 2]