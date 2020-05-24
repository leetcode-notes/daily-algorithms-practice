from typing import DefaultDict, List
from collections import defaultdict


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        fir = votes[0]
        mark: List[List] = [
            [0 for i in range(len(fir))] for j in range(len(fir))]

        for vote in votes:
            for i in range(len(vote)):
                char_idx = fir.index(vote[i])
                mark[char_idx][i] += 1

        for i in range(len(mark)):
            mark[i].append(fir[i])

        s = sorted(mark, key=lambda x: x[len(fir)])
        print(s)
        s = sorted(s, key=lambda x: x[:len(fir)], reverse=True)
        print(s)

        ans = ""
        for x in s:
            ans += x[len(fir)]

        return ans

# failed due to misunderstanding of problem


class Solutionold:
    def rankTeams(self, votes: List[str]) -> str:
        vote_count = {}

        for vote in votes:
            cur_score = len(votes[0])
            for i, letter in enumerate(vote):
                score = cur_score - i
                vote_count[letter] = vote_count.get(letter, 0) + score
        score_to_team: DefaultDict[int, List[str]] = defaultdict(list)

        for team, score in vote_count.items():
            score_to_team[score].append(team)
        max_score = len(votes[0])*len(votes)
        res: List[str] = []

        while max_score > 0:
            if max_score in score_to_team:
                for team in sorted(score_to_team[max_score]):
                    res.append(team)
            max_score -= 1
        return "".join(res)


votes = ["WXYZ", "XYZW"]
votes1 = ["M", "M", "M", "M"]
votes2 = ["FVSHJIEMNGYPTQOURLWCZKAX", "AITFQORCEHPVJMXGKSLNZWUY", "OTERVXFZUMHNIYSCQAWGPKJL", "VMSERIJYLZNWCPQTOKFUHAXG", "VNHOZWKQCEFYPSGLAMXJIUTR", "ANPHQIJMXCWOSKTYGULFVERZ", "RFYUXJEWCKQOMGATHZVILNSP", "SCPYUMQJTVEXKRNLIOWGHAFZ", "VIKTSJCEYQGLOMPZWAHFXURN", "SVJICLXKHQZTFWNPYRGMEUAO", "JRCTHYKIGSXPOZLUQAVNEWFM",
          "NGMSWJITREHFZVQCUKXYAPOL", "WUXJOQKGNSYLHEZAFIPMRCVT", "PKYQIOLXFCRGHZNAMJVUTWES", "FERSGNMJVZXWAYLIKCPUQHTO", "HPLRIUQMTSGYJVAXWNOCZEKF", "JUVWPTEGCOFYSKXNRMHQALIZ", "MWPIAZCNSLEYRTHFKQXUOVGJ", "EZXLUNFVCMORSIWKTYHJAQPG", "HRQNLTKJFIEGMCSXAZPYOVUW", "LOHXVYGWRIJMCPSQENUAKTZF", "XKUTWPRGHOAQFLVYMJSNEIZC", "WTCRQMVKPHOSLGAXZUEFYNJI"]

s = Solution()
print(s.rankTeams(votes))
