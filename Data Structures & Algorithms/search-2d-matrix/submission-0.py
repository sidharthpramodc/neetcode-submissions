class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top,bottom= 0,len(matrix)-1
        while top<=bottom:
            mid1 = (top + bottom)//2
            if matrix[mid1][0] > target:
                bottom = mid1 - 1
            elif matrix[mid1][-1] < target:
                top = mid1 + 1
            else: break
        # if not (top <= bottom):
        #     return False
        # mid1 = (top + bottom) // 2

        left ,right = 0, len(matrix[0])-1
        while left<=right:
            mid2 = (left + right)//2
            if matrix[mid1][mid2]<target:
                left = mid2+1
            elif matrix[mid1][mid2]>target:
                right = mid2-1
            else: 
                return True
        return False