class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        ans=0
        for num in nums:
            if (num-1) not in numset:
                l=0
                while num+l in numset:
                    l+=1
                ans = max(l,ans)
        return ans

        