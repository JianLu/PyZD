"""
Given two strings str1 and str2 and below operations that can performed on str1.
Find minimum number of edits (operations) required to convert ‘str1’ into ‘str2’.

Insert
Remove
Replace
All of the above operations are of equal cost.
"""


class Solution(object):
    def minEditDistance(self, s1, s2):
        m, n = len(s1), len(s2)

        # Create a table to store results of subproblems
        # M[i][j] denotes the minimum edit distance from s1[0,..,i-1] to s2[0,..,j-1]
        d = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        # Initialize boundaries
        # If s1 == "", then d(s1, s2) = len(s2), add characters to s1
        d[0] = [x for x in range(n+1)]
        # If s2 == "", then d(s1, s2) = len(s1), remove characters from s1
        for i in range(m+1):
            d[i][0] = i

        # Fill in the table bottom-up
        for i in range(m):
            for j in range(n):
                if s1[i] == s2[j]:
                    d[i+1][j+1] = d[i][j]
                else:
                    d[i+1][j+1] = 1 + min(d[i][j+1], d[i+1][j], d[i][j])

        return d[m][n]

if __name__ == "__main__":
    sol = Solution()
    s1 = "sunday"
    s2 = "saturday"
    print(sol.minEditDistance(s1, s2))