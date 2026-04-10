class Solution:
    import bisect
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        houses.sort()
        heaters.sort()
        rad=0
        for house in houses:
            indx= bisect.bisect_left(heaters, house)

            if indx == 0:
                dis= abs(heaters[0]- house)
            elif indx== len(heaters):
                dis= abs(heaters[-1]- house)
            else:
                dis= min(heaters[indx]- house, house - heaters[indx-1] )

            rad= max(rad, dis)
        return rad