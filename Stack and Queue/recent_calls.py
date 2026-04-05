from collections import deque
class RecentCounter:

    def __init__(self):
        
        self.record= deque()
        

    def ping(self, t: int) -> int:
        self.record.append(t)

        while self.record[0] < t - 3000:
            self.record.popleft()

        return len(self.record) 


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)