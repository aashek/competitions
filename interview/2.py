arr = [10,11,12,13,14,15,16,17,18,19]
l,r = 1,30
# l <= brr[i] <= r
# brr[i] - arr[i] <= brr[i+1] - arr[i+1]
# brr[i] <= brr[i+1]
# between two bounds check
# every prev diff should be less than current diff by 1 
# non-decreasing array

def getSmallestArray(arr, l, r):

    if l <= arr[0] <= r:
        brr = [arr[0]]
    elif arr[0] < l:
        brr = [l]
    else:
        return [-1]

    for i in range(1, len(arr)):
        diff = brr[i - 1] - arr[i - 1] + 1
        # print(diff)
        test_b = arr[i] + diff
        if not (l <= test_b <= r):
            return [-1]
        brr.append(test_b)

    return brr

print(getSmallestArray(arr, l, r))