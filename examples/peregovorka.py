n = int(input())
left = []
right = []
r_min = 0
count = 0
string = []

for i in range(n):
    string.append(list(map(int, input().split())))

for i in range(len(string)):
    if i % 2 == 0:
        left[i] = string[i]
    if i % 2 != 0:
        right[i] = string[i + 1]

for i in range(n):
    r_min = min(right)
    index = right.index(r_min)
    if left[i] <= r_min:
        left = left.pop(i)
        right = right.pop(i)

count = len(right)
print(count)