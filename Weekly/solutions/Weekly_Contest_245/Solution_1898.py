from typing import List


class Solution_1898:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        low, high = 0, len(removable)
        while low != high:
            mid = (low + high + 1) // 2
            bad = [False for i in range(len(s))]
            for i in removable[:mid]:
                bad[i] = True
            try:
                cur = 0
                for i in p:
                    while bad[cur] or s[cur] != i:
                        cur += 1
                    cur += 1
                low = mid
            except:
                high = mid - 1
        return low
