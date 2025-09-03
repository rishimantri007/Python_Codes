# Find intersection of 3 listsdef 


def intersection(list1,list2,list3):
    return list(set(list1) & set(list2) & set(list3))

print(intersection([1,2,3,4,5],[1,2,4,6],[1,3,4,7]))