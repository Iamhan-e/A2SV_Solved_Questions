import random
class RandomizedSet:

    def __init__(self):
        self.rand= set()
        
    def insert(self, val: int) -> bool:
        self.val= val
        if val not in self.rand:
            self.rand.add(val)
            return True
        else:
            return False
    def remove(self, val: int) -> bool:
        self.val= val
        if val in self.rand:
            self.rand.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(list(self.rand))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()