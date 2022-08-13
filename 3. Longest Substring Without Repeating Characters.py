s = "dvdf"
#Output: 3
# sliding window 
left,right=0,0
data=set()
res=0
while (right<len(s)):
    if s[right] not in data:
        data.add(s[right])
        right+=1
    else:
        data.remove(s[left])
        res=max(res,right-left)
        left+=1
res=max(res,right-left)
print(res)


        