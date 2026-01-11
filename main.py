import os
from random import choice
from time import sleep
from sys import stdin


# creating of game table 
class GameOfLife:
    def __init__(self, N: int, finish: int, mode=0):
        self.width = N
        self.matrix = [''.join([choice(['·', '#']) for i in range(N)]) for i in range(N)]
        self.gen = 0
        self.finish = finish
        self.next_inp = 10
        self.running = True

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

    def commands(self):
        print('Command GEN')
        inp = stdin.read().lower().split('\n')
        print(inp)
        flag_next = True
        for i in inp:
            self.print_console()
            if i[0:3] == 'pos':
                print(i[4:])
                try:
                    x, y, c = i[4:].split('/')
                    x, y = int(x), int(y)
                    self.matrix[y] = ''.join([self.matrix[y][i] if i != x else c for i in range(self.width)])
                except Exception:
                    print("WRONG POS COMMAND - TYPE LIKE pos x/y/c - pos 1/2/#")
            elif i[0:4] == 'nxco':
                flag_next = False
                try:
                    self.next_inp = int(i[4:])
                except Exception:
                    print('INPUT THE NUMBER')
                print(self.next_inp, i[4:])
            elif i[0:3] == 'fis':
                try:
                    self.finish = int(i[3:])
                except Exception:
                    print('INPUT THE NUMBER')
            elif i[0:4] == 'stop':
                self.running = False
            elif i[0:4] == 'cler':
                self.matrix = ['·' * self.width] * self.width
            elif i[0:4] == 'help':
                print("pos {x/y/c} - place a cell\n"
                      "nsco {number}- next command gen\n"
                      "fis {number}- set finish gen\n"
                      "stop - stop the game\n"
                      "cler - clear the board")
                sleep(10)

        if flag_next:
            self.next_inp += 10

    def print_console(self):
        os.system('clear')
        print('PyOfLife'.center(self.width, '|'))
        print(f'finish={self.finish}')
        population = 0
        for i in self.matrix:
            print(i)
            population += i.count('#')
        print('|' * self.width)
        print(f'Generation: {self.gen}')
        print(f'Population: {population}')
        sleep(0.5)

    def loop(self):
        self.gen += 1
        self.print_console()
        if self.gen == self.next_inp:
            self.commands()
        self.recounting()
        if self.gen >= self.finish:
            self.running = False


Game=GameOfLife(N=20, finish=50)
while Game.running:
    Game.loop()
