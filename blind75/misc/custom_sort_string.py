class Solution:
    def customSortString(self, order: str, s: str) -> str:

        c_map = {}
        for char in s:
            c_map[char] = c_map.get(char, 0) + 1
        #print(c_map)

        new_s = ''
        for char in order:
            if char in c_map:
                while c_map[char] != 0:
                    new_s += char
                    c_map[char] -= 1
        
        #print(c_map)
        for key, value in c_map.items():
            if c_map[key] == 0:
                #print('skipped')
                continue
            while True:
                #print('entered while', c_map[key])
                new_s += key
                c_map[key] -= 1
                if c_map[key] == 0:
                    break
        
        #print(c_map)
        #print(new_s)
        return new_s

        