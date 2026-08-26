class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        imap={}
        for i in range(n):
            
            if target-nums[i] in imap:
                e=imap[target-nums[i]]
                if i!=e:
                    return [e,i]
            imap[nums[i]]=i
        
                

            
        
        