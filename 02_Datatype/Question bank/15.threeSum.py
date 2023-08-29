def threeSum(nums):
    nums.sort() # 对数组进行排序
    result = [] # 用于存储结果的三元组
    n = len(nums)

    for i in range(n):
        # 如果当前数字大于0，则三数之和一定大于0，所以结束循环
        if nums[i] > 0:
            break
        # 避免重复解
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                # 避免重复解
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
                
    return result
  
  
nums1 = [-1,0,1,2,-1,-4]
print(threeSum(nums1)) # 输出：[[-1,-1,2],[-1,0,1]]
nums2 = [0,1,1]
print(threeSum(nums2)) # 输出：[]
nums3 = [0,0,0]
print(threeSum(nums3)) # 输出：[[0,0,0]]