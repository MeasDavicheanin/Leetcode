nums = [0]
left=0
right=len(nums)-1
while left<right:
    if nums[left]%2==0:
        left+=1
    else:
        #swap
        nums[left], nums[right] = nums[right], nums[left]
        right-=1
print(nums)