import pygame

def is_free_position(grid,column_index,row_index):
    return grid[row_index][column_index] == ' '

def is_winner(grid, mark):
    if (grid[0][0] == mark and grid[0][1] == mark and grid[0][2] == mark) or\
    (grid[1][0] == mark and grid[1][1] == mark and grid[1][2] == mark) or\
    (grid[2][0] == mark and grid[2][1] == mark and grid[2][2] == mark) or\
    (grid[0][0] == mark and grid[1][0] == mark and grid[2][0] == mark) or\
    (grid[0][1] == mark and grid[1][1] == mark and grid[2][1] == mark) or\
    (grid[0][2] == mark and grid[1][2] == mark and grid[2][2] == mark) or\
    (grid[0][0] == mark and grid[1][1] == mark and grid[2][2] == mark) or\
    (grid[2][0] == mark and grid[1][1] == mark and grid[0][2] == mark):
        return True
    else:
        return False

def is_grid_full(grid):
    full = True
    for row in grid:
        for mark in row:
            if mark == ' ':
                full = False

    return full


pygame.init() #모듈 init
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) #화면크기 설정
clock = pygame.time.Clock()

BLACK = (0,0,0)
RED = (255,0,0)
WHITE = (255,255,255)
YELLOW = (255,255,0)
large_font = pygame.font.SysFont('malgungothic',72)
CELL_SIZE = 200
COLUMN_COUNT = 3
ROW_COUNT = 3
X_WIN = 1
O_WIN = 2
DRAW = 3
game_over = 0

grid = [[' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']]

turn = 0

while True:
    screen.fill(BLACK)

    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        break
    elif event.type == pygame.MOUSEBUTTONDOWN and game_over == 0:
        column_index = event.pos[0] // CELL_SIZE
        row_index = event.pos[1] // CELL_SIZE
        print(column_index, row_index)

        if turn == 0:
            if is_free_position(grid, column_index, row_index):
                grid[row_index][column_index] = 'X'
                
                if is_winner(grid, 'X'):
                    game_over = X_WIN
                elif is_grid_full(grid):
                    game_over = DRAW

                turn += 1
                turn %= 2
        elif turn == 1:
            if is_free_position(grid, column_index, row_index):
                grid[row_index][column_index] = 'O'
                
                if is_winner(grid, 'O'):
                    game_over = O_WIN
                elif is_grid_full(grid):
                    game_over = DRAW
                
                turn += 1
                turn %= 2


    for column_index in range(COLUMN_COUNT):
        for row_index in range(ROW_COUNT):
            pygame.draw.rect(screen, WHITE, pygame.Rect(column_index * CELL_SIZE, row_index * CELL_SIZE, CELL_SIZE, CELL_SIZE),1)

    """
    pygame.draw.rect(screen, WHITE, pygame.Rect(0,0,200,200),1)
    pygame.draw.rect(screen, WHITE, pygame.Rect(200, 0, 200, 200), 1)
    pygame.draw.rect(screen, WHITE, pygame.Rect(400, 0, 200, 200), 1)

    pygame.draw.rect(screen, WHITE, pygame.Rect(0, 200, 200, 200), 1)
    pygame.draw.rect(screen, WHITE, pygame.Rect(200, 200, 200, 200), 1)
    pygame.draw.rect(screen, WHITE, pygame.Rect(400, 200, 200, 200), 1)

    pygame.draw.rect(screen, WHITE, pygame.Rect(0, 400, 200, 200), 1)
    pygame.draw.rect(screen, WHITE, pygame.Rect(200, 400, 200, 200), 1)
    pygame.draw.rect(screen, WHITE, pygame.Rect(400, 400, 200, 200), 1)
    """

    for column_index in range(COLUMN_COUNT):
        for row_index in range(ROW_COUNT):
            mark = grid[row_index][column_index]
            if mark == 'X':
                X_image = large_font.render('X', True, YELLOW)
                screen.blit(X_image, X_image.get_rect(centerx = column_index * CELL_SIZE + CELL_SIZE //2 ,
                                                      centery = row_index * CELL_SIZE + CELL_SIZE // 2))
            elif mark == 'O':
                O_image = large_font.render('O', True,WHITE)
                screen.blit(O_image, O_image.get_rect(centerx=column_index * CELL_SIZE + CELL_SIZE // 2,
                                                      centery=row_index * CELL_SIZE + CELL_SIZE // 2))
    if game_over > 0:
        if game_over == X_WIN:
            x_win_image = large_font.render('X 승리', True, RED)
            screen.blit(x_win_image, x_win_image.get_rect(centerx = SCREEN_WIDTH//2, centery = SCREEN_HEIGHT//2))
        elif game_over == O_WIN:
            o_win_image = large_font.render('O 승리', True, RED)
            screen.blit(o_win_image, o_win_image.get_rect(centerx=SCREEN_WIDTH // 2, centery=SCREEN_HEIGHT // 2))
        else:
            draw_image = large_font.render('무승부', True, RED)
            screen.blit(draw_image, draw_image.get_rect(centerx=SCREEN_WIDTH // 2, centery=SCREEN_HEIGHT // 2))

    pygame.display.update()
    clock.tick(30)

pygame.quit()