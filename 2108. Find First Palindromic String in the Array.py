
def firstPalindrome(words) -> str:
    for i in words:
        if i == i[::-1]:
            return i
    return ""

def main():
    words = ["abc","car","ada","racecar","cool"]
    ans=firstPalindrome(words)
    print(ans)
