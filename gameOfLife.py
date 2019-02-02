import pygame

SCREEN_HEIGHT = 630
SCREEN_WIDTH = 630

GRID_HEIGHT = 25
GRID_WIDTH = 25

MARGIN = 5
CELL_HEIGHT = 20
CELL_WIDTH = 20

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

screen = pygame.display.set_mode([SCREEN_HEIGHT, SCREEN_WIDTH])
    
# creates grid
def create_grid():
    grid = []
    for row in range(GRID_HEIGHT):
        grid.append([])
        for column in range(GRID_WIDTH):
            grid[row].append(0)
    grid[10][10] = 1
    return grid

def draw_grid(grid):
    for row in range(GRID_WIDTH):
        for column in range(GRID_HEIGHT):
            colour = BLACK
            if grid[row][column] == 1:
                colour = WHITE
            pygame.draw.rect(screen, colour, [(MARGIN + CELL_WIDTH) * column + MARGIN,
                                              (MARGIN + CELL_HEIGHT) * row + MARGIN,
                                               CELL_WIDTH,
                                               CELL_HEIGHT])
                                              
def main():
    grid = create_grid()
    screen.fill(BLACK)
    draw_grid(grid)
    pygame.display.flip()
    
if __name__ == '__main__':
    main()
