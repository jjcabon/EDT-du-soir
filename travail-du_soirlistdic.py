#Projet Bloc 2 Réalisé par Hary Andriananjafy, Mohamed Malide, Serge Marcoccia et Jean-Jacques Cabon
#Décembre 2019
#
#
#Objectifs

#Créer et utiliser un dictionnaire
#Utiliser un algorithme glouton pour créer des listes
#Objectif pédagogique: saisir l'emploi du temps d'un élève
#saisir un niveau estimé pour chaque matière
#Utiliser cet emploi hebdomadaire pour optimiser son travail du soir
#On demande à l'élève combien d'heures il prévoit pour chaque soir.
#que cela fera une demi heure par matiere
#chaque discipline sera affectée d'un coefficient selon le niveau estimé par le participant
#Bon= 1 Moyen = 2 Faible = 3
#Le travail effectué la veille d'un cours sera valorisé  et son coefficient sera doublé
#on cherchera alors les coefficients les plus importants pour etablir un planning pour chaque soir
#On calculera ensuite le score realise pour chaque matiere dans la semaine et le score total pour motiver l utilisateur
#on profitera de ces scores pour proposer une orientation
#on utilisera un algorithme KPPV

#on donne un emploi du temps pour tester les différentes fonctions
EDT215={'mercredi': {'histoire': 1, 'svt': 0, 'espagnol': 0, 'sciences_economiques': 0, 'anglais': 0, 'physique': 0, 'mathematiques': 0, 'informatique': 0, 'francais': 0}, 'jeudi': {'histoire': 0, 'svt': 0, 'espagnol': 0, 'sciences_economiques': 0, 'anglais': 1, 'physique': 1, 'mathematiques': 1, 'informatique': 1, 'francais': 1}, 'mardi': {'histoire': 0, 'svt': 1, 'espagnol': 1, 'sciences_economiques': 0, 'anglais': 1, 'physique': 0, 'mathematiques': 0, 'informatique': 0, 'francais': 0}, 'samedi': {'histoire': 0, 'svt': 0, 'espagnol': 0, 'sciences_economiques': 0, 'anglais': 0, 'physique': 0, 'mathematiques': 0, 'informatique': 0, 'francais': 0},'lundi': {'histoire': 1, 'svt': 0, 'espagnol': 1, 'sciences_economiques': 1, 'anglais': 1, 'physique': 0, 'mathematiques': 1, 'informatique': 0, 'francais': 1}, 'vendredi': {'histoire': 1, 'svt': 0, 'espagnol': 0, 'sciences_economiques': 1, 'anglais': 1, 'physique': 0, 'mathematiques': 1, 'informatique': 0, 'francais': 1}, 'aptitude': {'histoire': 11, 'svt': 13, 'espagnol': 11, 'sciences_economiques':13 , 'anglais': 13, 'physique': 11, 'mathematiques': 16, 'informatique': 16, 'francais': 11}, 'lundi': {'histoire': 0, 'svt': 0, 'espagnol': 1, 'sciences_economiques': 0, 'anglais': 1, 'physique': 1, 'mathematiques':1, 'informatique': 0, 'francais': 1}}

#ces deux listes serviront de référence pour la suite
semaine=['lundi','mardi','mercredi','jeudi','vendredi','samedi']
matieres=['anglais', 'espagnol', 'francais', 'physique', 'mathematiques', 'svt','sciences_economiques', 'histoire','informatique']


#CREATION DE DICTIONNAIRES
#Consigne eleve
#       Un dictionnaire dans Python a la structure dict={clé:valeur, clé2:valeur2 ... }
#       On le crée par une instruction dict[clé] = valeur
#       Cette structure ne conserve pas l'ordre
#       En utilisant ces deux listes semaine et matieres, définir une fonction saisieEDT(jour,matieres) qui renvoie un dictionnaire
#       dont les clés sont les matières et les valeurs 1 ou 0 selon qu'il y a ou non cours ce jour la
#       Creer une fonction saisieEDTdic(semaine,matieres) qui renverra un dictionnaire dont
#       les clés sont les jours et les valeurs les dictionnaires renvoyés par la fonction saisieEDT et un dictionnaire "aptitude"
#       de clés les matières et de valeurs 1, 2 ou 3 selon le niveau dans la matiere bon=1 moyen=2 faible=3

def saisieEDTDic(semaine,matieres):
    EDT={}
    for jour in semaine:        # On va saisir tous les cours de la semaine jour apres jour
        dd=jour
        dd={}

        for cours in matieres:
            print("avez vous",cours,"le",jour,"oui/non")
            result=input(cours)
            if result=='oui':
                dd[cours]=1          #jour sera un dictionnaire dont les cles sont les matieres
            else:                       # et les valeurs 1=il y a cours 0=il ny a pas de cours
                dd[cours]=0           #il suffira de taper entrer sil ny a pas de cours
        EDT[jour]=dd
    aptitude={}
    print("quel est votre niveau en ? Bon=1, Moyen=2, Faible=3")
    for m in matieres:
        resp=input(m)
        if resp=='Bon' or resp=='bon' or resp =='1':
            aptitude[m]=1
        elif resp=='Moyen' or resp=='moyen' or resp=='2':
            aptitude[m]=2
        else:
            aptitude[m]=3
    EDT["aptitude"]=aptitude
    return(EDT)                         #on renverra un dictionnaire de six dictionnaires de lundi
                                        # a samedi et un septieme pour les aptitudes


# UTILISATION ET MODIFICATION D UN DICTIONNAIRE
#Consigne élève
#           Pour utiliser un dictionnaire, on utilise dict[cle] qui renvoie la valeur.
#           Pour parcourir un dictionnare on utilise for nom in dict.keyes():
#           ou bien   for nom in dict.values():
#           et  for nomclé, nomvaleur in dict.items():

#           Definir une fonction parametreEDT qui prend un dictionnaire EDT créé par saisieEDTdic
#           Les clés seront les matières et les valeurs les coefficients d'aptitude et le double si
#           cette matière intervient le lendemain ou le lundi pour le samedi
#           On renverra un dictionnaire de 6 jours
#           on pourra commencer par traiter le samedi à part des autres jours puisque le lendemain correspond à lundi
#           ou on cherchera des astuces en utilisant k%6 qui donne le reste de la division de k par 6


#Premiere version en utilisant une fonction reste pour obtenir lundi lendemain de samedi

def parametreEDT(semaine,matieres,EDT):
    touslessoirs={}
    for j in range(6):
        jour=semaine[j]
        k=(j+1)%6               #quand j=5 donc samedi j+1=6 mais semaine[6] n'existe pas
        lendemain=semaine[k]    #on prend alors =j+1%6 donc k=0 et lendemain=lundi
        cesoir=EDT[lendemain]   #on contourne la difficulté
        for matiere in cesoir.keys():
            cesoir[matiere]+=1
            cesoir[matiere]=cesoir[matiere]*EDT["aptitude"][matiere]
        touslessoirs[jour]=cesoir
    return(touslessoirs)

#Deuxieme version en traitant samedi a part du reste de la semaine
def parametreEDT2(semaine,matieres,EDT):
    touslessoirs={} # on va creer un dictionnaire de six dictionnaires de cles les jours
                    # et a chaque matiere on donne une valeur
    semaine.append('lundi')#on ajoute la valeur 'lundi' qui sera le lendemain de 'samedi'
    for j in range(6):# de lundi a samedi
        jour=semaine[j]
        cesoir=jour
        lendemain=semaine[j+1]
        jour={}
        for matiere,valeur in EDT[lendemain].items():
            if valeur==1:
                jour[matiere]=2*EDT["aptitude"][matiere]
            else:
                jour[matiere]=EDT["aptitude"][matiere]
        # sil y a cours le lendemain on double le coefficient d_aptitude
        # sinon on prend le coefficient
        touslessoirs[cesoir]=jour

    return(touslessoirs)    # on retourne 6 dictionnaires de cles jours et valeurs les matieres avec un coefficient

#autre version utilisant le fait que semaine[-1]=samedi
def parametreEDT3(semaine,matieres,EDT):
    touslessoirs={}
    for j in range(6):
        k=6-j-1
        jour=semaine[k]
        lendemain=semaine[k+1]
        cesoir=EDT[lendemain]
        for matiere in cesoir.keys():
            cesoir[matiere]+=1
            cesoir[matiere]=cesoir[matiere]*EDT["aptitude"][matiere]
        touslessoirs[jour]=cesoir
    return(touslessoirs)



#TRI DANS UN DICTIONNAIRE
#consigne :
#       Un dictionnaire ne conserve pas l'ordre et il n'est pas simple de le trier par valeurs décroissantes
#       Toutes les stratégies de tri utilisées pour les listes ne peuvent plus s'appliquer
#       Définir une fonction EDTsoir qui prend un des EDTjour créé par la fonction parametreEDT
#       Cette fonction demande au participant le nombre d'heures travaillée ce jour, définit le nombre de matières travaillées
#       et va rechercher un par un un nombre égal de matières dont les coefficients sont maximaux parmi EDTjour;
#       Penser à éliminer du dictionnaire à chaque étape la matière dont le coefficient est maximal avec l'instruction del(dict[clé])
#        Cette fonction renverra un dictionnaire menu de quelques matières avec leurs coefficients.

def EDTdusoir(EDTjour):
    menu={}

    heure=int(input("combien d_heures_voulez_vous_travailler_ce_soir?"))
    temps=2*heure
    for h in range(temps):          # on prendra une demi heure pour chaque matiere
         max=0                      # a chaque boucle on commence par 0 et on recherche une valeur superieure de proche en proche
         for matiere in EDTjour.keys():
            if EDTjour[matiere]>max:  #si un coefficient est superieur a max alors max prend cette valeur et on memorise la matiere correspondante
             result=matiere         # si max est superieur au coefficient alors il garde sa valeur
             max=EDTjour[matiere]
         menu[result]=max
         print("max trouve",result,menu[result])
         del(EDTjour[result])               #on s'assure que la matiere reperee ne servira plus dans les comparaisons
    return(menu)



#       Définir une fonction plandetravail qui prend un emploi du temps créé par parametreEDT
#       et renvoie un dictionnaire lesoir dont les clés sont les jours et les valeurs des dictionnaires créés par EDTdusoir


def plandetravail(EDT):
    lesoir={}
    for jour in EDT.keys():
        print("aujourdhui,  ",jour)
        lesoir[jour]=EDTdusoir(EDT[jour])
    return(lesoir)


#ALGORITHME KPPV ORIENTATION
# Pour motiver l'eleve à travailler en respectant le plan donne on calculera un score qui va mesurer l'efficacite de son travail.
#Ecrire une fonction calculScore qui prendra comme parametres un dictionnaire EDT cree par plandetravail et qui renverra un dictionnaire score dont les cles seront
#les matieres de matieres et les valeurs le total des valeurs correspondant de EDT et un total de toutes les valeurs de score.
#
#on commencera a initialiser score a 0 en utilisant la liste matieres avant de passer aux calculs

def calculScore(EDT,matieres):
    score={}
    total=0
    for m in matieres:#Initialisation de score avec la liste matieres
            score[m]=0
    for jour in EDT.keys():#calcul de score a partir de EDT
        EDTjour=EDT[jour]
        for matiere in EDTjour.keys():
            score[matiere]=score[matiere]+EDTjour[matiere]
    for matiere in score.keys():
        total=total+score[matiere]
    print('score total',total)
    return(score)

#Definir une fonction orientation qui prend un dictionnaire score et qui renvoie un dictionnaire possibles dont les cles sont les voies possibles, cles
#d un dictionnaire voies definies pour les choix de specialites selon les futurs metiers par exemple on pourra consulter le site l Etudiant
#cette orientation prend en compte le choix de son niveau, et son emploi
#Le choix fait dans ce programme est de favoriser les matieres ou l utilisateur se declare moins a l aise pour le faire progresser.
#Pour compenser ce biais il serait possible de saisir les moyennes trimestrielles au lieu des preferences

def orientation(score):
    #exemple de choix de specialites
   voies={'sciences1':{'mathematiques','physique','svt'},'lettres1':{'francais','anglais','histoire'},'lettre2':{'francais','espagnol','histoire'},'sceco':{'sciences_economiques','anglais','histoire'},'sciences2':{'physique','mathematiques','anglais'}}
   possibles={}#les cles seront celles de voies
   for v in voies.keys():#on explore les voies
        possibles[v]=0
        for mat in voies[v]:
            possibles[v]+=score[mat]
   return(possibles)






#fonctionnement

#emploidutemps=saisieEDTDic(semaine,matieres)
#print(emploidutemps)       #on teste
lesoir=parametreEDT(semaine,matieres,EDT215)
tuvasfaire=plandetravail(lesoir)
#print(emploidutemps)
print(lesoir)
#for jour in lesoir.keys():
 #  print(jour)
  # print(EDTdusoir(lesoir[jour]))
   #print("###########################")
print("Ce soir tu vas faire")
print(tuvasfaire)
print(" voici les scores obtenus")
Scores=calculScore(tuvasfaire,matieres)
print(Scores)
print("voici un choix d orientation")
choix=orientation(Scores)
print(choix)

#on va trier par ordre croissant sur les valeurs de choix
choix=sorted(choix.items(),key=lambda x:x[1])#
print(choix)