class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        DIR = [(-1,0),(1,0),(0,1),(0,-1)]
        res = False

        def dfs(r,c,i):
            nonlocal DIR, res
            # print(res)
            if i == len(word):
                return True
            
            # print(res, r, c,i)
            # print(board)
            for dr,dc in DIR:
                nr,nc = r+dr , c+dc
                # print(nr,nc)
                if nr >= 0 and nr < len(board) and nc >= 0 and nc < len(board[0]) and board[nr][nc]==word[i]:
                    # print(word[i])
                    temp = board[nr][nc]
                    board[nr][nc] = "#"
                    # print(r,c,nr,nc,i)
                    # print(board)
                    res = dfs(nr,nc,i+1)
                    board[nr][nc] = temp

            return res

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    board[r][c]="#"
                    res = dfs(r,c,1)
                    board[r][c] = word[0]
        
        return res