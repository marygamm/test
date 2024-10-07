from itertools import count

nums = input().split()
for num in nums:
    num = float(num)

for n in count(nums[0], nums[2]):
    if n <= nums[1]:
        print(round(n, 2))
    else:
        break