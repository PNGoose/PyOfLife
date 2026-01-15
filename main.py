import os
from random import choice
from time import sleep
from sys import argv


# creating of game table 
class GameOfLife:
    def __init__(self, N: int, finish: int, mode=0):
        self.width = 30
        self.heigh = 20
        self.matrix = [''.join([choice(['·', '#']) for i in range(self.width)]) for i in range(self.heigh)]
        self.gen = 0
        self.finish = finish
        self.next_inp = 10
        self.running = True
    
    def game_control(self, mode: int):
        if mode == 0:
            self.running = False
        elif mode == 1:
            self.matrix = ['·' * self.width] * self.heigh
        elif mode == 2:
            self.matrix = [''.join([choice(['·', '#']) for i in range(self.width)]) for i in range(self.heigh)]

    def count_lives(self):
        result = []
        for y in range(self.heigh):
            st = ''
            for x in range(self.width):
                lives = 0
                neighbours = ''
                # finding the string with neighbours to each point
                if x == 0 and y == 0:
                    for i in range(2):
                        neighbours += self.matrix[y + i][x:x + 2]
                elif x == 0 and y == self.heigh - 1:
                    for i in range(-1, 1):
                        neighbours += self.matrix[y + i][x:x + 2]
                elif x == 0:
                    for i in range(-1, 2):
                        neighbours += self.matrix[y + i][x: x + 2]
                elif y == 0:
                    for i in range(2):
                        neighbours += self.matrix[y + i][x - 1:x + 2]
                elif y == self.heigh - 1:
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
        return result

    def recounting(self):
        mat_numbered = self.count_lives()
        result = []
        for y in range(0, self.heigh):
            st = ''
            for x in range(0, self.width):    
                if self.matrix[y][x] == '·':
                    if mat_numbered[y][x] == '3':
                        st += '#'
                    else:
                        st += '·'
                elif self.matrix[y][x] == '#':
                    if mat_numbered[y][x] not in ['2', '3']:
                        st += '·'
                    else:
                        st += '#'
            result.append(st)
        self.matrix = result

    def commands(self):
        while (inp:=input('Your command: ').strip()):
            if inp[0:3] == 'pos':
                self.pos_commmand(inp)
            elif inp[0:4] == 'nxco':
                self.next_command(inp)
            elif inp[0:3] == 'fis':
                self.finish_command(inp)
            elif inp[0:4] == 'stop':
                self.game_control(0)
                break
            elif inp[0:4] == 'cler':
                self.game_control(1)
            elif inp[0:4] == 'help':
               self.help_command()
            self.print_console()
    
    def pos_commmand(self, command: str):    
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
                self.next_inp += int(command[6:])   # '01234567'
            self.next_inp = int(command[4:])            # 'nxco +67'
        except Exception:
            pass
    
    def finish_command(self, command: str):
        try:
            self.finish = int(command[3:])
        except Exception: # '0123456'
            pass          # 'fis 500'

    def help_command(self):
        print("\npos {x/y/c} - place a cell\n"
            "nxco {number}- next command gen\n"
            "fis {number}- set finish gen\n"
            "stop - stop the game\n"
            "cler - clear the board")
        sleep(10)

    def print_console(self):
        os.system('clear')
        print('PyOfLife'.center(self.width, '|'))
        print(f'finish={self.finish} next command - {self.next_inp}')
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
        if self.next_inp <= self.gen:
            self.next_inp = self.gen + 10


Game=GameOfLife(N=20, finish=50)
while Game.running:
    Game.loop()
