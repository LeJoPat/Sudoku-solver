sous_carres=[[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)],\
             [(0,3),(0,4),(0,5),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5)],\
             [(0,6),(0,7),(0,8),(1,6),(1,7),(1,8),(2,6),(2,7),(2,8)],\
             [(3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(5,0),(5,1),(5,2)],\
             [(3,3),(3,4),(3,5),(4,3),(4,4),(4,5),(5,3),(5,4),(5,5)],\
             [(3,6),(3,7),(3,8),(4,6),(4,7),(4,8),(5,6),(5,7),(5,8)],\
             [(6,0),(6,1),(6,2),(7,0),(7,1),(7,2),(8,0),(8,1),(8,2)],\
             [(6,3),(6,4),(6,5),(7,3),(7,4),(7,5),(8,3),(8,4),(8,5)],\
             [(6,6),(6,7),(6,8),(7,6),(7,7),(7,8),(8,6),(8,7),(8,8)]]

def quel_sous_carre(i,j):
    T=[[0,1,2],\
       [3,4,5],\
       [6,7,8]]
    return(T[i//3][j//3])
    
def voisins(i,j):
    x=(i,j)
    Vois=[]             # Liste contenant les voisins
    
    for l in range (9):     # voisins de la ligne
        if l!=j:
            Vois.append((i,l))
            
    for c in range (9):       # voisins de la colonne
        if c!=i:
            Vois.append((c,j))
            
    k=quel_sous_carre(i,j)
    L=sous_carres[k]       # voisins du sous carré
    
    for l in L:             # on ôte les voisins déja existant
        x,y=l
        if x!=i and y!=j:
            Vois.append(l)
    return Vois
    
def voisinage():
    l=[0]*9
    for k in range (9):
        l[k]=[0]*9
    for i in range (9):
        for j in range (9):
            l[i][j]=voisins(i,j)
    return l

Voisin=voisinage()   # variable globale


def valeurs(grille,i,j):
    if grille[i][j]!=0:
        return []
    else :
        Lv=Voisin[i][j]         # Liste des coordonnées voisines
        Vp=[]                   # Liste des valeurs possibles
        for vp in range (1,10):
            n=0
            for lv in Lv:
                x,y=lv
                if grille[x][y]==vp:
                    n+=1
            if n==0:
                Vp.append(vp)
    return (Vp)
    
    
def premier_non_rempli(grille):
    for k in range (9):
        for i in range (9):
            if grille [k][i]==0:
                return ((k,i))
    return ((-1,-1))
    
    
def resolution(grille):
    i,j=premier_non_rempli(grille)
    if i==-1 and j==-1:
        print(grille)
        return True
    else:
        val=valeurs(grille,i,j)
        for v in val:                    # on parcourt la liste des valeurs
            grille[i][j]=v
            if resolution(grille)==True:      #appel récursif
                return True
            else:
                grille[i][j]=0
    grille[i][j]=0
    return False

#exemple
resolution ([[2,4,0,0,0,3,5,9,0],\
             [6,0,3,2,5,0,0,0,0],\
             [0,0,5,0,0,8,6,2,0],\
             [5,0,0,0,0,2,3,0,7],\
             [0,0,9,0,0,0,2,0,0],\
             [8,0,1,7,0,0,0,0,5],\
             [0,3,6,5,0,0,8,0,0],\
             [0,0,0,0,8,1,7,0,6],\
             [0,1,8,3,0,0,0,5,9]])