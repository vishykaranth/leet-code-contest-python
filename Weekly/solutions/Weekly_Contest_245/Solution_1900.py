from typing import List


class Solution_1900:
    def earliestAndLatest(self, n: int, p1: int, p2: int) -> List[int]:
        players = list(range(1, n + 1))

        def helper(players):
            m = len(players)
            if players.index(p1) + players.index(p2) == m - 1:
                return [1, 1]
            # otherwise, they don't play each other
            matches = []
            for i in range(m // 2):
                if players[i] != p1 and \
                        players[i] != p2 and \
                        players[-i - 1] != p1 and \
                        players[-i - 1] != p2:  # dont count matches from p1,p2
                    matches.append((players[i], players[-i - 1]))
            auto = [p1, p2]
            if m % 2 == 1 and players[m // 2] not in auto:
                auto.append(players[m // 2])
            res = None
            for mask in range(1 << len(matches)):
                winners = auto + [matches[i][(mask >> i) & 1] for i in range(len(matches))]
                winners.sort()
                tmp = helper(winners)
                if res is None:
                    res = [tmp[0] + 1, tmp[1] + 1]
                else:
                    res[0] = min(res[0], 1 + tmp[0])
                    res[1] = max(res[1], 1 + tmp[1])
            return res

        return helper(players)
