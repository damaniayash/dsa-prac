class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        count = 0
        ss = [1, 5, 15, 60]
        current, correct = list(map(int, current.split(':'))), list(map(int,correct.split(':')))
        cu = 60 * current[0] + current[1]
        co = 60 * correct[0] + correct[1]
        diff = abs(cu-co)
        while diff > 0:
            if diff >= ss[-1]:
                diff -= ss[-1]
                count += 1
                continue
            else:
                ss.pop()
        return count
            
       