#définition des modèles
import copy


Bus = {
    "idBus" : "Empty",
    "nombreDePlaces" : 0,
    "listeDesPassagers":[]
}

Passagers = {
    "idPass" : 0,
    "nomPass" : "Empty",
    "poidPass" : 0.0,
    "idBus" : "Empty"
}
# 
print('')
print('-------------------------------------------------------------------------------------------------------------------')
print("             Application de gestion des bus et des passagers au sein d'une agence de voyage         ")
print('--------------------------------------------------------------------------------------------------------------------')
print('')
#Fonction d'ajout d'un bus
listeDesBus = []

def ajoutBus():
    idBus = input("Entrez l'identifiant unique de ce bus ")
    nombreDePlaces=int(input("Entrez le nombre de places potentielles du bus "))
    listeDesPassagers = input("entrez la liste des passagers ")
    Bus["idBus"]=idBus
    Bus["nombreDePlaces"]=nombreDePlaces
    Bus["listeDesPassagers"]=listeDesPassagers
    currentBus = copy.deepcopy(Bus)
    listeDesBus.append(currentBus)
    return Bus
    
addBus = input("Veux-tu ajouter un nouveau bus? \n\t Oui/Non? ")
while addBus == "Oui":
    Bus = ajoutBus()
    listeDesBus.append(Bus)
    addBus = input("Veux-tu ajouter un nouveau bus?\n\t Oui/Non? ")
print(listeDesBus)

#Fonction d'ajout d'un Passager
listeDesPassagers = []
def nouveauPassager():
    idPass=input("Entrez l'identifiant unique de ce passager ")
    nomPass=input("Entrez le nom du passeger ")
    poidDesBagages=float(input("Entrez le poid de ses bagages "))
    idBus=input("Entrez le numéro d'identification unique de son bus ")
    Passager["idPass"]=idPass
    Passager["nomPass"]=nomPass
    Passager["poidPass"]=poidDesBagages
    Passager["idBus"]=idBus
    currentpassager = copy.deepcopy()
    listeDesPassagers.append(currentpassager)
    return Passager

addPassager = input("Veux-tu ajouter un nouveau passager?  \n\t Oui/Non? ")
while addPassager == "Oui":
    Passager = nouveauPassager()
    listeDesPassagers.append(Passager)
    addPassager = input("Veux-tu ajouter un nouveau passager?  \n\t Oui/Non? ")
print(listeDesPassagers)
print("Fin...")