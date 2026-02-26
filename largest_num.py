class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        arr=[str(num) for num in nums]
        
        arr.sort(key=cmp_to_key (lambda a,b: -1 if a+b > b+a else 1))
        
        if arr[0] == "0":
            return "0"
        
        return "".join(arr)
            
        

       