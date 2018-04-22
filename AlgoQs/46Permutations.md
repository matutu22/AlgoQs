# 46. Permutations

Given a collection of distinct integers, return all possible permutations.

Example:

Input:  
[1,2,3]  

Output:  

    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]
---

##### Solution 1 Recursively:
	class Solution(object):
        def permute(self, nums):
            """
            :type nums: List[int]
            :rtype: List[List[int]]
            """
            
            result = [[]]

            for n in nums:
                temp = []
                for r in result:
                    for i in range(len(r)+1):
                        temp.append(r[:i] + [n] + r[i:])
                result = temp
            return result 
        
        
##### Solution 2 Iteratively:

	class Solution(object):
        def permute(self, nums):
            """
            :type nums: List[int]
            :rtype: List[List[int]]
            """


            result = []
            
            def helper(nums, path, result):
                if not nums:
                    result.append(path)
                for i in range(len(nums)):
                    helper(nums[:i] + nums[i+1:], path + [nums[i]], result)
                    
            helper(nums, [], result)
            
            return result 