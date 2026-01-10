import os
from random import choice


# creating of game table 
N=5
matrix = [''.join([choice(["·", "#"]) for i in range(N)]) for i in range(N)]


def count_lives(mat: str):
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
            if mat[y][x] == '#':
                lives -= 1
            st += str(lives)
        result += [st]
    
    for i in result:
        print(i)

os.system('clear')
for i in matrix:
    print(i)
print()
count_lives(matrix)
