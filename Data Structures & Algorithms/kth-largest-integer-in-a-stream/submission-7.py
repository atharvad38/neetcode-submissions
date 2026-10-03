import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap = []
        self.k = k
        if nums:
            nums.sort(reverse=True)
            n = min(k,len(nums))
            for i in range(n):
                heapq.heappush(self.minheap,nums[i])
        

    def add(self, val: int) -> int:

        heapq.heappush(self.minheap,val)
        n=len(self.minheap)
        if n<self.k:
            return -1
        elif n==self.k:
            ans=heapq.heappop(self.minheap)
            heapq.heappush(self.minheap,ans)
            return ans
        else:
            heapq.heappop(self.minheap)
            ans = heapq.heappop(self.minheap)
            heapq.heappush(self.minheap,ans)
            return ans

        
