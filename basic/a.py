from random import shuffle
from itertools import cycle

def showDispay(target):
    colCodi = cycle('1234567890')
    rowCodi = cycle('1234567890')
    
    print('  ', end = '')
    for _ in range(cols):
        print(next(colCodi), end = '   ')    
    print()

    
    for x in target:
        print(next(rowCodi), ' | '.join(x))

def countMines(row, col):
    rect = ((-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)
           )
    count = 0
    
    for x, y in rect:
        x += row 
        y += col
        
        if 0 <= x < rows and 0 <= y < cols:
            if minePlate[x][y] == '*':
                count += 1
    
    return count

def commandClick(x, y):
    x -= 1
    y -= 1
    status = minePlate[x][y]
    
    if status == '*':
        display[x][y] = 'X'
        return 'fail'
    elif '0' <= status <= '8':
        display[x][y] = status
    else:
        openSpace(status, spacePlate[status])

def openSpace(mark, area):
    for x, y in area:
        temp = minePlate[x][y]
        
        display[x][y] = ' ' if temp == mark else temp

rows       = 16 
cols       = 30
mines      = 99
minePlate  = []
spacePlate = {}
display    = []

# 지뢰 초기화 하기
temp = ['#'] * (rows * cols)

for x in range(mines):
    temp[x] = '*'
    
shuffle(temp)

for x in range(rows):
    minePlate.append(temp[x * cols:(x + 1) * cols])
    display.append(['O'] * cols)
    
# 주위에 지뢰 개수 구하기
for row in range(rows):
    for col in range(cols):
        if minePlate[row][col] == '#':
            count = countMines(row, col)
            minePlate[row][col] = str(count) if count != 0 else '#'
            
# 지뢰가 없는 영역 찾기
def dfs(row, col):
    rect = ((-1, 0), (0, -1), (0, 1), (1, 0))
    
    if minePlate[row][col] == '#':
        minePlate[row][col] = chr(mark)
        tempSpace.append((row, col))
        
        for x, y in rect:
            x += row 
            y += col

            if 0 <= x < rows and 0 <= y < cols:
                dfs(x, y)
        
    elif '1' <= minePlate[row][col] <= '8':
        tempSpace.append((row, col))    
    
    
mark = ord('A')
for row in range(rows):
    for col in range(cols):
        if minePlate[row][col] == '#':
            tempSpace = []
            dfs(row, col)
            spacePlate[chr(mark)] = tempSpace
            mark += 1
            
while True:
    command = list(input('C x y | M x y | U x y | V | Q ? ').split())
    
    if len(command) == 1:
        if command[0].lower() == 'v':
                showDispay(display)
        elif command[0].lower() == 'q':
                break
        elif command[0].lower() == 's':
                showDispay(minePlate)
                
    elif len(command) == 3:
        if command[0].lower() == 'c':
            commandClick(int(command[1]), int(command[2]))
        elif command[0].lower() == 'm':
            pass
        elif command[0].lower() == 'u':
            pass        
