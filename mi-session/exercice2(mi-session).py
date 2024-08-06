def build_list():
    students = []
    while True:
        name = input("Nom: ")
        age = int(input("Age: "))
        students.append((name, age))
        add_more = input("Ajouter un autre etudiant? (1/0) ")
        if add_more == '0':
            break
    return students

# Liste complète non triée
students_list = build_list()
print("Liste complete non triee:", students_list)