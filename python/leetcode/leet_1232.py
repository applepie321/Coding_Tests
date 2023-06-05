# 1232. Check If It Is a Straight Line

# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. 
# Check if these points make a straight line in the XY plane.

 




class Solution:
    def checkStraightLine(self, coordinates):
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]

        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            if (x - x0) * (y1 - y0) != (y - y0) * (x1 - x0):
                return False

        return True
 


# https://leetcode.com/problems/check-if-it-is-a-straight-line/solutions/2404442/python-soln-by-checking-slopes-w-explanation/
# Find slope for first two points, point1 and point2
# Then compare the slopes of all other points to this slope
# Slope of point1 (x1, y1) and point2 (x2, y2) is:
# (y2 - y1) / (x2 - x1)
# Slope of point1 (x1, y1) and point3 (x3, y3) is:
# (y3 - y1) / (x3 - x1)
# For all three points to be on the same line, the slopes should be equal, in other words:
# (y2 - y1) / (x2 - x1) = (y3 - y1) / (x3 - x1)
# To avoid the 'divide by zero' error, use cross multiplication to find slope:
# (y2 - y1) * (x3 - x1) = (y3 - y1) * (x2 - x1)