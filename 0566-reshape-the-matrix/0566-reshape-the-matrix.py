class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        if m * n != r * c:
            return mat
        
        flattened = [val for row in mat for val in row]
        
        ans = []
        for i in range(r):
            ans.append(flattened[i * c : (i + 1) * c])
            
        return ans