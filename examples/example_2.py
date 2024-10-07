from itertools import accumulate

string = input().split()

for word in string:
    word = word + ' '
for word in accumulate(string):
    print(word + ' ')

#for string in accumulate([word + ' ' for word in input().split()]):