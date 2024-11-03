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

