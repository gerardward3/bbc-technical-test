from random import randint
import pygame

# global variables
SCREEN_HEIGHT = 630
SCREEN_WIDTH = 630

GRID_HEIGHT = 25
GRID_WIDTH = 25

CELL_HEIGHT = 20
CELL_WIDTH = 20
MARGIN = 5

# colour variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# setup pygame
pygame.init()
screen = pygame.display.set_mode([SCREEN_HEIGHT, SCREEN_WIDTH])
    
# creates blank grid, each cell = 0 (dead)
def create_grid():
    grid = []
    for row in range(GRID_HEIGHT):
        grid.append([])
        for column in range(GRID_WIDTH):
            grid[row].append(0)
    return grid

# draws grid on screen
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

# carries out iteration of game
def evolve(grid):
    next_grid = create_grid()
    for row in range(GRID_HEIGHT):
        for column in range(GRID_WIDTH):
            cell = grid[row][column]
            neighbours = count_neighbours(grid, row, column)
            if cell == 0:
                if neighbours == 3:
                    cell = 1
            else:
                if neighbours < 2 or neighbours > 3:
                    cell = 0
            next_grid[row][column] = cell
    return next_grid           

# counts neighbour cells of a cell    
def count_neighbours(grid, x, y):
    neighbours = [[x - 1, y - 1], [x, y - 1], [x + 1, y - 1], [x - 1, y], [x + 1, y], [x - 1, y + 1], [x, y + 1], [x + 1, y + 1]]
    neighbour_count = 0
    for n in neighbours:
        if n[0] >= 0 and n[0] < GRID_WIDTH and n[1] >= 0 and n[1] < GRID_HEIGHT:
            neighbour_count += grid[n[0]][n[1]]
    return neighbour_count
    
def main():
    done = False
    clock = pygame.time.Clock()
    grid = create_grid()
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            grid[x][y] = randint(0,1)
            
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            #elif event.type == pygame.MOUSEBUTTONDOWN:
        grid = evolve(grid)
        screen.fill(BLACK)
        draw_grid(grid)
        clock.tick(5)
        pygame.display.flip()
        
    pygame.quit()
    
if __name__ == '__main__':
    main()
