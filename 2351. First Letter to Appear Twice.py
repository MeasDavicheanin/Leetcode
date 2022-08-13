#Input: s = "abccbaacz"
#Output: "c"

s = "abcdd"
counter=set()

for i in s:
    if i not in counter:
        counter.add(i)
    else:
        print(i)
        break;