import os

print("Welcome to Sudokumania\nTo generate sudoku press 1\nTo scan a sudoku press2\n\nChoice:: ")
value = int(input())
if value == 1 :
    os.system('python generator.py')
  
elif value== 2:
    os.system('python sudukoMain.py')
