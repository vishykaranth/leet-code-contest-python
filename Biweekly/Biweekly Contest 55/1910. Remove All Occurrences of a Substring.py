# https://leetcode.com/contest/biweekly-contest-55/problems/remove-all-occurrences-of-a-substring/
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while True:
            i = s.find(part)
            if i == -1:
                return s
            s = s[:i] + s[i + len(part):]
        return s


s = Solution()
print(s.removeOccurrences('daabcbaabcbc', 'abc'))
print(s.removeOccurrences('axxxxyyyyb', 'xy'))