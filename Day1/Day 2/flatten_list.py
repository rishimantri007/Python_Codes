# Flatten a 2D list.

# def flatten(lst):
#     return [item for sublist in lst for item in sublist]

# print(flatten([[1,2],[3,4],[5,6,7]]))

# If the list is deeply nested (like [1, [2, [3, 4]]]), we’d need a recursive function.

def flatten(lst):
    flat = []
    for item in lst:
        if isinstance(item, list):   # if element is a list → flatten it recursively
            flat.extend(flatten(item)) # [1,[2,[3,4]]]->1,[2,[3,4]] aisa banayga aur flat list me add karega
        else:
            flat.append(item)
    return flat


# Example
print(flatten([[1, [2, [3, 4]], 5],[8,9]]))