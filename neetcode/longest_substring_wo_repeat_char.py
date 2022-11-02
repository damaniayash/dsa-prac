class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_cnt, max_cnt = 0, 0
        for i in range(0, len(s)):
            j = i
            wordset = set()
            while s[j] not in wordset :
                wordset.add(s[j])
                curr_cnt += 1x
                j += 1
                if j > len(s)-1:
                    break
            max_cnt = max(curr_cnt, max_cnt)
            curr_cnt = 0
        return max_cnt
                