nums = [1,2,3,4,5]
print(nums)

nums0 = nums[0]
print(nums0)

range_list = nums[2:]
print(range_list)

range_list = nums[2:3]
print(range_list)

list_in_list = [nums, range_list]
print(list_in_list)

#indexing from the reverse
print(nums[-5])

#add the value
nums.append(8)

#insert via index
#9 is the index and 0 is the value
nums.insert(9,0)
print(nums)

#remove based
nums.remove(0)
print(nums, "remove 0")


#remove the element based on index
nums.pop(0)
print(nums, "pop 0")

#remove the element by default whichever last in index
nums.pop()
print(nums)

#delete multiple value
del nums[2:]

print(nums)

#add multiple value
nums.extend([1,2,3,4,45])

#get min number from the ;ist
print(min(nums))

#get max value from the list
print(max(nums))

print(nums.copy())

#sort in ascending order
nums.sort()
print(nums)

#sort in descending order
nums.reverse()
print(nums)

#give count total of element in the list
print(nums.count(3))

print(nums)

#can also insert in list like this
nums[0] = 2
print(nums)

#this is how he got first index of the element
print(nums.index(2))

#clear all element
nums.clear()



