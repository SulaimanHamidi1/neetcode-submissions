class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        
        values = self.hashmap[key]
        l, r = 0, len(values) - 1

        successor = -1
        succ_index = -1

        while l <= r:
            m = l + (r - l) // 2

            if values[m][1] <= timestamp:
                if successor < values[m][1]:
                    successor = values[m][1]
                    succ_index = m
                l = m + 1
            elif values[m][1] > timestamp:
                r = m - 1
            else:
                return values[m][0]
        
        if succ_index != -1:
            return values[succ_index][0]
        
        return ""

