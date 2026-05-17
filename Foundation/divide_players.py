class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n= len(skill)

        tot= 0
        team_skill= skill[0]+ skill[-1]

    
        for i in range(n//2):
            if skill[i]+ skill[-i-1] != team_skill:
                return -1

            tot+= (skill[i] * skill[n-i-1])

        return tot