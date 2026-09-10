class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subs = []
        n = len(nums)
        def solve(i):
            if i==n:
                ans.append(subs.copy())
                return
            subs.append(nums[i])
            solve(i+1)
            subs.pop()
            solve(i+1)
        solve(0)
        return ans

        