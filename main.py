import sqlite3

parametres_connexion = {
    'dbname': 'test1.db'  # SQLite uses a local file as the database
}

class Interface:
    def __init__(self, para):
        self.parametre_connexion = para
        self.connexion = sqlite3.connect(parametres_connexion['dbname'])
        self.curseur = self.connexion.cursor()
        self.categorie = ["Personal", "Work", "Important"]

        # Appeler la fonction d'initialisation de la base de données
        self.initialize_database()

    def initialize_database(self):
        self.curseur.execute('''
            CREATE TABLE IF NOT EXISTS note (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                contenu TEXT NOT NULL,
                categorie TEXT NOT NULL
            );
        ''')
        self.connexion.commit()

    def choose_categorie(self):
        for index, ele in enumerate(self.categorie):
            print(f"{index}: {ele}")
        choose_cat = int(input("Select category: "))
        return self.categorie[choose_cat]

    def add_note(self):
        contenu = str(input('Content: '))
        categorie = str(self.choose_categorie())
        self.curseur.execute(f"INSERT INTO NOTE (contenu, categorie) VALUES (?, ?);", (contenu, categorie))
        self.connexion.commit()

    def consult_note(self):
        self.curseur.execute("SELECT * FROM note;")
        result = self.curseur.fetchall()
        for ligne in result:
            print(ligne)

    def note_by_id(self):
        note_id = input('What is the id of the note: ')
        self.curseur.execute("SELECT * FROM note WHERE id = ?;", (note_id,))
        print(self.curseur.fetchall())

    def leave(self):
        self.curseur.close()
        self.connexion.close()

def CLI(parametres_connexion):
    interface_for_user = Interface(parametres_connexion)
    koi_faire = ["1.Add note", "2.Consult Note", "3.Note by id", "4.Exit"]
    while True:
        for ele in koi_faire:
            print(ele)
        nav = input("What do you want to do? :")
        if nav == "1":
            interface_for_user.add_note()
        elif nav == "2":
            interface_for_user.consult_note()
        elif nav == "3":
            interface_for_user.note_by_id()
        elif nav == "4":
            interface_for_user.leave()
            return False
        else:
            print("Invalid Input")

CLI(parametres_connexion)