import pygame 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
W, H = 200, 200

pygame.init()
screen = pygame.Surface((W, H))

screen.fill(WHITE)

#créer une liste de 10 stim avec 5 formes & 5 miroirs. On veut 2 coudes par forme 2D, 3 coudes par forme 3D

pygame.draw.circle(screen, BLACK, (100,100), 71, 0)
pygame.draw.rect(screen, WHITE, (60, 70, 20, 20))
pygame.draw.rect(screen, WHITE, (80, 70, 20, 20))
pygame.draw.rect(screen, WHITE, (100, 70, 20, 20))
pygame.draw.rect(screen, WHITE, (100, 90, 20, 20))
pygame.draw.rect(screen, WHITE, (100, 110, 20, 20))
pygame.draw.rect(screen, WHITE, (120, 110, 20, 20))
pygame.image.save(screen, "shapeA1.png")

screen = pygame.transform.flip(screen, True, False)
pygame.image.save(screen, "shapeA2.png")

pygame.draw.circle(screen, BLACK, (100,100), 71, 0)
pygame.draw.rect(screen, WHITE, (60, 70, 20, 20))
pygame.draw.rect(screen, WHITE, (60, 90, 20, 20))
pygame.draw.rect(screen, WHITE, (60, 110, 20, 20))
pygame.draw.rect(screen, WHITE, (80, 110, 20, 20))
pygame.draw.rect(screen, WHITE, (100, 110, 20, 20))
pygame.draw.rect(screen, WHITE, (120, 110, 20, 20))
pygame.image.save(screen, "shapeB1.png")

screen = pygame.transform.flip(screen, True, False)
pygame.image.save(screen, "shapeB2.png")

pygame.draw.circle(screen, BLACK, (100,100), 71, 0)
pygame.draw.rect(screen, WHITE, (80, 50, 20, 20))
pygame.draw.rect(screen, WHITE, (80, 70, 20, 20))
pygame.draw.rect(screen, WHITE, (80, 90, 20, 20))
pygame.draw.rect(screen, WHITE, (80, 110, 20, 20))
pygame.draw.rect(screen, WHITE, (100, 110, 20, 20))
pygame.draw.rect(screen, WHITE, (100, 130, 20, 20))
pygame.image.save(screen, "shapeC1.png")

screen = pygame.transform.flip(screen, True, False)
pygame.image.save(screen, "shapeC2.png")

pygame.draw.circle(screen, BLACK, (100,100), 71, 0)
pygame.draw.rect(screen, WHITE, (70, 60, 20, 20))
pygame.draw.rect(screen, WHITE, (70, 80, 20, 20))
pygame.draw.rect(screen, WHITE, (70, 100, 20, 20))
pygame.draw.rect(screen, WHITE, (90, 100, 20, 20))
pygame.draw.rect(screen, WHITE, (90, 120, 20, 20))
pygame.draw.rect(screen, WHITE, (110, 120, 20, 20))
pygame.image.save(screen, "shapeD1.png")

screen = pygame.transform.flip(screen, True, False)
pygame.image.save(screen, "shapeD2.png")

pygame.draw.circle(screen, BLACK, (100,100), 71, 0)
pygame.draw.rect(screen, WHITE, (70, 70, 20, 20))
pygame.draw.rect(screen, WHITE, (90, 70, 20, 20))
pygame.draw.rect(screen, WHITE, (110, 70, 20, 20))
pygame.draw.rect(screen, WHITE, (110, 90, 20, 20))
pygame.draw.rect(screen, WHITE, (110, 110, 20, 20))
pygame.draw.rect(screen, WHITE, (90, 110, 20, 20))
pygame.image.save(screen, "shapeE1.png")

screen = pygame.transform.flip(screen, True, False)
pygame.image.save(screen, "shapeE2.png")



pygame.quit()
