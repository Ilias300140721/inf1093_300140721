## Exercice 1
#### Question 1
listIdName = [(202401, "Anani"), (202402, "Simon"),(202403, "Pierre"),(202404, "Kylian"),(202405, "Alphonse"),(202406, "Joshua"),(202407, "Colince"),(202408, "Khristian"),(202409, "Zinedine"),(202410, "Didier") ]
listidgrade = [(202401, 74), (202402, 93),(202403, 59),(202404, 77),(202405, 90),(202406,73),(202407, 59),(202408,17)]
fulllist=[]
for matricule,not in listidgrade:
for mat,nom in listidname:
    if matricule==mat:
        fulllist.append((matricule,nom,note))
        break
        #affichage du resultat
        print("listes complete des candidats avec leur notes:")
        for item in fullist:
            print(f"matricule:^[item[0]),
                  nom:[item[1]],note:[item[2]]"
                  
        
print(listIdName)




## Exercice 2
#### Question 1
def searchNameById(name):
    ## Completer ici 
                  for matricule,nom not in listidname
                  if nom==name:
                  return matricule
                  return"nom nom trouvée"
                  matricule_trouve=
                  
                  

    return 0

print("Le matricule de Anani : ", searchNameById("Anani"))  ## Le matricule de Anani :  202401 
print("Le matricule de Peter : ", searchNameById("Peter"))  ## Le matricule de Peter :  0

#### Question 2
def searchGradeByIdSeq(id):
    ## Completer ici 
                  for mat,not in list grade:
                  if mat==matricule:
                  return"matricule_non_trouvée"
                  

    return 0
  
print("La note du matricule 202403 est de  : ", searchGradeByIdSeq(202403))  ## La note du matricule 202403 est de  :  73
print("La note du matricule 202405 est de  : ", searchGradeByIdSeq(202405))  ## La note du matricule 202403 est de  :  0

#### Question 3
def buildListSeq():
    ## Completer ici
                       for matricule,nom in listidNames:
                  note=
                  searchgradebyid(matricule)
                  if insinstance(note,int):
                  
                  fullist.append(matricule,nom,note))
        else:
         fulllist.append(matricule,nom,0))
            buildlist()
        print(fulllist)
                  
    return 0
    
buildListSeq()
#print(fullList)

## Exercice 3
## Question1  : implementons le tri de ton choix
def get_matricule(element):
    return element["matricule"]
def trier_par_matricule(liste):
    return sorted (liste,
                   key=get_matricule)
listIdName=
trier_par_matricule(notes)
print(listIdNames)



    
#listIdGrade = tri(listIdGrade)
#print(listIdGrade)

####Question 2
def searchGradeByIdDicho(id):
            listidgrade=
                  trier_par_matricules(notes)
                  gauche,droite=0
                  len(notes_triees)-1
                  while gauche<=droite:
                  milieu=(gauche+droite)//2
                  if notes_triees[milieu]
                  ["matricule"]==id:
                  return listeidgrade[milieu]
                  ["note"]
                    elif listidgrade[milieu]
                  ["matricule"]<id:
                  gauche=milieu+1
                  else:
                  droite=milieu-1
                  
 
    return 0
                  
## Question 3
def buildListDicho():
                  for matricule,nom in listidNames:
                  note=
                  searchgradebyid(matricule)
                  if insinstance(note,int):
                  
                  fullist.append(matricule,nom,note))
        else:
         fulllist.append(matricule,nom,0))
            buildlist()
        print(fulllist)

    return 0
    
buildListDicho()
#print(fullList)


#exercice 3 partie 1