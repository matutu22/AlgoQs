# 213. House Robber II

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example 1:  

    Input: [2,3,2]  
    Output: 3  
    Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
                 because they are adjacent houses.

Example 2:  

 
    Input: [1,2,3,1]  
    Output: 4  
    Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
                 Total amount you can rob = 1 + 3 = 4.

---

##### Solution 1:
Either rob nums[0], which means no nums[-1],
Or not rob nums[0], which means only need to consider nums[1: ]


    class Solution(object):
        def rob(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            if len(nums) == 1:
                return nums[0]

            in1 = 0
            ex1 = 0
            for num in nums[:-1]:
                cur = ex1 + num
                ex1 = max(in1,ex1)
                in1 = cur
            r1 = max(in1,ex1)

            in2 = 0
            ex2 = 0
            for num in nums[1:]:
                cur = ex2 + num
                ex2 = max(in2,ex2)
                in2 = cur
            r2 = max(in2,ex2)

            return max(r1,r2)