import mysql.connector as mysql

# création d'une classe
# modifier les infos de connexion pour connecter sa propre bdd
class Connexion :
    __user = 'root'
    __password = 'root'
    __host = 'localhost'
    __port = '8081'
    __database = 'breizhibus'
    __cursor = None 

# méthode pour ouvrir la connexion à la bdd
    @classmethod
    def ouvrir_connexion(cls):
        if cls.__cursor == None :
            cls.__bdd = mysql.connect(user = cls.__user, password = cls.__password, host = cls.__host, port = cls.__port, database = cls.__database)
            cls.__cursor = cls.__bdd.cursor()




# insertion des futures méthodes

    # méthodes pour lister les lignes de bus
    @classmethod
    def lister_lignes(cls):
        cls.ouvrir_connexion()
        query = "SELECT * FROM lignes;"
        cls.__cursor.execute(query)

        liste_lignes = []

        for element in cls.__cursor :
            liste_lignes.append(element)
            

        return liste_lignes

        cls.fermer_connexion()

    
    # méthode pour retrouver tous les arrêts d'une ligne précise
    @classmethod
    def lister_arrets(cls, ligne_selectionnee):
        # on veut les arrêts d'une ligne précise = on rajoute un paramètre

        liste_ligne = []

        if ligne_selectionnee == 1 :
            query_1 = "SELECT nom, adresse FROM arrets  natural join arrets_lignes WHERE id_ligne = 1 ;"
            cls.__cursor.execute(query_1)
            for element in cls.__cursor :
                liste_ligne.append(element)
            return liste_ligne

        elif ligne_selectionnee == 2 :
            query_2 = "SELECT nom, adresse FROM arrets  natural join arrets_lignes WHERE id_ligne = 2 ;"
            cls.__cursor.execute(query_2)
            for element in cls.__cursor :
                liste_ligne.append(element)
            return liste_ligne

        elif ligne_selectionnee == 3 :
            query_3 = "SELECT nom, adresse FROM arrets  natural join arrets_lignes WHERE id_ligne = 3 ;"
            cls.__cursor.execute(query_3)
            for element in cls.__cursor :
                liste_ligne.append(element)
            return liste_ligne

        else :
            print("Erreur. Entrez une valeur valide...")


    #méthode pour identifier l'utilisateur (identifiant + mdp)
    @classmethod
    def identifier(cls, pseudo, mdp):
        Connexion.ouvrir_connexion()
        identification = []
        
        cls.__cursor.execute("SELECT identifiant, mdp FROM utilisateurs")
        for element in cls.__cursor :
            identification.append(element)
            

            if pseudo == identification[0][0] and mdp == identification[0][1]:
                print("Vous êtes autorisés à accéder aux modifications")
                return pseudo, mdp
            else : 
                print("Erreur. Vérifiez votre identifiant et votre mot de passe.")
                # print(identification[0])

        Connexion.fermer_connexion()

    # méthode pour ajouter un bus
    @classmethod
    def ajouter_bus(cls, numero, immatriculation, nombre_places, ligne):
        Connexion.ouvrir_connexion()
        cls.__cursor.execute(f'INSERT INTO bus(numero,immatriculation,nombre_place,id_ligne) VALUES ( "{numero}", "{immatriculation}", "{nombre_places}", "{ligne}")')
        cls.__bdd.commit()
        Connexion.fermer_connexion()



       


    # méthode pour modifier un bus
    @classmethod
    def modifier_bus(cls, id_bus, numero, immatriculation, nombre_places, ligne):
        Connexion.ouvrir_connexion()
        cls.__cursor.execute(f"UPDATE bus SET numero = '{numero}', immatriculation = '{immatriculation}', nombre_place = '{nombre_places}', id_ligne = '{ligne}' WHERE id_bus = '{id_bus}'")
        cls.__bdd.commit()
        Connexion.fermer_connexion()

    # méthode pour supprimer un bus
    @classmethod
    def supprimer_bus(cls, id_bus):
        cls.__cursor.execute(f'DELETE FROM bus WHERE id_bus = "{id_bus}"')
        cls.__bdd.commit()


# méthode pour fermer la connexion à la bdd
    @classmethod
    def fermer_connexion(cls):
        cls.__cursor.close()
        cls.__bdd.close()
        cls.__cursor = None

# print("test d'identification")
# print(Connexion.identifier('aas', 'aaaa'))
# print(Connexion.identifier('admin', 'admin'))


