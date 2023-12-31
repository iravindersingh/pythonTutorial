# Given a sorted array of distinct integers and a target value,
# return the index if the target is found. If not,
# return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.

class BinarySearch:
    @staticmethod
    def search_position(nums, target):

        start = 0
        end = len(nums) -1
        while start <= end:
            mid = start + (end -start)//2
            print(mid, "mid .........")
            if(target == nums[mid]):
                return mid

            elif (target < nums[mid]):
                end = mid -1

            else:
                start = mid +1

        return mid

result = BinarySearch.search_position([1,3,4,5,6],2)
print(result)
