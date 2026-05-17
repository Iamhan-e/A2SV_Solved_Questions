class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        indx1={res:i for i, res in enumerate(list1)}
        min_sum=float('inf')
        result= []

        for i, val in enumerate(list2):
            if val in indx1:
                current= indx1[val]+i
                if current < min_sum:
                    min_sum= current
                    result= [val]
                elif current== min_sum:
                    result.append(val)
        return result

            


        