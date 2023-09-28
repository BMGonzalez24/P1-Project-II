def distancia(pt1, pt2):
    return ((pt2[0]-pt1[0])**2+(pt2[1]-pt1[1])**2)**(1/2)

def sugerirCentroide(centros, pt):
    indices = []
    for i in centros:
        indices.append(distancia(i,pt))
    return indices.index(min(indices))

def encontrarCentroMassa(pts):
    x = []
    y = []

    for i in pts:
        primeiro,segundo = i
        x.append(primeiro)
        y.append(segundo)
   
    mediaX = sum(x) / len(x)
    mediaY = sum(y) / len(y)

    return mediaX, mediaY

def custear(centros, pts):
    total = 0
    for p in pts:
        total += distancia(centros[sugerirCentroide(centros,p)],p)**2
    return total

def sugerirK(pts, minK=2, maxK=10):
  """
  requires: minK >= 2
  requires: minK < maxK
  """
  distancia = [k for k in range(minK,maxK)]
  centroides = [  ]
  custos = [   ]
 
  for k in distancia:
    centroides = (aglomerar(k, pts))
    custos.append(custear(centroides,pts)*k**(3/2))
    
  return distancia[custos.index(min(custos))]