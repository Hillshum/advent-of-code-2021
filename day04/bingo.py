lines = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""

with open('input.txt', 'r') as f:
    lines = f.read()


def parse_board(board_string, move_list):
    rows = filter(len, board_string.split('\n'))
    return [[*map(lambda x: move_list[int(x)], r.split())] for r in rows]

def score_board(board):
    scores = []
    for i in board:
        scores.append(max(i))

    # print(board)

    for col_index in range(len(board[0])):
        col = []
        for row in board:
            col.append(row[col_index])

        scores.append(max(col))

    return min(scores)

def get_total(board, moves):
    flatted = [food for sublist in board for food in sublist]
    score = score_board(board)
    print(score)
    unmarked = filter(lambda x: x> score, flatted)
    print(unmarked)
    unmarked_vals = [*map(lambda x: moves[x], unmarked) ]
    print(unmarked_vals)
    return moves[score] * sum(unmarked_vals)

print(lines)
sp = lines.split('\n\n')
moves = [*map(int, sp[0].split(','))]


indexed_moves = [m for m in enumerate(moves)]
indexed_moves.sort(key=lambda x: x[1])
# print(indexed_moves)
sorted_moves = [move for move,order in indexed_moves]
# print(sorted_moves)


boards = [parse_board(board, sorted_moves) for board in sp[1:]]
# print(boards)

scored_boards = sorted( boards, key=score_board, reverse=False)
winning_board = scored_boards[0]
print(winning_board)
losing_board = scored_boards[-1]
losing_total = get_total(losing_board, moves)
total = get_total(winning_board, moves)

print(total, losing_total)
