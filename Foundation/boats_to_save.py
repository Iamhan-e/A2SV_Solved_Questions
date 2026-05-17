class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        left= 0
        right= len(people)-1
        cnt=0   

        while left <= right:
            if left== right:
                cnt+=1
                break

            if people[left]+ people[right] <= limit:
                cnt+=1
                left+=1
                right-=1
            else:
                cnt+=1
                right-=1
        return cnt


