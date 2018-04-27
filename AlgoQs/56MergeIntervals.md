# 56. Merge Intervals


Given a collection of intervals, merge all overlapping intervals.

Example 1:

    Input: [[1,3],[2,6],[8,10],[15,18]]  
    Output: [[1,6],[8,10],[15,18]]  
    Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].  

Example 2:

    Input: [[1,4],[4,5]]  
    Output: [[1,5]]  
    Explanation: Intervals [1,4] and [4,5] are considerred overlapping.  


---

##### Solution:
    # Definition for an interval.
    # class Interval(object):
    #     def __init__(self, s=0, e=0):
    #         self.start = s
    #         self.end = e

    class Solution(object):
        def merge(self, intervals):
            """
            :type intervals: List[Interval]
            :rtype: List[Interval]
            """

            # Solution 1

            if not intervals:
                return []
            intervals = sorted(intervals, key = lambda i:i.start)
            result = []
            start = intervals[0].start
            end = intervals[0].end

            for i in range(len(intervals)):
                cur = intervals[i]
                if cur.start > end:
                    result.append(Interval(start,end))
                    start = cur.start
                    end = cur.end
                else:
                    if cur.end >end:
                        end = cur.end
            result.append(Interval(start,end))
            return result 


##### Solution:

            # Solution 2
            
            if not intervals:
                return []
                
            intervals = sorted(intervals, key = lambda i:i.start)
            
            result = [intervals[0]]

            for interval in intervals[1:]:
                if interval.start <= result[-1].end:
                    if interval.end > result[-1].end:
                        result[-1].end = interval.end
                else:
                    result.append(interval)
            return result 
