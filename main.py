import os
from random import choice
from time import sleep


# creating of game table 
N=10
matrix = [''.join([choice(["·", "#"]) for i in range(N)]) for i in range(N)]


def count_lives(mat: list):
    result = []

    for y in range(len(mat)):
        st = ''
        for x in range(len(mat[y])):
            lives = 0
            neighbours = ''

            # finding the string with neighbours to each point
            if x == 0 and y == 0:
                for i in range(2):
                    neighbours += mat[y + i][x:x + 2]
            
            elif x == 0 and y == N - 1:
                for i in range(-1, 1):
                    neighbours += mat[y + i][x:x + 2]

            elif x == 0:
                for i in range(-1, 2):
                    neighbours += mat[y + i][x: x + 2]

            elif y == 0:
                for i in range(2):
                    neighbours += mat[y + i][x - 1:x + 2]

            elif y == N - 1:
                for i in range(-1, 1):
                    neighbours += mat[y + i][x -1:x + 2]

            else:
                for i in range(-1, 2):
                    neighbours += mat[y + i][x - 1:x + 2]
            
            lives += neighbours.count('#')
            # we shouldn't count ourself
            if mat[y][x] == '#':
                lives -= 1
            st += str(lives)
        result += [st]
    
    return result


def recounting(mat_orig: list, mat_counted: list): 
    result = []
    for x in range(len(mat_orig)):
        st = ''
        for y in range(len(mat_orig)):            
            if mat_orig[x][y] == '·':
                if mat_counted[x][y] == '3':
                    st += '#'
                else:
                    st += '·'

            elif mat_orig[x][y] == '#':
                if mat_counted[x][y] not in ['2', '3']:
                    st += '·'
                else:
                    st += '#'
        result.append(st)
    for i in result:
        print(i)


os.system('clear')
for i in matrix:
    print(i)
print()
c = count_lives(matrix)
recounting(matrix, c)
