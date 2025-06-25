import pygame
from sys import exit


pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))
test_font = pygame.font.Font(None,30)

board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],

    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],

    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


class Box:
    def __init__(self,x,y,color="white",width=50):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
    def draw(self):
        self.rect =  pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.width),2)
        return self.rect
    
    def write(self,char,color="red"):

        pygame.draw.rect(screen, "black", (self.x+2, self.y+2, self.width-3, self.width-3))

        text_surf = test_font.render(char,False,color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf,text_rect)
        
grid = []

def isvalid():
    pass

for i in range(9):
    row = []
    for j in range(9):
        b = Box(100 + 50 * j, 100 + 50 * i)
        row.append(b)
    grid.append(row)

def isvalid(board, row, col, num):
    
    for j in range(9):
        if board[row][j] == num and j != col:
            return False

  
    for i in range(9):
        if board[i][col] == num and i != row:
            return False

   
    box_start_row = (row // 3) * 3
    box_start_col = (col // 3) * 3

    for i in range(box_start_row, box_start_row + 3):
        for j in range(box_start_col, box_start_col + 3):
            if board[i][j] == num and (i, j) != (row, col):
                return False

    return True

def solve(grid,board):
    for i in range(9):
        for j in range(9):
            if(board[i][j]==0):
                for k in range(1,10):
                    if(isvalid(board,i,j,k)):
                        board[i][j] = k
                        grid[i][j].write(str(k),color="green")
                        pygame.display.update()
                        # pygame.time.delay(50)

                        if(solve(grid,board)):
                            return True
                        

                        board[i][j] = 0
                        grid[i][j].write("")
                        pygame.display.update()
                        # pygame.time.delay(50)

                return False
    return True

solved = False

for i in range(9):
    for j in range(9):
        grid[i][j].draw()
        if board[i][j] != 0:
            grid[i][j].write(str(board[i][j]))
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    
                
    if not solved:
        
        solve(grid,board)
        solved = True

    pygame.display.update()
    clock.tick(60)