import pygame as pg
import time

maze1 = [
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

maze2 = [
    [1,0,1,1],
    [1,0,1,1],
    [1,0,0,0],
    [1,1,1,1]]

start = 0,1
end = 0,3

m = []
for i in range(len(maze1)):
    m.append([])
    for j in range(len(maze1[i])):
        m[-1].append(0)
i,j = start
m[i][j] = 1

n = 0
while m[end[0]][end[1]] == 0:
    n += 1
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == n:
                if i>0 and m[i-1][j] == 0 and maze1[i-1][j] == 0:
                    m[i-1][j] = n + 1
                if j>0 and m[i][j-1] == 0 and maze1[i][j-1] == 0:
                    m[i][j-1] = n + 1
                if i<len(m)-1 and m[i+1][j] == 0 and maze1[i+1][j] == 0:
                    m[i+1][j] = n + 1
                if j<len(m[i])-1 and m[i][j+1] == 0 and maze1[i][j+1] == 0:
                    m[i][j+1] = n + 1

i, j = end
n = m[i][j]
P = [(i,j)]
while n > 1:
    if i > 0 and m[i - 1][j] == n-1:
        i, j = i-1, j
        P.append((i, j))
        n-=1
    elif j > 0 and m[i][j - 1] == n-1:
        i, j = i, j-1
        P.append((i, j))
        n-=1
    elif i < len(m) - 1 and m[i + 1][j] == n-1:
        i, j = i+1, j
        P.append((i, j))
        n-=1
    elif j < len(m[i]) - 1 and m[i][j + 1] == n-1:
        i, j = i, j+1
        P.append((i, j))
        n -= 1

min_moves = []
for i in range (len(m)):
    for j in range (len(m[i])):
        min_moves.append(m[i][j])

#print(m)
#print(P)
print(max(min_moves)-1)

pg.init()
L = 50 # Pixel height and width of tiles

screen = pg.display.set_mode((len(maze1)*L,len(maze1)*L)) # Window size

moves = []

player = []

player.append((start))

running = True
while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            # Close window
            running = False
        elif event.type == pg.KEYDOWN:
            #if event.key == pg.K_ESCAPE:
                #state = "PAUSE"
            if event.key == pg.K_w:
                head_r,head_c = player[0]
                new_head = (head_r-1,head_c)
                player.insert(0,new_head)
                player.pop()
                moves.append(1)
                print(len(moves))
            elif event.key == pg.K_s:
                head_r,head_c = player[0]
                new_head = (head_r+1,head_c)
                player.insert(0,new_head)
                player.pop()
                moves.append(1)
                print(len(moves))
            elif event.key == pg.K_d:
                head_r,head_c = player[0]
                new_head = (head_r,head_c+1)
                player.insert(0,new_head)
                player.pop()
                moves.append(1)
                print(len(moves))
            elif event.key == pg.K_a:
                head_r,head_c = player[0]
                new_head = (head_r,head_c-1)
                player.insert(0,new_head)
                player.pop()
                moves.append(1)
                print(len(moves))

    # Draw game board
    for c in range(len(maze1)):      # Create variables c and r for width and height
        for r in range(len(maze1)):
            pg.draw.rect(screen,(50,50,50), pg.Rect(c*L+5,r*L+5,L-5,L-5))

    # Draw walls
    for c in range(len(maze1)):
        for r in range(len(maze1[c])):
            if maze1[r][c] == 1:
                pg.draw.rect(screen,(50,200,50), pg.Rect(c*L+5,r*L+5,L-5,L-5))

    for p in player:
        r,c = p
        pg.draw.rect(screen,(200,50,50), pg.Rect(c*L+5,r*L+5,L-5,L-5))
            
    # update the screen window
    pg.display.flip()

