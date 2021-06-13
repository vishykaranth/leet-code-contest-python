from typing import List


class Solution_1899:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a = b = c = 0
        for i in triplets:
            if all(i[j] <= target[j] for j in range(3)):
                a = max(a, i[0])
                b = max(b, i[1])
                c = max(c, i[2])
        return a == target[0] and b == target[1] and c == target[2]
