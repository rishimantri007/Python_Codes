# Create list of squares of even numbers using comprehension

def list_compre(lst):
    return [item*item for item in lst if item%2==0]

print(list_compre([1,2,3,4,5,6,7,8]))