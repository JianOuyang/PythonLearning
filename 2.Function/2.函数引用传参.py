def recoverRotatedSortedArray(nums):
    print(id(nums))
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            temp = nums[(i + 1):] + nums[:(i + 1)]
            print(temp)
            break
    #第一种赋值方式
    #nums = temp
    
    #第二种赋值方式
    for i in range(len(nums)):
        nums[i] = temp[i]
    print(id(nums))
    print(id(temp))

nums = [6,7,1,2,3,4,5]
print(id(nums))
recoverRotatedSortedArray(nums)
print(nums)