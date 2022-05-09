# a = [1,2,3] 
# b = [2,5,5]


# intrusive
def mergeArrays(a,b):
    if not a:
        return b 
    elif not b:
        return a 

    ret = []
    while a and b:
        if a[0] < b[0]:
            ret.append(a.pop(0))
        elif a[0] >= b[0]:
            ret.append(b.pop(0))
        
    if a:
        ret.extend(a)
    elif b:
        ret.extend(b)

    return ret

def mergeArrays1(a,b):    
    return sorted(a + b)


# Driver code
arr1 = [1]
 
arr2 = [2, 4, 6, 8]
print(mergeArrays(arr1, arr2))
print(mergeArrays1(arr1, arr2))