import Puissance4 as P4
import client_socket as CS
import time


game = P4.Game()  # Create an instance of Game
Soket_client = CS.ClientSocket() # Create an instance of ClientSocket


#game.init_game() # Call the game_init method from the Game class in the Puissance4.py file
#game.play() # Call the play method from the Game class in the Puissance4.py file

Soket_client.connect() # Call the connect method from the ClientSocket class in the client_socket.py file
Soket_client.send_message('lancer une partie') # Call the send_message method from the ClientSocket class in the client_socket.py file
message = Soket_client.receive_message() # Call the receive_message method from the ClientSocket class in the client_socket.py file
print ("recp : " + message) # Print the message received from the server
time.sleep(1.3) # Pause the program for 1.3 seconds

print ("demarrage du jeu...")
time.sleep(1.3) # Pause the program for 1.3 seconds

print("Entrez le nom du joueur")
game.get_username() # Call the get_username method from the Game class in the Puissance4.py file
time.sleep(1.3) # Pause the program for 1.3 seconds 

print("envoi du nom du joueur au serveur")
Soket_client.send_message("add_playername") # Call the send_message method from the ClientSocket class in the client_socket.py file
Soket_client.send_message({game.player1}) # Call the send_message method from the ClientSocket class in the client_socket.py file
print("attente de la confirmation du serveur")
message = Soket_client.receive_message() # Call the receive_message method from the ClientSocket class in the client_socket.py file
if message == 'joueur ajouté': # Check if the message received from the server is 'demande acceptée'
    print("demande acceptée joueur ajouté") # Print 'demande acceptée'
else:   
    print('demande refusée')
    exit()

print("attente de l'adversaire")





game.play() # Call the play method from the Game class in the Puissance4.py file