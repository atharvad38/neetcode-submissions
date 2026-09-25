# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         even = 0
#         odd = 0
#         n = len(nums)
#         for i in range(n):
#             if i%2==0:
#                 even+=nums[i]
#             else:
#                 odd+=nums[i]
#         # return max(even,odd)

class Solution:
    def solve(self,i,prev,nums,dp):
        if i>=len(nums):
            return 0
        if (i,prev) in dp:
            return dp[(i,prev)]
        take = 0
        if prev!=i-1:
            take = nums[i]+self.solve(i+2,i,nums,dp)
        not_take = self.solve(i+1,prev,nums,dp)
        dp[(i,prev)]=max(take,not_take)
        return dp[(i,prev)]
    def rob(self, nums: List[int]) -> int:
        dp={}
        return self.solve(0,-2,nums,dp)
            
        
            
        