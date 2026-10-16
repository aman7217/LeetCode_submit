
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        import bisect

        tails = []

        for num in nums:
            i = bisect.bisect_left(tails, num)

            if i == len(tails):
                tails.append(num)
            else:
                tails[i] = num

        return len(tails)
