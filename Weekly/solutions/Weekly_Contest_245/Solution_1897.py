from collections import defaultdict
from typing import List


class Solution_1897:
    def makeEqual(self, words: List[str]) -> bool:
        c = defaultdict(int)
        for i in words:
            for j in i:
                c[j] += 1
        return all(i % len(words) == 0 for i in c.values())
