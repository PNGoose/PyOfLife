import os
from random import choice
from time import sleep


# creating of game table 
class GameOfLife:
    def __init__(self, N: int):
        self.width = N
        self.matrix = [''.join([choice(['·', '#']) for i in range(N)]) for i in range(N)]
        self.gen = 0

    def count_lives(self):
        result = []
        for y in range(self.width):
            st = ''
            for x in range(self.width):
                lives = 0
                neighbours = ''
                # finding the string with neighbours to each point
                if x == 0 and y == 0:
                    for i in range(2):
                        neighbours += self.matrix[y + i][x:x + 2]
                elif x == 0 and y == self.width - 1:
                    for i in range(-1, 1):
                        neighbours += self.matrix[y + i][x:x + 2]
                elif x == 0:
                    for i in range(-1, 2):
                        neighbours += self.matrix[y + i][x: x + 2]
                elif y == 0:
                    for i in range(2):
                        neighbours += self.matrix[y + i][x - 1:x + 2]
                elif y == self.width - 1:
                    for i in range(-1, 1):
                        neighbours += self.matrix[y + i][x -1:x + 2]
                else:
                    for i in range(-1, 2):
                        neighbours += self.matrix[y + i][x - 1:x + 2]
                # we shouldn't count ourself
                if self.matrix[y][x] == '#':
                    lives -= 1
                lives += neighbours.count('#')
                st += str(lives)
            result += [st]
        self.mat_numbered = result

    def recounting(self):
        self.count_lives()
        result = []
        for x in range(self.width):
            st = ''
            for y in range(self.width):            
                if self.matrix[x][y] == '·':
                    if self.mat_numbered[x][y] == '3':
                        st += '#'
                    else:
                        st += '·'
                elif self.matrix[x][y] == '#':
                    if self.mat_numbered[x][y] not in ['2', '3']:
                        st += '·'
                    else:
                        st += '#'
            result.append(st)
        self.matrix = result

    def commands(self, inp):
        pass

    def loop(self):
        os.system('clear')
        print('PyOfLife'.center(self.width, '-'))
        self.gen += 1
        for i in self.matrix:
            print(i)
        print('-' * self.width)
        print(f'Generation: {self.gen}')
        self.recounting()


Game=GameOfLife(20)
for i in range(50):
    Game.loop()
    sleep(1)
