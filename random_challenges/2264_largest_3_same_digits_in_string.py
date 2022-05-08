class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = []
        temp = ''
        for i in range(0, len(num)-1):
            if num[i] == num[i+1]:
                temp += num[i]
            else:
                temp = ''
            if len(temp) == 2:
                ans.append(temp+temp[-1])
        if ans:
            return max(ans)
        else: return ''
        
            
                