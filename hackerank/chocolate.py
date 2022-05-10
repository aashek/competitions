a = [2,2,1,3,2]

length = 2
sum0 = 4

# return [2,2] [1,3] 

ret = []

for i in range(len(a) - 1):
    c = a[i:i+length]
    if sum(c) == sum0:
        ret.append(c)


print(ret)