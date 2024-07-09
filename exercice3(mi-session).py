# Fonction switch pour permuter deux éléments dans une liste
def switch(liste, i, j):
    liste[i], liste[j] = liste[j], liste[i]

# Fonction bubbleSort pour trier la liste par ordre alphabétique des noms
def bubbleSort(liste):
    n = len(liste)
    for i in range(n):
        for j in range(0, n-i-1):
            if liste[j][0] > liste[j+1][0]:
                switch(liste, j, j+1)
        print(f"Iteration {i+1}: {liste}")
    return liste

# Fonction selectionSort pour trier la liste par ordre croissant des âges
def selectionSort(liste):
    n = len(liste)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if liste[j][1] < liste[min_idx][1]:
                min_idx = j
        switch(liste, i, min_idx)
    return liste

# Exemple d'utilisation avec les données de l'exercice
students = [('Viny', 34), ('Ryan', 43), ('Tity', 31), ('Antony', 27), ('Calvin', 39), ('Lilian', 27)]

# Permutation des éléments 1 et 2
switch(students, 1, 2)
print("Liste complete apres permutation des elements 1 et 2:", students)

# Trie par bulle basé sur les noms
print("\nTri par bulle basé sur les noms:")
sorted_by_name = bubbleSort(students[:])

# Trie par sélection basé sur les âges
print("\nTri par sélection basé sur les âges:")
sorted_by_age = selectionSort(students[:])
print("Liste triée par sélection:", sorted_by_age)
