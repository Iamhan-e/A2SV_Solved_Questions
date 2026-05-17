class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        n= len(image)

        for r in range(n):
            for c in range(n//2):
                image[r][c], image[r][n-c-1]= image[r][n-c-1], image[r][c]

        for r in range(n):
            for c in range(n):
                if image[r][c] == 1:
                    image[r][c]= 0
                else:
                    image[r][c]= 1

        return image
