# 238. Product of Array Except Self

Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

Follow up:
Could you solve it with constant space complexity?  

(Note: The output array does not count as extra space for the purpose of space complexity analysis.)


---


##### Solution :
	
	class Solution(object):
        def productExceptSelf(self, nums):
            """
            :type nums: List[int]
            :rtype: List[int]
            """
            length = len(nums)
            result = [1] * length

            for i in range(1,length):
                result[i] = result[i-1] * nums[i-1]

            right = 1
            for i in range(length-1,-1,-1):
                result[i] *= right
                right *= nums[i]

            return result