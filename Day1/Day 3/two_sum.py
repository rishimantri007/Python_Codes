# two sum indexes using dictornary

def two_sum(nums, target):
    seen = {}

    for i in range(len(nums)):
        num = nums[i]
        diff = target - num

        if diff in seen:
            return [seen[diff], i]

        seen[num] = i

    return []

print(two_sum([1,3,5,7,9],8))