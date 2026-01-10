import os
from random import choice


# creating of game table 
N=10
matrix = '\n'.join([''.join([choice(["·", "#"]) for i in range(N)]) for i in range(N)])


os.system('clear')
print(matrix)
#for i in matrix:
#    print(*i)
