import math
import os
import csv
MY_DIR = os.path.dirname(os.path.realpath(__file__))
MY_CONFIG_FILE = 'robot.map.20x20.csv'

def inport_map(input_filename):

    final_board = []
    board = []
    with open(input_filename, 'r') as f:
        csv_board_start = csv.reader(f)
        for row in csv_board_start:
            if len(row) == 2:
                starting_position = (int(row[0])+1), (int(row[1])+1)
            elif len(row) == 1:
                num_moves = int(row[0])
            else:
                board.append(row)
        length = len(board[0])
        height = len(board)
        for i in range (length + 2):
            final_board_row = []
            for j in range (height + 2):
                if i == 0 or i == (height+1) or j == 0 or j == (length+1):
                    final_board_row.append(None)
                else:
                    final_board_row.append(int(board[i-2][j-2]))
            final_board.append(final_board_row)

    return final_board, starting_position, num_moves

#board, starting_position, num_moves = inport_map(MY_DIR + '/' + MY_CONFIG_FILE)
#for row in board:
#    print(row)
#print(starting_position, num_moves)


def find_max_of_surroundings(a,b, board):
    max = 0
    #print(board[a][b])
    for i in range(-1,2):
        for j in range(-1,2):
            #print(board[i+a][j+b])
            #print(i,j)
            if i == 0 and j == 0:
                pass
            elif board[a+i][b+j] == None:
                pass
            else:
                if board[a+i][b+j] > max:
                    max = board[a+i][b+j]
                    #print(max, i, j, a, b)
                    max_i = i
                    max_j = j
                    #print(max_i, max_j, 'max i,j')
    return max_i + a, max_j + b, max_i, max_j




def main_robot(input_filename):
    outputlist = list()
    board, starting_position, num_moves = inport_map(input_filename)
    x_position, y_position = starting_position
    score_counter = 0
    score_counter = board[x_position][y_position]
    for moves in range(num_moves+1):
        #print(x_position, y_position, board[x_position][y_position])
        new_x, new_y, max_i, max_j = find_max_of_surroundings(x_position, y_position, board)
        #print(score_counter)

        board[x_position][y_position] = 0
        x_position, y_position = new_x, new_y
        score_counter += board[x_position][y_position]
        outputlist.append((max_i,max_j))
        for row in board:
            #print(row)
            pass
    return outputlist
#do you count starting position?
#minimum size of chart
filenamein  = MY_DIR + '/' + MY_CONFIG_FILE
filenameout = MY_DIR + '/' + 'outputfile.txt'
outputlist = main_robot(filenamein)


with open(filenameout, 'w') as outputfile:
    outputfile.write('row,col')
    outputfile.write('\n')
    for row in outputlist:
        outputfile.write(str(row[0]))
        outputfile.write(', ')
        outputfile.write(str(row[1]))
        outputfile.write('\n')
