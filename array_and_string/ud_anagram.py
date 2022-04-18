from collections import Counter
def anagram():
    s1 = "resftul"
    s2 = "fluster"
    s1 = Counter(s1)
    s2 = Counter(s2)
    if s1 == s2: return True
    else: return False
print(anagram())
    