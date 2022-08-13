nums = [2, 2, 1, 1, 1, 2, 2]
#Output: 3
count={}
res, maxCount=0,0

for n in nums:
    count[n]=1+count.get(n,0)
    res= n if count[n]>maxCount else res
    maxCount=max(count[n],maxCount)
print(res)
        
    

    

