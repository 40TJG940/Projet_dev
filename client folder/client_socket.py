import socket
import time


class ClientSocket:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ip = ''
        self.port = ''
        self.message = ''

    def connect(self):
        self.ip = input("Entrez l'adresse IP du serveur : ")
        self.port = int(input("Entrez le port du serveur : "))
        server_address = (self.ip, self.port)
        print("Connexion...")
        self.s.connect(server_address)

    def send_message(self, message):
        self.s.sendall(self.message.encode())

    def receive_message(self):
        data = self.s.recv(1024).decode()
        return data

    def ask_for_game(self):
        self.send_message('lancer une partie')
        data = self.receive_message()
        if data == 'Demande acceptée':
            print("demande acceptée")
        else:
            print('demande refusée')

    def close_connection(self):
        self.s.close()



# client = ClientSocket()
# client.connect()

# client.send_message('client: Bonjour serveur')

# data = client.receive_message()
# if data:
#     print(f"Client à reçu : {data}")
#     time.sleep(1.3)
#     print("Client : envoie la demande de lancer une partie")
#     client.send_message('lancer une partie')
# else:
#     print('Client: Pas de reponse du serveur')

# client.ask_for_game()

# print('connexion terminée')
# client.close_connection()

