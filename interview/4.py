d = {}

items = [1,1,1,1,2] #
m = 2


for i in items:
    d[i] = d.get(i,0) + 1

print(sorted(d))