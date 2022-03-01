from flask import Flask, render_template, request
from data import Connexion


# on appelle le constructeur de flask pour notre appli
app = Flask(__name__)


# page d'accueil, le / appelle le nom de domaine
@app.route('/')
def accueil() :
    return render_template('index.html', title = 'Breizhibus')


# page de connexion
@app.route('/connexion')
def connexion():
    return render_template('formulaire.html')

# page pour visualiser les lignes
@app.route('/lignes') #, methods = ['POST'])
def voir_lignes():
    lignes = Connexion.lister_lignes()
    return render_template('lignes.html', post = lignes)

# page pour visualiser les arrêtes
@app.route('/arrets/<int:id_ligne>')
def voir_arrets(id_ligne):
    arrets = Connexion.lister_arrets(id_ligne)
    return render_template('arrets.html', post = arrets)
                            # arrets.html




@app.route('/connexion')
def identifier(cls, pseudo, mdp): #cls?
    connexion = False

    Connexion.ouvrir_connexion()
    requete = "SELECT identifiant, mdp from utilisateurs WHERE identifiant = %s AND mdp = %s"
    # requete = "SELECT identifiant, mdp from utilisateurs WHERE identifiant = {pseudo} AND mdp = {mdp}"
    cle = (pseudo, mdp)

    Connexion.__cursor.execute(requete, cle)
    if Connexion.__cursor.fetchone :
        connexion = True

    Connexion.fermer_connexion()
    return render_template("formulaire.html")

@app.route("/autoriser", methods=['POST'])
def autoriser():
    pseudo = request.values.get("username") # username est le nom inscrit dans le formulaire
    mdp = request.values.get("password") # idem pour password
    connexion = Connexion.identifier(pseudo, mdp)
    return render_template("identifier.html", qui = pseudo, reponse = connexion) # exemple = vous êtes authentifiés

# ajouter un bus (formulaire)
@app.route("/autorisation/ajouter", methods=['GET', 'POST'])
def ajouter_bus():
    # 1 formulaire pour ajouter un bus
    return render_template("ajouter_bus.html")
    


#ajout d'un bus à la liste
@app.route('/add', methods=['GET'])
def add():
    numero = request.values.get('numero')
    immatriculation = request.values.get('immatriculation')
    nombre_places=request.values.get('nombre_place')
    ligne=request.values.get('id_ligne')

    Connexion.ajouter_bus(numero, immatriculation, nombre_places, ligne)
    return render_template('add.html')


@app.route("/autorisation/modifier", methods=['GET'])
def modifier_bus():
    numero = request.values.get('numero')
    immatriculation = request.values.get('immatriculation')
    nombre_places=request.values.get('nombre_place')
    ligne=request.values.get('id_ligne')
    bus=request.values.get("id_bus")

    Connexion.modifier_bus(bus, numero, immatriculation, nombre_places, ligne)
    return render_template("modifier_bus.html")

#modification d'un bus à la liste
@app.route('/modd', methods=['GET'])
def modd():
    numero = request.values.get('numero')
    immatriculation = request.values.get('immatriculation')
    nombre_places=request.values.get('nombre_place')
    ligne=request.values.get('id_ligne')
    bus=request.values.get("id_bus")

    Connexion.modifier_bus(bus, numero, immatriculation, nombre_places, ligne)
    return render_template("modifier_bus.html")

# Méthode pour supprimer un bus
# @app.route("/autorisation/modifier", methods=['GET'])



# lance automatiquement le serveur en mode debug
# False = pour la production, désactive les messages
if __name__ == "__main__":
    app.run(debug=True)


    