def algoritmo_basico_de_lineas(xini,yini,xfin,yfin):
    m = round((yfin-yini)/(xfin-xini))
    auxy = yini
    auxx = xini
    while auxy <= yfin:
        print("basico","x:",auxx,"y:",auxy)
        auxx += 1
        auxy += m

algoritmo_basico_de_lineas(10,3,15,8)

def algoritmo_dda(xini,yini,xfin,yfin):
    dx = abs(xfin - xini)
    dy = abs(yfin - yini)
    if dx > dy:
        steps = dx
    else:
        steps = dy
    xinc = dx/steps
    yinc = dy/steps

    x = xini
    y = yini
    k = 1
    while k<=steps:
        print("dda","x:",round(x),"y:",round(y))
        x += xinc
        y += yinc
        k += 1
algoritmo_dda(20,10,30,18)