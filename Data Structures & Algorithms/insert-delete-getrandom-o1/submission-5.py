import random, collections
class RandomizedSet:

    def __init__(self):
        self.array = []
        self.values = {}
        

    def insert(self, val: int) -> bool:
        if val in self.values:
            return False
        self.array.append(val)
        self.values[val] = len(self.array) - 1

        return True

    def remove(self, val: int) -> bool:
        if val not in self.values:
            return False
        idx = self.values[val]
        self.values[self.array[-1]] = idx
        self.array[idx], self.array[-1] = self.array[-1], self.array[idx]
        self.array.pop()
        del self.values[val]
        
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.array)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()