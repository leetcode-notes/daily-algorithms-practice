class Solution:
    def numRookCaptures(self, board) -> int:
        rook_r, rook_c = 0, 0

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 'R':
                    rook_r, rook_c = i, j
                    break
        count = 0
        for i in range(rook_r+1, len(board)):
            if board[i][rook_c] != "." and board[i][rook_c] != 'p':
                break
            elif board[i][rook_c] == 'p':
                count += 1
                break

        for i in range(rook_r-1, -1, -1):
            if board[i][rook_c] != "." and board[i][rook_c] != 'p':
                break
            elif board[i][rook_c] == 'p':
                count += 1
                break

        for j in range(rook_c+1, len(board[0])):
            if board[rook_r][j] != '.' and board[rook_r][j] != 'p':
                break
            elif board[rook_r][j] == 'p':
                count += 1
                break

        for j in range(rook_c-1, -1, -1):
            if board[rook_r][j] != '.' and board[rook_r][j] != 'p':
                break
            elif board[rook_r][j] == 'p':
                count += 1
                break

        return count


t = [[".", ".", ".", ".", ".", ".", ".", "."],
     [".", ".", ".", "p", ".", ".", ".", "."],
     [".", ".", ".", "R", ".", ".", ".", "p"],
     [".", ".", ".", ".", ".", ".", ".", "."],
     [".", ".", ".", ".", ".", ".", ".", "."],
     [".", ".", ".", "p", ".", ".", ".", "."],
     [".", ".", ".", ".", ".", ".", ".", "."],
     [".", ".", ".", ".", ".", ".", ".", "."]]

s = Solution()
print(s.numRookCaptures(t))


'''
Success
Details
Runtime: 24 ms, faster than 94.22% of Python3
Memory Usage: 13.8 MB, less than 56.04% of Python3
Next challenges:
Shortest Word Distance
Lonely Pixel II
Subarray Sum Equals K
'''
