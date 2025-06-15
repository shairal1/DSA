# Heap is a complete binary tree that satisfies the heap property.
# The heap property is that the parent node is greater than or equal to the child nodes.
# The heap property is that the parent node is less than or equal to the child nodes.
# The heap property is that the parent node is equal to the child nodes.
# The heap property is that the parent node is greater than or equal to the child nodes.
# The heap property is that the parent node is less than or equal to the child nodes.
# The heap property is that the parent node is equal to the child nodes.
# The heap property is that the parent node is greater than or equal to the child nodes.
# The heap property is that the parent node is less than or equal to the child nodes.
# The heap property is that the parent node is equal to the child nodes.
'''
#question:
-k th smallest element in an array
-k th largest element in an array
-k th smallest element in a stream
-k th largest element in a stream
-k th smallest element in a stream
'''
import heapq
from collections import Counter
from collections import deque
class Heap:
    def kth_smallest(self, nums, k):
        return heapq.nsmallest(k, nums)[-1]

    def kth_smallest_heap(self, nums, k):
        heapq.heapify(nums)
        for i in range(k):
            heapq.heappop(nums)
        return nums[0]
    def kth_smallest_heap_(self, nums, k):
        heap=[]
        for i in range(len(nums)):
            heapq.heappush(heap, nums[i])
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

    def topKFrequent(self, nums, k) :
        counted = Counter(nums)
        min_heap = []
        result = deque()

        for num, count in counted.items():
            heapq.heappush(min_heap, (count, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        for i in range(len(min_heap)):
            result.appendleft(min_heap[i][1])
        return result

if __name__ == "__main__":
    heap = Heap()
    print(heap.kth_smallest_heap_([3, 2, 1, 5, 6, 4], 2))
    print(heap.kth_smallest_heap_([3, 2, 3, 1,], 10))
    print(heap.topKFrequent([1,1,1,2,2,3], 2))