class Solution:
    def numRookCaptures(self, board):
        """
        在一个 8 x 8 的棋盘上，有一个白色车（rook）。也可能有空方块，白色的象（bishop）和黑色的卒（pawn）。它们分别以字符 “R”，“.”，“B” 和 “p” 给出。大写字符表示白棋，小写字符表示黑棋。
        车按国际象棋中的规则移动：它选择四个基本方向中的一个（北，东，西和南），然后朝那个方向移动，直到它选择停止、到达棋盘的边缘或移动到同一方格来捕获该方格上颜色相反的卒。另外，车不能与其他友方（白色）象进入同一个方格。
        返回车能够在一次移动中捕获到的卒的数量。
        """
        B = list()
        p = list()
        # for row in board:
        #     for col in range(len(row)):
        #         if row[col]=="R":
        #             R=[board.index(row),col]
        #         if row[col]=="B":
        #             B.append([board.index(row),col])
        #         if row[col]=="p":
        #             p.append([board.index(row),col])
        count = 0
        for i in range(len(board)):
            if "R" in board[i]:
                j = board[i].index("R")
                for l in range(j,0,-1):
                    if board[i][l]=="p":
                        count += 1
                        break
                    elif board[i][l]=="B":
                        break
                for r in range(j,len(board[i])):
                    if board[i][r] == "p":
                        count += 1
                        break
                    elif board[i][r]=="B":
                        break
                for u in range(i,0,-1):
                    if board[u][j] == "p":
                        count += 1
                        break
                    elif board[u][j]=="B":
                        break
                for p in range(i,len(board)):
                    if board[p][j] == "p":
                        count += 1
                        break
                    elif board[p][j]=="B":
                        break

                


        return count

sol = Solution()
board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
print(sol.numRookCaptures(board))