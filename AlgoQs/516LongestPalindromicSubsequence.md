# 516. Longest Palindromic Subsequence

Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

    "bbbab"
Output:  

    4  
    One possible longest palindromic subsequence is "bbbb".  
    
Example 2:  
Input:

    "cbbd"
Output:  

    2  
    One possible longest palindromic subsequence is "bb".

---


##### Solution 1:
    class Solution(object):
        def longestPalindromeSubseq(self, s):
            """
            :type s: str
            :rtype: int
            """


            l = len(s)
            if s == s[::-1]:
                return l

            dp = [[0 for _ in range(l)] for _ in range(l)]

            '''
             The order can be decided from the state transition. dp[i][j] is depend on dp[i+1][j-1], which means to calculate dp[i][j], you need to know the value of 				dp[i+1][j-1] first ("i" is relying on "i+1", "i+1" need to be calculate first, that's why the i loop reverse order)
            '''


            for i in range(l-1, -1, -1):
                dp[i][i] = 1
                for j in range(i+1,l):
                    if s[i] == s[j]:
                        dp[i][j] = dp[i+1][j-1] + 2
                    else:
                        dp[i][j] = max(dp[i+1][j], dp[i][j-1])

            return dp[0][l-1]