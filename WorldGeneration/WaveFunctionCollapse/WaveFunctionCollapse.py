import pygame
from ClassWorld import World
from ClassDrawWorld import DrawWorld
from Config import *



INTERACTIVE = True
INTERACTIVE_KEYPRESS = False


pygame.init()
clock = pygame.time.Clock()

displaySurface = pygame.display.set_mode((WORLD_X * TILESIZE * SCALETILE, WORLD_Y * TILESIZE * SCALETILE))
pygame.display.set_caption("Wave Function Collapse")


world = World(WORLD_X, WORLD_Y)
drawWorld = DrawWorld(world)

done = False

if INTERACTIVE == False:
    while done == False:
        result = world.waveFunctionCollapse()
        if result == 0:
            done = True


drawWorld.update()
isRunning = True


while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False
            if event.key == pygame.K_SPACE:
                if INTERACTIVE == True and INTERACTIVE_KEYPRESS == True:
                    world.waveFunctionCollapse()
                    drawWorld.update()

    if INTERACTIVE == True and INTERACTIVE_KEYPRESS == False:
        if not done:
            result = world.waveFunctionCollapse()
            if result == 0:
                done = True
        drawWorld.update()


    drawWorld.draw(displaySurface)

    pygame.display.flip()
    clock.tick(60)


pygame.quit()
