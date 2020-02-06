import pygame
import math
import numpy as np
from numpy.linalg import solve
from classes.MassvelClass import massobj

pygame.init()

win = pygame.display.set_mode((1500, 800))

pygame.display.set_caption("First Game")

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)

width = 40
heigth = 30

# Object 1 statistics
x1_init = 50
y1_init = 700
velm1 = 5
m1 = 10
m1obj = massobj(m1, velm1)

# Object 2 statistics
x2_init = 150
y2_init = 700
velm2 = 10
m2 = 20
m2obj = massobj(m2, velm2)

KEm1 = m1 * math.pow(velm1, 2) / 2
mvm1 = m1 * velm1

KEm2 = m2 * math.pow(velm2, 2) / 2
mvm2 = m2 * velm2

myfont = pygame.font.SysFont('Times New Roman', 15)

###Calculate v1_final
###x is v1_final and y is v2_final
##v1fin, v2fin = symbols('v1fin v2fin')
##eq1 = Eq(velm2 - velm1 + v2fin - velm1)
##eq2 = Eq(mvm1 + mvm2 - m1*velm1 - m2*velm2)
##sol=solve((eq1, eq2),(v1fin, v2fin))
##newv1=sol[v1fin]

# Solve equations using matrice linalg
# v1 = v2 --> v1 - v2 = 0
# m1*u1 + m2*u2 = m1*v1 + m2*v2
# where u1 and u2 is initial velocity, solve for v1 and v2
# A*[x1 x2] = b
#
A = np.array([[1, -1], [m1, m2]])
b = np.array([0, mvm1 + mvm2])
x = solve(A, b)

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    x1_init += velm1
    x2_init += velm2

    # Text for m1
    m1_mass_text = myfont.render("M1 mass: " + str(m1), True, black)
    m1_initvel_text = myfont.render("M1 initial velocity: " + str(velm1), True, black)
    m1_vel_text = myfont.render("M1 velocity: " + str(x[0]), True, black)

    # Text for m2
    m2_mass_text = myfont.render("M2 mass: " + str(m2), True, black)
    m2_init_text = myfont.render("M2 initial velocity: " + str(velm2), True, black)
    m2_vel_text = myfont.render("M2 velocity: " + str(x[1]), True, black)


    win.fill(white)
    win.blit(m1_mass_text, (0, 0))
    win.blit(m1_initvel_text, (0, 15))
    win.blit(m1_vel_text, (0, 30))
    win.blit(m2_mass_text, (0, 45))
    win.blit(m2_init_text, (0, 60))
    win.blit(m2_vel_text, (0, 75))

    pygame.draw.rect(win, (255, 0, 0), (x1_init, y1_init, width, heigth))
    pygame.draw.rect(win, (255, 0, 0), (x2_init, y2_init, width, heigth))

    pygame.display.update()

    print("gittest")

pygame.quit()