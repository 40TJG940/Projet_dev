import socket
import time
import sqlite3
con = sqlite3.connect("game.db")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 9109
s.bind(('', port))

s.listen(5) # Nombre de connexions autorisées (5 maximum)
conn, addr = s.accept() # Accepte la connexion
print('Connecté par', addr)  # Affiche l'adresse du client




data = conn.recv(1024) # Récupère les données du client
if data:
    print("Server à reçu :",data.decode()) # Affiche les données reçues du client
    if data.decode() == 'lancer une partie': #  Si les données reçues du client sont égales à 'client: lancer une partie'
        print("Server : le client veut lancer une partie")
        time.sleep(1.3)
        print("Server : Envoie de la réponse")
        time.sleep(1.3)
        conn.sendall('Demande acceptée'.encode()) # Envoie des données au client
    else:
        print('server : requête inattendue reçue')
else:
    print('Pas de données')


conn.sendall('Au revoir'.encode())



print('Fermeture de la connexion')
conn.close()
s.close()