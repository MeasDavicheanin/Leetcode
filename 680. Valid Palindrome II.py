s = "aba"

for i in range(0, len(s)):
    new_string=s.replace(s[i],"")
    if new_string==new_string[::-1]:
        print("True")
