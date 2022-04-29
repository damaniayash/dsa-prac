import re
class Solution:
    def reverseWords(self, s: str) -> str:
        s = ' '.join(s.split(' ')[::-1]).strip()
        s = re.sub(' +', ' ', s)
        return s