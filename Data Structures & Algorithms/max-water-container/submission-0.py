class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        r = n-1
        l = 0
        ans = 0
        while l<r:
            h = min(heights[l],heights[r])
            w = r-l
            cur = h*w
            ans = max(ans,cur)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return ans

        