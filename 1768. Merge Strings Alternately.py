word1 = "ab"
word2 = "pqrs"
#Output: aqbqr

minimum=min(len(word1), len(word2))
ans=""
if len(word1)==len(word2):
    for i in range(minimum):
        ans+=word1[i]+word2[i]
elif len(word1)<len(word2):
    cut_word2=word2[:minimum]
    for i in range(minimum):
        ans+=word1[i]+word2[i]
    ans+=word2[minimum:]
else:
    cut_word1=word1[:minimum]
    for i in range(minimum):
        ans+=word1[i]+word2[i]
    ans+=word1[minimum:]
print(ans)