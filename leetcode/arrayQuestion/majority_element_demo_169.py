class Solution:

    @staticmethod
    def majorityElement(lst):
        count = 0
        candidate = 0

        for num in lst:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate

a = Solution()
print(a.majorityElement([1,2,3,3,3,4,5,6,1,2,2,8,2,2,3,3,3,3]))
