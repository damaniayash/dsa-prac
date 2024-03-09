class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        masterset = [set("qwertyuiopQWERTYUIOP"), 
                        set("asdfghjklASDFGHJKL"), 
                        set("zxcvbnmZXCVBNM")]
        res = []

        for word in words:
            for i in range(0, len(masterset)):
                if word[0] in masterset[i]:
                    print(masterset[i])
                    ind = i

            add = True
            for char in word:
                if char not in masterset[ind]:
                    add = False
                    
            if add:
                res.append(word)
        
        return res
                    
