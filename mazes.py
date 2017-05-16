'''
toy maze solver
'''

def solve_maze(maze, x, y):
    ''' find all paths from coord to exit '''
    solutions = []
    solve_maze_recurse(maze, x, y, [], solutions)
    return solutions

def solve_maze_recurse(maze, x, y, path, paths):
    ''' dfs maze solver '''
    if maze[y][x] == 'E':
        paths.append(path)
        return paths
    visitable = [n for n in legal_neighbours(maze, x, y) if n not in path]
    for neighbour in visitable:
        maze[neighbour[1]][neighbour[0]]
        new_path = path + [neighbour]
        solve_maze_recurse(maze, neighbour[0], neighbour[1], new_path, paths)

def neighbours(maze, x, y):
    '''
    returns all neighbouring squares
    NNN
    N_N
    NNN
    '''
    maze_height = len(maze)
    maze_width = len(maze[0])
    squares = []
    if x > 0:
        squares.append((x-1, y))
    if x < maze_width - 1:
        squares.append((x+1, y))
    if y > 0:
        squares.append((x, y-1))
    if y < maze_height - 1:
        squares.append((x, y+1))
    return squares

def legal_neighbours(maze, x, y):
    ''' returns neighbours that are open '''
    return [n for n in neighbours(maze, x, y) if maze[n[1]][n[0]] in (' ', 'E')]

def main():
    maze = [
        [' ', '#', ' ', ' ', ' '],
        [' ', '#', ' ', '#', ' '],
        [' ', '#', ' ', '#', ' '],
        [' ', ' ', ' ', ' ', 'E'],
    ]

    solutions = solve_maze(maze, 0, 0)
    for s in solutions:
        print(s)

if __name__ == '__main__':
    main()
