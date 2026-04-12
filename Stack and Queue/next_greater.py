class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nge= {n:i for i, n in enumerate(nums1)}

        res= [-1] * len(nums1)
        stack= []

        for i in range(len(nums2)):
            
            while stack and stack[-1] < nums2[i]:
                cut= stack.pop()
                indx= nge[cut]
                res[indx]= nums2[i]
            
            if nums2[i] in nums1:
                stack.append(nums2[i])

        return res
