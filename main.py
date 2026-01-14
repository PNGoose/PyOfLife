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
    
    def random_fill(self):
        self.matrix = [''.join([choice(['·', '#']) for i in range(N)]) for i in range(N)]

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
        flag_next = True
        inp=input('Your command: ')
        while inp:
            if inp[0:3] == 'pos':
                self.pos_com(inp)
            elif inp[0:4] == 'nxco':
                if '+' not in inp:
                    flag_next = False
                self.next_command(inp)
            elif inp[0:3] == 'fis':
                self.finish_command(inp)
            elif inp[0:4] == 'stop':
                self.running = False
            elif inp[0:4] == 'cler':
                self.matrix = ['·' * self.width] * self.width
            elif inp[0:4] == 'help':
                print("pos {x/y/c} - place a cell\n"
                    "nxco {number}- next command gen\n"
                    "fis {number}- set finish gen\n"
                    "stop - stop the game\n"
                    "cler - clear the board")
                sleep(10)
            self.print_console()
            inp=input('Your command: ')

        if flag_next:
            self.next_inp += 10
    
    def pos_com(self, command: str):    
        try:                            # 'pos x/y/c'
            l = command[4:].split('/')  # '012345678'
            x, y, c = int(l[0]), int(l[1]), l[-1]
            if c in '#·':
                new_row = [self.matrix[y][i] if i != x else c for i in range(self.width)]
                self.matrix[y] = ''.join(new_row)
        except Exception:
            pass
    
    def next_command(self, command: str):    
        try: 
            if '+' in command:
                self.next_command += int(command[6:])   # '01234567'
            self.next_inp = int(command[4:])            # 'nxco +67'
        except Exception:
            self.next_inp += 10
    
    def finish_command(self, command: str):
        try:
            self.finish = int(i[4:])
        except Exception: # '0123456'
            pass          # 'fis 500'

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
