# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
#
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n,
# where the first m elements denote the elements that should be merged,
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

class MergeTwoArray:

    @staticmethod
    def merge_array(arr1, arr2):
        i = 0
        j = 0
        merged_arr = []
        while((len(arr1) > i) and (len(arr2) > j)):
            if arr1[i] > arr2[j]:
                merged_arr.append(arr1[j])
                j += 1
            else:
                merged_arr.append(arr1[i])
                i +=1
        while len(arr1) > i:
            merged_arr.append(arr1[i])
            i += 1

        while len(arr2) > j:
            merged_arr.append(arr2[j])
            j += 1
        return merged_arr

re = MergeTwoArray.merge_array([1,2,3,4,5,6,7,8], [1,2,3,4,5,6,7])
print(re)
