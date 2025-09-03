# Find 2nd largest element in list.

def kthlargest(lst,k):
    unique_list=list(set(lst))
    unique_list.sort(reverse=True)
    return unique_list[k-1] if len(unique_list)>=k else None

print(kthlargest([10,10,20,30,90,70],2))