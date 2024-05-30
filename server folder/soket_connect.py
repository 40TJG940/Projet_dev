import socket
import time
import os
import sqlite3
import sys
from threading import Thread
from _thread import interrupt_main
import keyboard


SQL_con = sqlite3.connect("game.db")
SystemPassCompter = 0


class SokServer:  

    def __init__(self):
        self.stop_thread = False
        self.aff = True
        self.ClientID = {}
        self.ClientCompter = 0
        self.addr = None

        global SystemPassCompter
        print('Passage dans __init__ numéro :', SystemPassCompter)
        SystemPassCompter += 1

        if SystemPassCompter == 1:
            if self.StartServer(True)  == True:
                print('Arrêt du serveur imminent !!!')
                os.system('powershell kill -n python3.10')
                exit()
            else:
                print('__init__ ok')
                return
        else:
            print("Alerte !! Second passage dans __init__")
            os.system('powershell pause')
            self.close(self.s)
        
    def StartServer(self, en):
        
        print("liaison ok")
        
        if en == True:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ip = '' # Adresse IP du serveur
            port = '' # Port du serveur

            # reseigner l'adresse IP de votre serveur
            ip = input("Entrez l'adresse IP du serveur : ")
            port = int(input("Entrez le port du serveur : "))  # Convert the input to an integer

            # Utilisez votre adresse IP ou nom d'hôte
            self.server_address = (ip , port)

        try:
            self.s.bind(self.server_address) # Liaison de l'adresse IP et du port
            self.s.listen(5) # Nombre de connexions autorisées
            print("liaison ok")
            self.status = False
            return False
        except socket.error as e:
            print('Erreur de liaison')
            self.status = True
            return True
        except KeyboardInterrupt:
            print('Arrêt du serveur kb')
            self.status = True
            return True
        # except: # Si une erreur se produit
        
    def ServerIsErr(self):
        return self.status
        
    def Add_ClientID(self, addr, aff):

        self.ClientCompter += 1
        self.ClientID[self.ClientCompter] = addr
        if aff == True:
            self.Affiche_ClientID()

    def Affiche_ClientID(self):
        os.system('powershell clear')
        print('+++ Added  ClientID:' , self.addr)
        print('=== Client list : ')
        for client in self.ClientID:
            print(self.ClientID[client],'\r')
        print('--- Client Compter:', self.ClientCompter)

    def StartParalleleClientManager(self):
        self.stop_thread = False
        self.process = Thread(target=self.ClientAutoAdder)
        self.process.start()

    def StopParalleleClientManager(self):
        self.stop_thread = True
        print('Arrêt du serveur imminent !!!')

    def GetClientCompter(self):
        return self.ClientCompter 

    def ClientAutoAdder(self):
        

        if keyboard.is_pressed('q'):
            exit()


        try:
            self.s.listen(5) # Nombre de connexions autorisées
            print("try : liaison ok")
            
        except socket.error as e:
            print('try : Erreur de liaison')
            return True
        except KeyboardInterrupt:
            print('try : Arrêt du serveur kb')
            return True


        while not self.stop_thread:
            if KeyboardInterrupt == True:
                os.system('powershell keybord_interrupt')
                os.system('powershell kill -n python3.10')
                break
            if keyboard.is_pressed('q'):
                os.system('powershell keybord_interrupt')
                os.system('powershell kill -n python3.10')
                break

            
            con, addr = self.s.accept() # Accepte la connexion
            print('Connecté par', addr)  # Affiche l'adresse du client
            
            data = con.recv(1024) # Récupère les données du client
            if data.decode() == 'lancer une partie':
                print('Demande acceptée')
                con.sendall('demande accepter'.encode())
                self.Add_ClientID(addr,self.aff)
                SQL_con.execute("INSERT INTO  (player1, player2) VALUES ('', '')")
            # if data.decode() == 'add_playername':
            #     print('adding player name')
            #     data = data.decode()
            #     print('player name :', data)
            #     con.sendall('joueur ajouté'.encode())
            
            time.sleep(0.01)
        
    def client_connect(self):

        # reseigner l'adresse IP de votre client
        self.ip_client = input("Entrez l'adresse IP du client : ")
        self.port_client = input("Entrez le port du client : ")
        
        # Utilisez votre adresse IP ou nom d'hôte
        self.server_address = (self.ip , self.port)

        con, addr = self.s.accept() # Accepte la connexion
        print('Connecté par', addr)  # Affiche l'adresse du client

        con.sendall('Bienvenue sur le serveur'.encode())
        return con ,addr

    def send(self, con, data):
        con.sendall(data.encode())

    def receive(self, con):
        data = con.recv(1024).decode()
        return data
    
    def close(self, con):
        con.close()
        self.s.close()
    
