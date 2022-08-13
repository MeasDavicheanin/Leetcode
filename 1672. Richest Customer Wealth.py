accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]

ans=0
for item in accounts:
    if sum(item)>ans:
        ans=sum(item)

print(ans)