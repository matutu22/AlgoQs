# 452. Minimum Number of Arrows to Burst Balloons



There are a number of spherical balloons spread in two-dimensional space. For each balloon, provided input is the start and end coordinates of the horizontal diameter. Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end of the diameter suffice. Start is always smaller than end. There will be at most 104 balloons.

An arrow can be shot up exactly vertically from different points along the x-axis. A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend. There is no limit to the number of arrows that can be shot. An arrow once shot keeps travelling up infinitely. The problem is to find the minimum number of arrows that must be shot to burst all balloons.

    Example:  

    Input:  
    [[10,16], [2,8], [1,6], [7,12]]

    Output:  
    2

    Explanation:
    One way is to shoot one arrow for example at x = 6 (bursting the balloons [2,8] and [1,6]) and another arrow at x = 11 (bursting the other two balloons).
---

##### Solution 1:
    class Solution(object):
        def findMinArrowShots(self, points):
            """
            :type points: List[List[int]]
            :rtype: int
            """

            if not points:
                return 0
            points = sorted(points,key=lambda x:x[0])
            end = points[0][1]
            result = 1
            for point in points[1:]:
                if point[0] > end:
                    result += 1
                    end = point[1]
                if point[1] < end:
                    end = point[1]
            return result
