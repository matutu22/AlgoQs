# 650. 2 Keys Keyboard


Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step:

Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
Paste: You can paste the characters which are copied last time.
Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'.

Example 1:  
Input: 3  
Output: 3  
Explanation:  

      Intitally, we have one character 'A'.
      In step 1, we use Copy All operation.
      In step 2, we use Paste operation to get 'AA'.
      In step 3, we use Paste operation to get 'AAA'.
      Note:
      The n will be in the range [1, 1000].

---

##### Solution 1:
	class Solution(object):
        def minSteps(self, n):
            """
            :type n: int
            :rtype: int
            """

            result = 0
            # i steps if i is largest that can divide
            for i in range(2,int(n**0.5)+1):
                while n%i == 0:
                    result += i
                    n /=i

            # If n is prime number
            if n != 1:
                result += n

            return result


        
##### Solution 2:
DP 

        dp = [0]*(n+1)        
        for i in range(2,n+1):
            dp[i] = i
            for j in range(2,i)[::-1]:
                if i%j == 0:
                    dp[i] = dp[j] + i/j
                    break
        return dp[n]