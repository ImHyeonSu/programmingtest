from heapq import heappush, heappop
class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.min_heap = []
        for num in nums:
            self.add(num)
        

    def add(self, val: int) -> int:
        heappush(self.min_heap, val)
        if len(self.min_heap) > self.k:
            heappop(self.min_heap)
        return self.min_heap[0]


commands = ["KthLargest", "add", "add", "add", "add", "add"]
values = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

result = []

kth_largest = KthLargest(values[0][0], values[0][1])
result.append(None)


for i in range(1, len(commands)):
    result.append(kth_largest.add(values[i][0]))
print(result)