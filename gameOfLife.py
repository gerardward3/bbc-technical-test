# BBC Technical Test - Software Engineering Graduate Trainee Scheme
# Author - Gerard Ward
# Date - 03/02/2019
# Game of Life
#
# - Requires Python 3 and Pygame
# - Game is played on 25 x 25 grid, can be changed by editing GRID_HEIGHT and GRID_WIDTH variables
# - Live cells are white, dead cells are black
# - Seeded grid randomly generated at beginning of game

from random import randint
import pygame

# global variables
GRID_HEIGHT = 25        # Change for
GRID_WIDTH = 25         # different sized grid

CELL_HEIGHT = 20
CELL_WIDTH = 20
MARGIN = 5

SCREEN_HEIGHT = ((CELL_HEIGHT + MARGIN) * GRID_HEIGHT) + MARGIN
SCREEN_WIDTH = ((CELL_WIDTH + MARGIN) * GRID_WIDTH) + MARGIN

# colour variables
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# setup pygame
pygame.init()
screen = pygame.display.set_mode([SCREEN_HEIGHT, SCREEN_WIDTH])
    
# creates blank grid as 2D array, each cell = 0 (dead)
def create_grid():
    grid = []
    for row in range(GRID_HEIGHT):
        grid.append([])
        for column in range(GRID_WIDTH):
            grid[row].append(0)
    return grid

# draws grid on screen - dead cell = 0 = black, live cell = 1 = white
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

# counts neighbour cells of a cell    
def count_neighbours(grid, x, y):
    
    # gets all neighbours horizontally, vertically and diagonally
    neighbours = [[x - 1, y - 1], [x, y - 1], [x + 1, y - 1],
                  [x - 1, y], [x + 1, y],
                  [x - 1, y + 1], [x, y + 1], [x + 1, y + 1]]  
    neighbour_count = 0

    # checks neighbours have valid coordinates then adds value of cell to neighbour total
    for n in neighbours:
        if n[0] >= 0 and n[0] < GRID_WIDTH and n[1] >= 0 and n[1] < GRID_HEIGHT:
            neighbour_count += grid[n[0]][n[1]]
    return neighbour_count

# carries out iteration of game
def evolve(grid):

    # creates new grid for next iteration of game
    next_grid = create_grid()
    for row in range(GRID_HEIGHT):
        for column in range(GRID_WIDTH):
            cell = grid[row][column]
            neighbours = count_neighbours(grid, row, column)
            if cell == 0:
                if neighbours == 3:     # Checks for Scenario 4 (Creation of Life)
                    cell = 1
            else:
                if neighbours < 2 or neighbours > 3:    # Checks for Scenario 1 (Underpopulation), Scenario 2 (Overcrowding) and Scenario 3 (Survival)
                    cell = 0
            next_grid[row][column] = cell
    return next_grid           
    
def main():
    done = False
    clock = pygame.time.Clock()
    grid = create_grid()

    # Populates initial grid with random live cells
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            grid[x][y] = randint(0,1)

    # Starts game loop        
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:       # Game quits upon close button being pressed
                done = True
                
        grid = evolve(grid)
        screen.fill(BLACK)
        draw_grid(grid)
        clock.tick(2)                           # Game runs at 2 frames per second
        pygame.display.flip()
        
    pygame.quit()
    
if __name__ == '__main__':
    main()
