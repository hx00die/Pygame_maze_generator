import pygame, sys, random, time
from pygame.math import Vector2

def remove_left(cur):
    pygame.draw.rect(screen,(150,0,150),(cur[0]*w-w +1, cur[1]*w+1, w*2-1, w-1))
    pygame.display.update()
def remove_right(cur):
    pygame.draw.rect(screen,(150,0,150),(cur[0]*w+1, cur[1]*w+1, w*2-1, w-1))
    pygame.display.update()
def remove_down(cur):
    pygame.draw.rect(screen,(150,0,150),(cur[0]*w+1, cur[1]*w+1, w-1, w*2-1))
    pygame.display.update()
def remove_up(cur):
    pygame.draw.rect(screen,(150,0,150),(cur[0]*w+1, cur[1]*w-w+1, w-1, w*2-1))
    pygame.display.update()
def current(cur):
    pygame.draw.rect(screen,(0,255,0),(cur[0]*w+1, cur[1]*w+1, w-1, w-1))
    pygame.display.update()
def backtracking_cell(cur):
    pygame.draw.rect(screen, (150,0,150), (cur[0]*w+1, cur[1]*w+1, w-1, w-1))
    pygame.display.update()

def play():
    pos = pygame.mouse.get_pos()
    win(pos)
    x,y = pos
    xpos, ypos = x // w,y // w
    possitions.append(Vector2(xpos,ypos))
    if draw_spots():
        spots = pygame.Rect(xpos*w + w//4, ypos*w + w//4, w//2, w//2)
        drawn.append(spots)
        pygame.draw.rect(screen,(135,206,250),spots)

def draw_spots():
    valid = [0, -1, 1]
    if len(possitions) > 1:
        if int(possitions[-1].x - possitions[-2].x) in valid:
            return True
        if int(possitions[-1].y - possitions[-2].y) in valid:
            return True 
        else:
            return False
    else:
        return True

def finish():
    global e
    start = 0
    end = (rows-1)*w
    pygame.draw.rect(screen, (50,150,70), (start + w // 4,start + w //4, w//2,w//2))
    e = pygame.draw.rect(screen, (255,215,0), (end + w // 4,end + w //4, w//2,w//2))

def win(pos):
    global message
    if e.collidepoint(pos):
        message = "Solved!!"
        path()
        

def path():
    for i in range(len(drawn)-1):
        pygame.draw.line(screen, (135,206,250), (drawn[i].centerx-1,drawn[i].centery-1), (drawn[i+1].centerx-1,drawn[i+1].centery-1), w //2)
 
def cell(x,y):
    x,y = x,y
    pos = (x,y)
    return pos

def make_grid():
    for x in range(rows):
        for y in range(cols):
            grid.append(cell(x,y))

def show():
    for c in grid:
        a,b = c
        x = a*w
        y = b*w
        pygame.draw.line(screen, (200,200,200), (x,y), (x+w,y))
        pygame.draw.line(screen, (200,200,200), (x+w,y), (x+w,y+w))
        pygame.draw.line(screen, (200,200,200), (x+w,y+w), (x,y+w))
        pygame.draw.line(screen, (200,200,200), (x,y+w), (x,y))

def get_neighburs():
    cur = grid[0]
    current(cur)
    visited.append(cur)
    stack.append(cur)
    while len(stack) > 0:
        time.sleep(0.01) 
        n = []
        cur = stack[-1]
        x,y = cur
        left = (x - 1,y)
        right = (x + 1,y)
        up = (x,y - 1)
        down = (x,y + 1)
        if left not in visited and left[0] != -1:
            n.append(left)
        if right not in visited and right[0] != rows:
            n.append(right)
        if up not in visited and up[1] != -1:
            n.append(up)
        if down not in visited and down[1] != cols:
            n.append(down)
        if len(n) > 0:
            r = random.choice(n)
              
            if r == left:
                remove_left(cur)  
                stack.append(r)
                visited.append(r)
            if r == right:
               remove_right(cur)  
               stack.append(r)
               visited.append(r)
            if r == up:
                remove_up(cur)  
                stack.append(r)
                visited.append(r)
            if r == down:
                remove_down(cur)  
                stack.append(r)
                visited.append(r)
        else:
            stack.pop()
            current(cur)
            time.sleep(0.01)
            backtracking_cell(cur)

pygame.init()
clock = pygame.time.Clock()

screen_width = 403
screen_height = 403
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption(('Maze generator'))

grid = []
drawn = []
stack = []
possitions = []
visited = []

w = 40
rows = 10
cols = 10

myfont = pygame.font.SysFont("monospace",40)
message = ''

make_grid()
show()
get_neighburs()
pygame.display.set_caption(('generated!'))

while True:
    finish()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            play()
    
    text1 = myfont.render("{0}".format(message), True, (0,0,0))
    screen.blit(text1, (120,100))
    pygame.display.flip()
    clock.tick(30)
    
