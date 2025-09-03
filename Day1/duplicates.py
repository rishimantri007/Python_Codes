# Remove duplicates from list

def remove_duplicates(lst):
    seen=set()
    unique_list=[]
    for item in lst:
        if item not in seen:
            seen.add(item)
            unique_list.append(item)
    return unique_list

print(remove_duplicates([1,2,2,3,3,4,4,5]))        
