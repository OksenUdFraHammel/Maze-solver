import pygame as pg
import time

maze1 = [
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1 ,0 ,1 ,0 ,0 ,0 ,0 ,0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 1 ,0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

maze2 = [
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
#print(max(min_moves)-1)

pg.init()

def print_moves():
    moves.append(1)
    pg.draw.rect(screen,(50,50,50), pg.Rect(805,5,190,145))
    text = font1.render("Min. {}".format((max(min_moves)-1)), True,(255,255,255))
    text_rect = text.get_rect()
    text_rect.center = (900,45)
    screen.blit(text,text_rect)
    text = font1.render("Cur. {}".format(len(moves)), True, (255,255,255))
    text_rect.center = (900,95)
    screen.blit(text,text_rect)
    

L = 50 # Pixel height and width of tiles

#screen = pg.display.set_mode(((len(maze1)+int(len(maze1)))*L+5,len(maze1)*L+5)) # Window size
screen = pg.display.set_mode((1000,805))
font1 = pg.font.Font("Inconsolata-Bold.ttf", 35)
font2 = pg.font.Font("Inconsolata-Bold.ttf", 28)
font3 = pg.font.Font("Inconsolata-Bold.ttf", 20)

state = "PLAY"

moves = []

player = [start]

pg.draw.rect(screen,(50,50,50), pg.Rect(805,5,190,145))
text = font1.render("Min. {}".format((max(min_moves)-1)), True,(255,255,255))
text_rect = text.get_rect()
text_rect.center = (900,45)
screen.blit(text,text_rect)
text = font1.render("Cur. {}".format(len(moves)), True, (255,255,255))
text_rect.center = (900,95)
screen.blit(text,text_rect)

running = True
while running:
    if state == "PLAY":
        for event in pg.event.get():
            if event.type == pg.QUIT:
                # Close window
                running = False
            elif event.type == pg.KEYDOWN:
                #if event.key == pg.K_ESCAPE:
                    #state = "PAUSE"
                if event.key == pg.K_w:
                    if not maze1[r-1][c] == 1:
                        head_r,head_c = player[0]
                        new_head = (head_r-1,head_c)
                        player.insert(0,new_head)
                        player.pop()
                        print_moves()
                    else:
                        pass
                elif event.key == pg.K_s:
                    if not maze1[r+1][c] == 1:
                        head_r,head_c = player[0]
                        new_head = (head_r+1,head_c)
                        player.insert(0,new_head)
                        player.pop()
                        print_moves()
                    else:
                        pass
                elif event.key == pg.K_d:
                    if not maze1[r][c+1] == 1:
                        head_r,head_c = player[0]
                        new_head = (head_r,head_c+1)
                        player.insert(0,new_head)
                        player.pop()
                        print_moves()
                    else:
                        pass
                elif event.key == pg.K_a:
                    if not maze1[r][c-1] == 1:
                        head_r,head_c = player[0]
                        new_head = (head_r,head_c-1)
                        player.insert(0,new_head)
                        player.pop()
                        print_moves()
                    else:
                        pass
                     
        # Draw game board
        for c in range(len(maze1)):      # Create variables c and r for width and height
            for r in range(len(maze1)):
                pg.draw.rect(screen,(50,50,50), pg.Rect(c*L+5,r*L+5,L-5,L-5))

            # Draw walls
        for c in range(len(maze1)):
            for r in range(len(maze1[c])):
                if maze1[r][c] == 1:
                    pg.draw.rect(screen,(50,200,50), pg.Rect(c*L+5,r*L+5,L-5,L-5))

        # Draw player
        for p in player:
            r,c = p
            pg.draw.rect(screen,(200,50,50), pg.Rect(c*L+5,r*L+5,L-5,L-5))

        if player == [end]:
            state = "END"
           
        # update the screen window
        pg.display.flip()

    elif state == "END":
        pg.draw.rect(screen,(200,200,200), pg.Rect(205,205,395,395))
        text = font2.render("Congratulations!", True,(0,0,0))
        text_rect = text.get_rect()
        text_rect.center = (402,280)
        screen.blit(text,text_rect)
        text = font3.render("You completed the maze in {} moves".format(len(moves)), True,(0,0,0))
        text_rect.center = (342,350)
        screen.blit(text,text_rect)
        text = font2.render("Press [SPACE] to try again", True,(0,0,0))
        text_rect.center = (333,500)
        screen.blit(text,text_rect)
        if int(len(moves)) - int(max(min_moves)-1) == 0:
            text = font3.render("Perfect run!", True,(0,0,0))
            text_rect.center = (452,400)
            screen.blit(text,text_rect)   
        else:
            text = font3.render("Try to complete it in {} less moves".format(int(len(moves)-int(max(min_moves)-1))), True,(0,0,0))
            text_rect.center = (340,400)
            screen.blit(text,text_rect)
        

        for event in pg.event.get():
            if event.type == pg.QUIT:
                # Close window
                running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    state = "RESET"

        pg.display.flip()

    elif state == "RESET":
        moves = []
        player = [start]
        screen.fill((0,0,0))
        pg.draw.rect(screen,(50,50,50), pg.Rect(805,5,190,145))
        text = font1.render("Min. {}".format((max(min_moves)-1)), True,(255,255,255))
        text_rect = text.get_rect()
        text_rect.center = (900,45)
        screen.blit(text,text_rect)
        text = font1.render("Cur. {}".format(len(moves)), True, (255,255,255))
        text_rect.center = (900,95)
        screen.blit(text,text_rect)

        state = "PLAY"
