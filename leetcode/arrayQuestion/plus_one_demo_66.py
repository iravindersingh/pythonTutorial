# You are given a large integer represented as an integer array digits,
# where each digits[i] is the ith digit of the integer. The digits are ordered
# from most significant to least significant in left-to-right order.
# The large integer does not contain any leading 0's.
#
# Increment the large integer by one and return the resulting array of digits.

class PlusOneDemo:

    @staticmethod
    def plus_one(nums):
        for i in range(len(nums)-1,0,-1):
            if nums[i] < 9:
                nums[i] = nums[i] + 1
                return nums
            else:
                nums[i] = 0
        # return nums

result = PlusOneDemo.plus_one([1,9,2,9,9])
print(result)