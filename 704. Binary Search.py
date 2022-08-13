nums = [-1, 0, 3, 5, 9, 12]
target=2
nums.sort()
#output 4
left=0
right=len(nums)-1
while left<right:
    middle=(left+right)//2
    if nums[middle]<target:
        left=middle+1
    elif nums[middle]>target:
        right=middle-1
    else:
        print(middle)
        break
print("ERROR")