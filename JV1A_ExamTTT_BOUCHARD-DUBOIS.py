def alignement(n,tableau):
    tableau = n*"X"
    return(tableau)

n = 3
tableau = ["#"]

for i in range (0,n):
    tableau = n*["#"]
    print(tableau)

joueur1 = "X"
choix = int(input("quel case choisir ?\n"))
tableau [i] = choix

if(tableau[i] == [1]):
    tableau.pop[1]
    tableau.insert["X",[1]]
    print(tableau)

if(tableau[i] == [2]):
    tableau.pop[2]
    tableau.insert["X",[2]]
    print(tableau)

if(tableau[i] == [3]):
    tableau.pop[3]
    tableau.insert["X",[3]]
    print(tableau)

if(tableau[i] == [4]):
    tableau.pop[4]
    tableau.insert["X",[4]]
    print(tableau)

if(tableau[i] == [5]):
    tableau.pop[5]
    tableau.insert["X",[5]]
    print(tableau)

if(tableau[i] == [6]):
    tableau.pop[6]
    tableau.insert["X",[6]]
    print(tableau)

if(tableau[i] == [7]):
    tableau.pop[7]
    tableau.insert["X",[7]]
    print(tableau)

if(tableau[i] == [8]):
    tableau.pop[8]
    tableau.insert["X",[8]]
    print(tableau)

if(tableau[i] == [9]):
    tableau.pop[9]
    tableau.insert["X",[9]]
    print(tableau)

if (alignement == 3):
    print("You won")

#Pour pragrammer un puissance 4 il suffirait de rallonger la grille, remplacer la fonction pour que le jeu s'arrete lorsqu'il y a un allignement de 4 au lieu de 3 et de crée un programme pour quond ne puisse pas placer sont symbole lorsque qu'il y a des cases libres en dessous