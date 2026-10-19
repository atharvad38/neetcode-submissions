
class Solution:
    def solve(self, i, s, dp):
        n = len(s)

        if i == n:
            return 1

        if s[i] == '0':
            return 0

        if dp[i] != -1:
            return dp[i]

        # Take one digit
        take_one = self.solve(i + 1, s, dp)

        # Take two digits
        take_two = 0
        if i + 1 < n and 10 <= int(s[i:i+2]) <= 26:
            take_two = self.solve(i + 2, s, dp)

        dp[i] = take_one + take_two
        return dp[i]

    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [-1] * n
        return self.solve(0, s, dp)
