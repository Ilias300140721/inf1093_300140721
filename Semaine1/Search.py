# Collection de numbers
numbers = []
nb = int(input("Combien de nombres : "))
for i in range(nb):
    nb = int(input(f"Nombre {i+1}: "))
    numbers.append(nb)

# Affichage des numbers
print(numbers)

# Lire la valeur à rechercher.
search_nb = int(input("Quel nombre cherchez-vous? "))

# Recherche séquentielle
position = -1
for i in range(len(numbers)):
    if search_nb == numbers[i]:
        position = i
        break
if position > -1:
    print(f"{search_nb} est à la position {position}")
else:
    print(f"{search_nb} n'existe pas dans le tableau")

# 1) Trouver la position de la valeur maximale
max_value = max(numbers)
max_position = numbers.index(max_value)
print(f"La valeur maximale est {max_value} à la position {max_position}")

# 2) Trouver la position de la valeur minimale
min_value = min(numbers)
min_position = numbers.index(min_value)
print(f"La valeur minimale est {min_value} à la position {min_position}")

# 3) Vérifier si le tableau est trié en ordre croissant
is_sorted = numbers == sorted(numbers)
if is_sorted:
    print("Le tableau est trié en ordre croissant")
else:
    print("Le tableau n'est pas trié en ordre croissant")

# 4) Recherche dichotomique dans un tableau trié en ordre décroissant
found = False
begin = 0
end = len(numbers) - 1

while not found and begin <= end:
    mid = (begin + end) // 2
    if search_nb == numbers[mid]:
        found = True
        print(f"Nombre trouvé à la position : {mid}")
    else:
        if search_nb > numbers[mid]:
            end = mid - 1  # Correction pour une recherche dans un tableau trié en ordre décroissant
        else:
            begin = mid + 1  # Correction pour une recherche dans un tableau trié en ordre décroissant

if not found:
    print("Nombre inexistant")




