nums = ["1", "1", "1"]
target = "11"
count=0
for i in range(0, len(nums)):
    for j in range(0, len(nums)):
        if i!=j:
            print(nums[i], nums[j])
            if nums[i]+nums[j]==target:
                count+=1
print(count)