import numpy as np


randnums = np.random.randint(1,101,6)
print(list(randnums))


def mergeSort(A, l, r):
    if l < r:
        mid = l + r // 2
        left = mergeSort(A, l, mid)
        right = mergeSort(A, mid + 1, r)
        if not left:
            return right
        elif not right:
            return left
        return left.extend(right)

print(mergeSort(randnums, 0, len(randnums) - 1))