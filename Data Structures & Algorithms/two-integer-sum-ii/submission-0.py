class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l=0
        r=n-1
        while l<r:
            cur = numbers[l]+numbers[r]
            if cur==target and l!=r:
                return [l+1,r+1]
            if cur<target:
                l+=1
            else:
                r-=1
        
        