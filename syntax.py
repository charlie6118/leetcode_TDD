
nums = [1, 2, 3, 4, 2, 1, 3, 5]
# how to add create dictionary from list
d = {}
for val in nums:
    d[val] = d.get(val, 0) + 1
print(d)

# traverse through key and value
for i, v in enumerate(nums):
    print(i, v)

# iterate through dictionary
dic = {}
for num in nums:
    dic[num] = dic.get(num, 0)+1
for key, val in dic.items():
    if val == 1:
        print(key)

#size of dictionary
len(dic)

# find the mid of linked list
# slw & fst, slw move once each time and fst move twice 
fast = slow = head
while fast and fast.next:
    fast = fast.next.next
    slow = slow.next