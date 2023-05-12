import time
import sys

inicio = time.time()
class KnightsTour:
    def __init__(self, width, height):
        self.w = width
        self.h = height

        self.board = []
        self.generate_board()

    def generate_board(self):
        for i in range(self.h):
            self.board.append([0]*self.w)

    def print_board(self):
        for elem in self.board:
            print (elem)
    def generate_legal_moves(self, cur_pos):
        possible_pos = []
        move_offsets = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                        (2, 1), (2, -1), (-2, 1), (-2, -1)]

        for move in move_offsets:
            new_x = cur_pos[0] + move[0]
            new_y = cur_pos[1] + move[1]
            if (new_x >= self.h):
                continue
            elif (new_x < 0):
                continue
            elif (new_y >= self.w):
                continue
            elif (new_y < 0):
                continue
            else:
                possible_pos.append((new_x, new_y))

        return possible_pos

    def sort_lonely_neighbors(self, to_visit):
        neighbor_list = self.generate_legal_moves(to_visit)
        empty_neighbours = []

        for neighbor in neighbor_list:
            np_value = self.board[neighbor[0]][neighbor[1]]
            if np_value == 0:
                empty_neighbours.append(neighbor)

        scores = []
        for empty in empty_neighbours:
            score = [empty, 0]
            moves = self.generate_legal_moves(empty)
            for m in moves:
                if self.board[m[0]][m[1]] == 0:
                    score[1] += 1
            scores.append(score)

        scores_sort = sorted(scores, key = lambda s: s[1])
        sorted_neighbours = [s[0] for s in scores_sort]
        return sorted_neighbours

    def tour(self, n, path, to_visit):
        self.board[to_visit[0]][to_visit[1]] = n
        path.append(to_visit)
        if n == self.w * self.h: 
            self.print_board()
            sys.exit(1)

        else:
            sorted_neighbours = self.sort_lonely_neighbors(to_visit)
            for neighbor in sorted_neighbours:
                self.tour(n+1, path, neighbor)

            self.board[to_visit[0]][to_visit[1]] = 0
            try:
                path.pop()
            except IndexError:
                print ("No path found")
                sys.exit(1)
time.sleep(1)

fin = time.time()

print(fin-inicio)
if __name__ == '__main__':
    kt = KnightsTour(5, 5)
    kt.tour(1, [], (2,2))
    
    
    kt.print_board()
    
