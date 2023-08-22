# Make a spiral
# https://www.codewars.com/kata/534e01fbbb17187c7e0000c6/solutions




# Best practice
def spiralize(size):
    
    def on_board(x, y):
        return 0 <= x < size and 0 <= y < size
        
    def is_one(x, y):
        return on_board(x, y) and spiral[y][x] == 1
        
    def can_move():
        return on_board(x+dx, y+dy) and not (is_one(x+2*dx, y+2*dy) or is_one(x+dx-dy, y+dy+dx) or is_one(x+dx+dy, y+dy-dx))
    
    
    spiral = [[0 for x in range(size)] for y in range(size)]   
    x, y = -1, 0
    dx, dy = 1, 0
    turns = 0
    
    while (turns < 2):
        if can_move():
            x += dx
            y += dy
            spiral[y][x] = 1
            turns = 0
        else:
            dx, dy = -dy, dx
            turns += 1
    
    return spiral





# Clever

def spiralize(size):
    # Make a snake
    spiral = [[1 - min(i,j,size-max(i,j)-1)%2 for j in xrange(size)] for i in xrange(size)]
    for i in xrange(size/2-(size%4==0)):
      spiral[i+1][i] = 1 - spiral[i+1][i]
    return spiral





import numpy as np

def spiralize(size):
    if size == 0:
        return []
    if size == 1:
        return [[1]]
    if size == 2:
        return [[1,1],[0,1]]
    sp = np.zeros((size, size))
    sp[0, :] = 1
    sp[:, -1] = 1
    sp[-1, :] = 1
    sp[2:, :-2] = np.array(spiralize(size-2))[::-1,::-1]
    return sp.tolist()