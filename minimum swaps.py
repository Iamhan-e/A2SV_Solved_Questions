class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        cnt = Counter(s1+s2)

        if cnt['x'] % 2 != 0 or cnt['y']%2 != 0:
            return -1

        d= defaultdict(int)

        for i, j in zip(s1, s2):
            if i !=j:
                d[i+j]+=1
        res=0
        for val in d.values():
            res += val//2 +1 if val % 2 else val//2

        return res



            

       

       

                    