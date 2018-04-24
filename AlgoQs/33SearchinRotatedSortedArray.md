# 33. Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0  
Output: 4    


Example 2:  

Input: nums = [4,5,6,7,0,1,2], target = 3  
Output: -1  


##### Solution :
	class Solution(object):
        def search(self, nums, target):
            """
            :type nums: List[int]
            :type target: int
            :rtype: int
            """
            lo = 0
            hi = len(nums) - 1
            # When lo+1=hi, target = nums[hi], so add =
            while lo <= hi :
                mid = (lo+hi) / 2
                if nums[mid] == target:
                    return mid

                # Add =, because nums[lo] may be target
                if nums[mid] >= nums[lo]:
                    # Is in the left up tunnel
                    if  nums[lo] <= target < nums[mid]:
                        hi = mid - 1
                    else:
                        lo = mid + 1

                else:
                    # Is in the right up tunnel
                    if nums[hi]>=target > nums[mid]:
                        lo = mid + 1
                    else:
                        hi = mid - 1

            return -1
                    
                