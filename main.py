from C_Table import C_Table
from utilite import input_in_range,input_plus,afficher_list,input_in_list

class Etudient(C_Table):
    A = {"CNE":"TEXT NOT NULL UNIQUE",
         "CIN":"TEXT NOT NULL UNIQUE",
         "full_name":"TEXT NOT NULL",
         "date_naissance":"TEXT",
         "Nationalite":"TEXT",
         "tel":"TEXT NOT NULL",
         "Email":"TEXT NOT NULL",
         "cordonnes":"TEXT"}

    # def __init__(self):
    #     super(C_Table, self).__init__("daad.db")

    def sasier_Etudient(self,*args):
        self.CNE = input_plus("Donner le CNE",0,*args)
        if ((self.all_etudient_filtter(CNE=self.CNE)) and (tuple(self.all_etudient_filtter(CNE=self.CNE)) != args)):
            print("ce Etudient deja existe")
            return
        self.CIN = input_plus("Donner le CIN",1,*args)
        if ((self.all_etudient_filtter(CIN=self.CIN)) and (tuple(self.all_etudient_filtter(CIN=self.CIN)) != args)):
            print("ce Etudient deja existe")
            return
        self.full_name = input_plus("donner nom et prenom",2,*args)
        self.date_naissance = input_plus("doner la date de naissance de l'etudient",3,*args)
        self.Nationalite = input_plus("donner nationalite",4,*args)
        self.tel = input_plus("donner le numero de telephone",5,*args)
        self.Email = input_plus("donner Email",6,*args)
        self.cordonnes = input_plus("donner CodePostal/Pays/Ville/Adresse ",7,*args)


    @staticmethod
    def Liste_Cmd_Etudiants():
        return(["1. Enregistrer un étudiant",
           "2. Chercher un étudiant par son Nom ou son CNE",
           "3. Modifier les données d'un étudiant",
           "4. Afficher la liste de tous les étudiants",
           "5. Supprimer les données d'un étudiant",
           "6. Quitter le programme"
           ])




class Menu:

    def traiter_menu(self):
        Etudient.create_table()
        L=Etudient.Liste_Cmd_Etudiants()
        while True:
            print("\n")
            afficher_list(L)
            choix=input_in_range(L)
            if choix==1:
                self.enregistrer_un_étudiant()
            elif choix==2:
                print(self.chercher_un_étudiant())
            elif choix==3:
                self.modifier_étudiant()
            elif choix==4:
                if Etudient.all_etudient_filtter():
                    for elem in Etudient.all_etudient_filtter():
                        print(elem)
                else:
                    print('aucun etudient dans la base done')
            elif choix == 5:
                self.supprime_etudient()
            elif choix == 6:
                print("Gestion des étudiants terminée")
                break
    @staticmethod
    def enregistrer_un_étudiant():
        a = Etudient()
        a.sasier_Etudient()
        a.save()
    @staticmethod
    def chercher_un_étudiant():
        print("taper un nombre pour le champ que tu veut chercher par")
        x = input_in_list(list(Etudient.A.keys()))
        a = input("donner la valeur correspandant a le champ que tu choisie ")
        if Etudient.all_etudient_filtter(**{x: a}):
            return input_in_list(Etudient.all_etudient_filtter(**{x: a}))
        else:
            print("ce etudient ne pas existe tu peut le ajoute")
    @staticmethod
    def modifier_étudiant():
        a = input("donner le CNE de l'etudient que tu veut modifie")
        if Etudient.all_etudient_filtter(CNE=a):
            Etudient.update_elem1(CNE=a)
        else:
            print("ce etudient ne pas existe tu peut le ajoute")
    @staticmethod
    def supprime_etudient():
        a = input("donner le CNE de l'etudient que tu veut suprime")
        if Etudient.all_etudient_filtter(CNE=a):
            Etudient.remove_elem(CNE=a)
        else:
            print("ce etudient ne pas existe")

if __name__ == '__main__':
    # cette partie s'exécute en premier lors de l'execution du programme
    M=Menu()
    M.traiter_menu()