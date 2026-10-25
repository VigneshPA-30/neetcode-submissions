class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = collections.deque()
        # maxtime = 0
        R,C = len(grid)-1, len(grid[0])-1
        DIR = [(-1,0),(1,0),(0,-1),(0,1)]

        for i in range(R+1):
            for j in range(C+1):
                if grid[i][j]==0:
                    q.append((i,j,0))

        while q:
            r,c,d = q.popleft()
            # maxtime = max(maxtime, t)
            for i,j in DIR:
                nr,nc = r+i,c+j
                if nr>=0 and nr<=R and nc>=0 and nc<=C and grid[nr][nc]==2147483647:
                    grid[nr][nc] = min(grid[nr][nc], d+1)
                    q.append((nr,nc,grid[nr][nc]))


        # for i in range(R+1):
        #     for j in range(C+1):
        #         print(i,j)
        #         if grid[i][j]==1:
        #             return -1

        # print(grid)
        # return maxtime
        