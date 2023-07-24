def move_zeros(nums):
    non_zero = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[non_zero] = nums[i]
            non_zero += 1

    for i in range(non_zero, len(nums)):
        nums[i] = 0

nums = list(map(int,input().split()))
move_zeros(nums)
print(nums)  

