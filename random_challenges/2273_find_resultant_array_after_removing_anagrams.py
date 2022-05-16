class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        while True:
            prev = words
            remove_ind = []
            for i in range(0, len(words)-1):
                if sorted(words[i]) == sorted(words[i+1]):
                    remove_ind.append(words[i+1])
            for i in remove_ind:
                words.remove(i)
            if prev == words:
                return words
            prev = []
            
#         hashmap = []
#         remove_ind = []
        
#         for i in range(0, len(words)):
#             if ''.join(sorted(words[i])) in hashmap:
#                 remove_ind.append(words[i])
#                 continue
#             hashmap.append(''.join(sorted(words[i])))

#         for i in remove_ind:
#             words.remove(i)
            
#         return words
                
            