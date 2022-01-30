import copy
import pprint

def checkValid(row, col, board):
    for curr_row in range(row):
        if board[curr_row][col] == 'Q':
            return False

    for curr_col in range(col):
        if board[row][curr_col] == 'Q':
            return False

     #check the left diagonal
    curr_row = row
    curr_col = col
    while curr_row>= 0 and curr_col>= 0:
        if board[curr_row][curr_col] == 'Q':
            return False
        curr_row-=1
        curr_col-=1


    curr_row = row
    curr_col = col
    while curr_row >= 0 and curr_col < len(board[row]):
        if board[curr_row][curr_col] == 'Q':
            return False
        curr_row-=1
        curr_col+=1

    return True



def queens(n=8):
    def helper(row, board):
        if row == n:
            arragements.append(copy.deepcopy(board))
        else:
            for col in range(len(board[row])):
                #print("Trying", row, col)
                if checkValid(row, col, board):
                    board[row][col] = 'Q'
                    #print(row, col)
                    helper(row + 1, copy.deepcopy(board))
                    board[row][col] = '.'


    arragements = []
    board = [["." for _ in range(8)] for _ in range(8)]
    helper(0, board)
    return arragements

if __name__ == "__main__":
    q = queens()
    pprint.pprint(q)