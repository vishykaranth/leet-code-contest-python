from typing import List


class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            x = nums[:i] + nums[i + 1:]
            flag = True
            for j in range(1, len(x)):
                if x[j] <= x[j - 1]:
                    flag = False
                    break
            if flag:
                return True
        return False


s = Solution()
print(s.canBeIncreasing([1, 2, 10, 5, 7]))
print(s.canBeIncreasing([2, 3, 1, 2]))
print(s.canBeIncreasing([1, 1, 1]))
