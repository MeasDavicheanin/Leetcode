nums = [3, 2, 1, 5, 4]
k=2
#[1,2,2,1]

count=0
for i in range(0,len(nums)-1):
    for j in range(i,len(nums)):
        if i!=j:
            if abs(nums[i]-nums[j])==k:
                count+=1
print(count)