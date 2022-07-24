ll = [[1,3], [3,4], [4,5], [3,8], [1,10]]


ll.sort(key=lambda x: x[1])

print(ll)


prev = ll[0][1]
sum = 1

for i in range(1, len(ll)):
    if ll[i][1] <= prev:
        continue
    sum += 1
    prev = ll[i][0]


print(sum)