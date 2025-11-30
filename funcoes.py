from constantes import *

#função que me da as componentes x e y da aceleração no planeta 1 causada pelo planeta 2
def força_gravitacional(planeta1, planeta2):
    x1 = planeta1.rect.center[0]
    y1 = planeta1.rect.center[1]

    x2 = planeta2.rect.center[0]
    y2 = planeta2.rect.center[1]

    distancia = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5)

    #me da a força gravitacional entre esses dois corpos
    Fg = G * (planeta1.massa * planeta2.massa) // distancia ** 2

    #me da as componentes da força gravitacional:
    Fgx = - Fg * ((x1 - x2) // distancia)
    Fgy = - Fg * ((y1 - y2) // distancia)

    #me da as componentes da aceleração
    ax = Fgx // planeta1.massa
    ay = Fgy // planeta1.massa

    return [ax, ay]

