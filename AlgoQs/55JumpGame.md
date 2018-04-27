# 55. Jump Game




Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

    Input: [2,3,1,1,4]  
    Output: true  
    Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.  

Example 2:

    Input: [3,2,1,0,4]  
    Output: false  
    Explanation: You will always arrive at index 3 no matter what. Its maximum
                 jump length is 0, which makes it impossible to reach the last index.



---

##### Solution 1:
    class Solution(object):
        def canJump(self, nums):
            """
            :type nums: List[int]
            :rtype: bool
            """
            
            # Go backwards, if goal can be reached
            # Set goal to the smalled index that can reach him
            
            goal = len(nums)-1
            for i in range(len(nums))[::-1]:
                if i + nums[i] >= goal:
                    goal = i
            if goal <= 0:
                return True
            else:
                return False



##### Solution 2:
	       
        # m is the max position can reach at i
        # If at i, m < i, means i can't be reached => False
        
        m = 0
        l = len(nums)
        for i, v in enumerate(nums):
            if i > m:
                return False
            m = max(m, i+v)
            if m >= l-1:
                return True