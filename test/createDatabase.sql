-- Création de la table Utilisateurs
CREATE TABLE Utilisateurs (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Pseudo VARCHAR(255) NOT NULL,
    MotDePasse VARCHAR(255) NOT NULL,
    DateInscription TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    MMR INT DEFAULT 1000
);

-- Création de la table File d'attente
CREATE TABLE FileAttente (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    IDUtilisateurEnAttente INT,
    DateEntree TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    AdresseIP VARCHAR(255),
    Port INT,
    FOREIGN KEY (IDUtilisateurEnAttente) REFERENCES Utilisateurs(ID)
);

-- Création de la table Parties
CREATE TABLE Parties (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    IDJoueur1 INT,
    IDJoueur2 INT,
    PlateauJeu TEXT,
    StatutFinPartie BOOLEAN DEFAULT FALSE,
    IDJoueurGagnant INT,
    IDJoueurPerdant INT,
    FOREIGN KEY (IDJoueur1) REFERENCES Utilisateurs(ID),
    FOREIGN KEY (IDJoueur2) REFERENCES Utilisateurs(ID)
);

-- Création de la table Tours
CREATE TABLE Tours (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    IDPartie INT,
    IDJoueurQuiAJoue INT,
    InformationCoupJoue VARCHAR(255),
    DateTour TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (IDPartie) REFERENCES Parties(ID),
    FOREIGN KEY (IDJoueurQuiAJoue) REFERENCES Utilisateurs(ID)
);

-- Création de la table Messages
CREATE TABLE Messages (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    IDPartie INT,
    IDUtilisateur INT,
    ContenuMessage VARCHAR(255),
    DateEnvoi TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (IDPartie) REFERENCES Parties(ID),
    FOREIGN KEY (IDUtilisateur) REFERENCES Utilisateurs(ID)
);