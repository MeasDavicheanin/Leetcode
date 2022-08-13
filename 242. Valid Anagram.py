s = "rat"
t = "car"
#output True

# hash table approach 

countS={}
countT={}
for c in len(s):
    countS[s[c]]=1+countS.get(s[c],0)
    countT[s[c]]=1+countT.get(s[c],0)
for i in countS:
    if countS[i]!=countT.get(i,0):
        print("false")
