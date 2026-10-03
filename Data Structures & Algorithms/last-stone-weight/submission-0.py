import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxheap = []
        for i in range(len(stones)):
            heapq.heappush(maxheap,-stones[i])
        while maxheap:
            x = heapq.heappop(maxheap)
            x=x*-1
            if not maxheap:
                return x
            y = heapq.heappop(maxheap)
            y=y*-1
            if x==y:
                continue
            elif x<y:
                y=y-x
                heapq.heappush(maxheap,-y)
            else:
                x=x-y
                heapq.heappush(maxheap,-x)
        return 0

        