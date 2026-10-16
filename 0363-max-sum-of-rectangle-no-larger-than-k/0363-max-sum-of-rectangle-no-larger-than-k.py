
from typing import List
from bisect import bisect_left, insort

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        if len(matrix) > len(matrix[0]):
            matrix = [list(row) for row in zip(*matrix)]

        rows, cols = len(matrix), len(matrix[0])
        ans = float('-inf')

        for top in range(rows):
            sums = [0] * cols

            for bottom in range(top, rows):
                for c in range(cols):
                    sums[c] += matrix[bottom][c]

                prefix = 0
                prefixes = [0]

                for x in sums:
                    prefix += x

                    i = bisect_left(prefixes, prefix - k)

                    if i < len(prefixes):
                        ans = max(ans, prefix - prefixes[i])

                    insort(prefixes, prefix)

                    if ans == k:
                        return k

        return ans
