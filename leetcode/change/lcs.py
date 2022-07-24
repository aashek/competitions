
# string m length lm
# string n length ln

m = 'quetzalcoatl'
n = "tezcatlipoca"

lm = len(m)
ln = len(n)

lcs = [[0 for i in range(lm)] for j in range(ln)]
print(len(lcs))
print(len(lcs[0]))
for i in range(lm):
    for j in range(ln):
        if i == 0 | j == 0:
            lcs[i][j] = 0
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])
            if (m[i-1] == n[j-1]):
                lcs[i][j] = max(lcs[i][j], lcs[i-1][j-1] + 1)