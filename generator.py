import random
import numpy as np
import os

def MakeSudoku():
    grid = [[0 for x in range(9)] for y in range(9)] 
    for i in range(9):
        for j in range(9):
            grid[i][j] = 0
            
    # The range here is the amount
    # of numbers in the grid
    for i in range(5):
        #choose random numbers
        row = random.randrange(9)
        col = random.randrange(9)
        num = random.randrange(1,10)
        while(not CheckValid(grid,row,col,num) or grid[row][col] != 0): #if taken or not valid reroll
            row = random.randrange(9)
            col = random.randrange(9)
            num = random.randrange(1,10)
        grid[row][col]= num;
        
    Printgrid(grid)
    
 
def Printgrid(grid):
    TableTB = "|--------------------------------|"
    TableMD = "|----------+----------+----------|"
    print(TableTB)
    for x in range(9):
        for y in range(9):
            if ((x == 3 or x == 6) and y == 0):
                print(TableMD)
            if (y == 0 or y == 3 or y== 6):
                print("|", end=" ")
            print(" " + str(grid[x][y]), end=" ")
            if (y == 8):
                print("|")
    print(TableTB)
    def possible(row, column, number):
        #Is the number appearing in the given row?
        for i in range(0,9):
            if grid[row][i] == number:
                return False

        #Is the number appearing in the given column?
        for i in range(0,9):
            if grid[i][column] == number:
                return False
    
        #Is the number appearing in the given square?
        x0 = (column // 3) * 3
        y0 = (row // 3) * 3
        for i in range(0,3):
            for j in range(0,3):
                if grid[y0+i][x0+j] == number:
                    return False

        return True

    def solve():
        for row in range(0,9):
            for column in range(0,9):
                if grid[row][column] == 0:
                    for number in range(1,10):
                        if possible(row, column, number):
                            grid[row][column] = number
                            solve()
                            grid[row][column] = 0

                    return
      
        print(np.matrix(grid))
        print('For More possible solutions press 1 else 2')
        ch= int(input())
        if ch==1:
            solve()
        else:
            exit()
    print("\nWant to see solution,press1\nto exit to main menu press 2")
    val = int(input())
    if val==1:
        solve()
    elif val==2:
        os.system('python choice.py')
    
#     |-----------------------------|
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     |---------+---------+---------|
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     |---------+---------+---------|
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     | 0  0  0 | 0  0  0 | 0  0  0 |
#     |-----------------------------|
    
def CheckValid(grid,row,col,num):
    #check if in row
    valid = True
    #check row and collumn
    for x in range(9):
        if (grid[x][col] == num):
            valid = False
    for y in range(9):
        if (grid[row][y] == num):
            valid = False
    rowsection = row // 3
    colsection = col // 3
    for x in range(3):
        for y in range(3):
            #check if section is valid
            if(grid[rowsection*3 + x][colsection*3 + y] == num):
                valid = False
    return valid
 

 
MakeSudoku()
    





