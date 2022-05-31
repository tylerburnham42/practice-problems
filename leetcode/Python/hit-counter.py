# 362. Design Hit Counter
# https://leetcode.com/problems/design-hit-counter/submissions/


class HitCounter:

    def __init__(self):
        self.queue = []

    def hit(self, timestamp: int) -> None:

        self.queue.append(timestamp)
        #print(self.queue)

    def getHits(self, timestamp: int) -> int:
        #print(timestamp, self.queue[0])
        while self.queue and timestamp - self.queue[0] >= 300:
            #print(timestamp, self.queue[0])
            self.queue.pop(0)
        #print(self.queue) 
        return len(self.queue)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)