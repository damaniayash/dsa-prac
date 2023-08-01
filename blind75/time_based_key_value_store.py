class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = [(value, timestamp)]
        else:
            self.hashmap[key].append((value, timestamp)) 

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        for value, curr_ts in reversed(self.hashmap[key]):
            if timestamp == curr_ts or timestamp > curr_ts:
                return value
        return ""

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
