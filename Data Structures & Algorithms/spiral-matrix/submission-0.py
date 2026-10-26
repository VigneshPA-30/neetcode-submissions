class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
            
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]
        d_ind = 0

        lr, lc = len(matrix), len(matrix[0])
        answer = []
        i,j = 0,0
        visited = set()

        for _ in range(lr*lc):

            if (i,j) not in visited :
                answer.append(matrix[i][j])
                visited.add((i,j))

            di, dj = dirs[d_ind]
            next_i = i +  di
            next_j = j +  dj

            if not ((next_i>=0 and next_i<lr) and (next_j>=0 and next_j<lc) and (next_i, next_j) not in visited):
                d_ind = (d_ind+1)%4
                di, dj = dirs[d_ind]

            i += di
            j += dj


        return answer








        