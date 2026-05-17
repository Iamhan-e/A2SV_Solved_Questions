class Solution:
    def isHappy(self, n: int) -> bool:
        exist= set()

        while n!=1 and n not in exist:
            exist.add(n)

            n= sum(int(digit)**2 for digit in str(n))
        return n==1
        

            