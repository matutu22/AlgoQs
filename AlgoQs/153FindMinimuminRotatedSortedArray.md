# 153. Find Minimum in Rotated Sorted Array



Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.

Example:

    Input: [3,4,5,1,2],  
    Output: 1
 


---

##### Solution 1:
	class Solution(object):
        def findMin(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            lo = 0 
            hi = len(nums) - 1
            while lo <= hi:
                mid = (lo+hi)/2
                if nums[mid] >= nums[lo]:
                    if nums[mid] > nums[hi]:
                        lo = mid + 1
                    else:
                        hi = mid - 1
                else:
                    if nums[mid-1] < nums[mid]:
                        hi = mid - 1
                    else:
                        return nums[mid]
            return nums[lo]