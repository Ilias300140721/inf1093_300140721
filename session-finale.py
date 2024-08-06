#Exercice 1 code 1
def quickSortByAge(list):
    if len(list) <= 1:
        return list
    else:
        pivot = list[-1]  # Choisir le dernier élément comme pivot
        lesser = [item for item in list[:-1] if item[1] <= pivot[1]]
        greater = [item for item in list[:-1] if item[1] > pivot[1]]
        return quickSortByAge(lesser) + [pivot] + quickSortByAge(greater)

# Exemple d'utilisation
students = [("Viny", 34), ("Ryan", 43), ("Tity", 31), ("Antony", 27), ("Calvin", 39), ("Lilian", 27), ("Merlin", 19), ("Rachy", 25)]
sorted_students = quickSortByAge(students)
print(sorted_students)


#Exercice 2 code 2
#exercice 2 question 2 :
def search(arr, name, low, high):
# Si la recherche est toujours valide
    if high >= low:
# Calculer le nombre milieu
        mid = (high + low) // 2  
        
# Si le nom a l'indice milieu est qu'on cherche
        if arr[mid][0] == name:
            return arr[mid][1]
        
# Si le nom a l'indice milieu est supérieur au nom au'on cherche
        elif arr[mid][0] > name:
# Rechercher dans la liste gauche
            return search(arr, name, low, mid - 1)
        
# Si le nom a l'indice milieu est inferieur au nom au'on cherche
        else:
            return search(arr, name, mid + 1, high) 
    
    else:
# Retourner None si le nom n'est pas trouvé
        return None  

def searchByName(name):
    students = list = [("Viny",34 ), ("Ryan",43 ), ("Tity",31 ), ("Antony",27 ),("Calvin",39 ),("Lilian",27 ),("Merlin",19 ),("Rachy",25 )]
    students.sort()  # Trier la liste par ordre alphabétique des noms
# lancer la recherche dichotomique
    return search(students, name, 0, len(students) - 1)  


print(searchByName("Viny"))  # son age est 23
print(searchByName("Lilian"))  # son age est 27


#Exercice 3 code 1

def printNames(students):
    for student in students:
        print(student[0])

# L'utilisation
students = [('Merlin', 19), ('Rachy', 25), ('Antony', 27), ('Lilian', 27), ('Tity', 31), ('Viny', 34), ('Calvin', 39), ('Ryan', 43)]
printNames(students)

#Exercice 3 code 2

def printRecNames(students):
    if not students:  
        return
    # Afficher le nom du premier étudiant
    print(students[0][0])
    # Appel récursif pour le reste de la liste
    printRecNames(students[1:])

# L'utilisation
students = [('Merlin', 19), ('Rachy', 25), ('Antony', 27), ('Lilian', 27), ('Tity', 31), ('Viny', 34), ('Calvin', 39), ('Ryan', 43)]
printRecNames(students)