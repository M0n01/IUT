import math
import numpy as np
import sys
import time
import pygame

# Paramètres généraux
windowWidth = 800
windowHeight = 800
robotInitPos = np.array([400.0, 400.0]).T
robotInitOrient = 0.0 # radian

# Initialisation de pygame. Il s'agit de l'initialisation de la fenêtre
# graphique et de tous les éléments de pygame.
pygame.init()
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Robot')
myfont = pygame.font.SysFont("monospace", 15)
robot = pygame.image.load('robot.png')

# Affichage de texte dans la fenêtre (pour le debug) Cette partie est
# technique, vous n'avez pas besoin de vous y plonger en
# détail. Cependant, vous pourrez utiliser la fonction displayText
# pour afficher du texte pour débugger votre programme.
textLineNb = 0
def displayTextReset():
    global textLineNb
    textLineNb = 0
def displayText(msg=''):
    global textLineNb
    label = myfont.render(msg, 1, (0, 0, 0))
    window.blit(label, (5, 5 + textLineNb*15))
    textLineNb += 1

# Etat courant du robot
robotPos = robotInitPos  # Position courante du robot
robotOrient = robotInitOrient# Orientation courante du robot (rad)
# Ces variables stockent la position du robot, elles varient au cours
# du temps au gré de ses déplacements

# changement de repères

#solution + simple:
#def graph2world(xw,yw):
#    xg = (xw-400)/50
#    yg = (yw-400)/50
#    return xg, yg
#print(graph2world(500, 400))

def graph2world(CG):
    CW = [((CG-400)/50), ((CG-400)/50)]
    return CW

#def world2graph(CG):
#    CW = [(400+CG*50), (400+CG*50)]
#    return CW

def world2graph(xw,yw):
    xg = 400+xw*50
    yg = 400+yw*50
    return xg, yg

print(graph2world(robotPos)) #position du robot (robotPos) dans le monde
print(world2graph(1, 0))

obstacles = [] #list pour stock les coordonnées des obstacles

# Autres Variables Globales
mousePos = None  # Position de la souris
t0 = time.time()
last_t = 0
# Boucle principale:
# ------------------
# Le corps de la boucle est exécuté pour chaque mise à jour de la
# fenêtre d'affichage. Il s'occupe de récupérer les événements lié au
# clavier, à la souris ou encore la fenêtre elle-même (lorsqu'on la
# ferme typiquement). Ensuite, il crée les différents éléments
# constituant l'image de la fenêtre (par exemple le sprite du robot).
while 1:
    t = time.time() - t0
    T = time.time() - last_t
    last_t = time.time()
    fps = 1/T
    mousePos = np.array(pygame.mouse.get_pos())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('bye bye...')
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print('souris bouton gauche, TODO: ajouter un obstacle')
            obstacles.append(mousePos)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('Barre d\'espace')
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        robotOrient -= np.deg2rad(1)
    if keys[pygame.K_LEFT]:
        robotOrient += np.deg2rad(1)
    if keys[pygame.K_UP]:
        robotPos[1] -= np.cos(robotOrient)
        robotPos[0] -= np.sin(robotOrient)
    if keys[pygame.K_DOWN]:
        robotPos[1] += np.cos(robotOrient)
        robotPos[0] += np.sin(robotOrient)

    # Couleur du fond de la fenêtre
    window.fill((200, 200, 200))

    # Texte
    displayTextReset()
    displayText('Time: %0.3f sec' % (t))
    displayText('FPS: %0.3f fps' % (fps))
    displayText('Position Robot: X=%0.2f, Y=%0.2f' % tuple(robotPos))
    displayText('Orientation Robot: %0.2f deg' % (np.degrees(robotOrient)))
    displayText('Position Souris: X=%0.2f, Y=%0.2f' % tuple(mousePos))

    # Sprite du robot
    drawImage = pygame.transform.rotozoom(robot, np.degrees(robotOrient), 1.0)
    robotRect = drawImage.get_rect()
    robotRect.left = robotPos[0] - robotRect.width/2
    robotRect.top = robotPos[1] - robotRect.height/2
    window.blit(drawImage, robotRect)

    # Exemple de création d'un segment de couleur RGB (255,0,255)
    # d'épaisseur 4 entre les points (300,700) et (600,700).
    pygame.draw.line(window, (255,0,255), (300,700), (600,750), 4)

    # Exemple de création d'un cercle centrée en (500,600), de rayon
    # 30, d'épaisseur 3 (0 veut dire rempli) et de couleur RGB
    # (0,100,100)
    pygame.draw.circle(window, (0,100,100), (500,600), 20)

    for x,y in obstacles:
        print(mousePos)
        pygame.draw.circle(window, (0,100,100), (x,y), 20)

    pygame.display.flip()
    time.sleep(0.01)

