
nums = [1, 2, 3, 4, 2, 1, 3, 5]
# how to add create dictionary from list
d = {}
for val in nums:
    d[val] = d.get(val, 0) + 1
print(d)

# traverse through key and value
for i, v in enumerate(nums):
    print(i, v)