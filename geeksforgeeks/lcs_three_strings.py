"""
https://practice.geeksforgeeks.org/problems/lcs-of-three-strings0028/1
https://www.geeksforgeeks.org/lcs-longest-common-subsequence-three-strings/

Similar Question
https://leetcode.com/problems/longest-common-subsequence/

"""

class Solution:

    def LCSof3(self,A,B,C,n1,n2,n3):
        dp = [[[0 for k in range(n3+1)] for j in range(n2+1)] for i in range(n1+1)]
        
        # print(dp)

        # if last character equals, then dp[i][j] = max(dp[i-1], dp[j-1])

        for i in range(1, n1+1):
            for j in range(1, n2+1):
                for k in range(1, n3+1):
                    if A[i - 1] == B[j - 1] == C[k - 1]:
                        dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                    else:
                        dp[i][j][k] = max(dp[i][j-1][k], dp[i-1][j][k], dp[i][j][k-1])
        return dp[-1][-1][-1]