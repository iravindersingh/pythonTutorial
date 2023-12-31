# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints
# of the ith line are (i, 0) and (i, height[i]).
#
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
#
# Return the maximum amount of water a container can store.
#
# Notice that you may not slant the container.

import math

class MostWater:

    @staticmethod
    def most_water(lst):
        start = 0
        end = len(lst)-1
        maxAvg = 0

        while start < end:
            avg = min(lst[start], lst[end]) * (end - start)

            maxAvg = max(avg,maxAvg)

            if lst[start] > lst[end]:
                end -= 1
            else:
                start += 1

        print(maxAvg)
MostWater.most_water([1,8,6,2,5,4,8,3,7])












