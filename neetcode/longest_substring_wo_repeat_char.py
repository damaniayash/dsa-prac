class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        ans = 0
        l = 0 
        for r in range(0, len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            ans = max(ans, len(char_set))
        return ans
        
        # curr_cnt, max_cnt = 0, 0
        # for i in range(0, len(s)):
        #     j = i
        #     wordset = set()
        #     while s[j] not in wordset :
        #         wordset.add(s[j])
        #         curr_cnt += 1
        #         j += 1
        #         if j > len(s)-1:
        #             break
        #     max_cnt = max(curr_cnt, max_cnt)
        #     curr_cnt = 0
        # return max_cnt
                