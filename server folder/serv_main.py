import time
import sql_serv as Srvsql
import soket_connect as Srvsocket
import keyboard
import os

COMPTEUR = 0





if __name__ == '__main__':  # This is necessary for Windows because the multiprocessing module uses the 'spawn' start method by default on Windows
    
    
    sql_server = Srvsql.SQLServer()   # Create an instance of the SQLServer class
    socket_server = Srvsocket.SokServer() # Create an instance of the SokServer class
    err = socket_server.ServerIsErr() # Start the server

    if err == True:
        print('Arrêt du serveur imminent M!!!')
        os.system('powershell kill -n python3.10')
        exit()
    
    
    COMPTEUR += 1
    print('Main time:', COMPTEUR)
    socket_server.StartParalleleClientManager()
    time.sleep(1)

    
    while True:
        
        if socket_server.GetClientCompter() < 1:
            print('Compteur de boucle :', COMPTEUR)
            print('nombre de client connecté :', socket_server.GetClientCompter())
            print('Pas de client connecté')

        # if keyboard.is_pressed('q'):
        #     socket_server.StopParalleleClientManager()
        #     exit()
            

        COMPTEUR += 1




