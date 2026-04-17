class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        
        a = [nums1[i] - nums2[i] for i in range(len(nums1))]
        self.cnt = 0
        
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            
            j = 0
            for i in range(len(left)):
                while j < len(right) and right[j] < left[i] - diff:
                    j += 1
                self.cnt += len(right) - j
            
            
            return merge(left, right)
        
        def merge(left, right):
            result = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
            result.extend(left[i:])
            result.extend(right[j:])
            return result
        
        merge_sort(a)
        return self.cnt