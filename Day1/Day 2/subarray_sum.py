# Find subarray with given sum

def subarray_sum(lst,k):
    start=0
    current_sum=0

    for end in range(len(lst)):
        current_sum+=lst[end]

        while current_sum>k and start<=end:
            current_sum-=lst[start]
            start+=1

        if current_sum==k:
            return lst[start:end+1]    
    return None    

print(subarray_sum([1,2,3,4,5,6,7],10))


# kya karta hai yeh program
# sum karta hai tab tak jab tak sum k ya usse jada na ho
# next voh list ka starting se ek ek eleminent minus karta hai till current_sum==k bss....