# 380. Insert Delete GetRandom O(1)
# https://leetcode.com/problems/insert-delete-getrandom-o1/
# Solved 5-26-2022


class RandomizedSet:

    def __init__(self):
        self.items = []
        self.item_lookup = {}
        

    def insert(self, val: int) -> bool:
        if val in self.item_lookup:
            return False
        else:
            self.items.append(val)
            self.item_lookup[val] = len(self.items)-1
            return True

    def remove(self, val: int) -> bool:
        if val in self.item_lookup:
            position = self.item_lookup.pop(val)
            last_item = self.items.pop()
            if position != len(self.items):
                self.items[position] = last_item
                self.item_lookup[last_item] = position
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.items)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()