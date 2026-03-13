## Personal Programming Project - Yaretzi Pang
import os, time

players = []
player_turn = 1
colour_list = ["R", "Y", "G", "B", "S"]
numbers = 

class Player:

    def _init_(self):
        self.player_cards = []
        self.num_of_cards = 0



def clear_screen():

    print("(clearing screen)")
    for i in range(3):
        print(".")
        time.sleep(1)
    os.system("cls")


def create_players():

    for i in range(num_of_players):
        player = Player()
        players.append(player)


def player_turn():
    
    output_player_cards()


def output_player_cards():
    get_card_list()


def get_card_list():

    if generating = True:
        generate_cards()

    if player_turn = 0:
        players[0].player_cards = 


def generate_cards():

    if player_turn = 0:
        players[0].player_cards = []



print("""--------------
     UNO
--------------""")
num_of_players = int(input("How many players are playing (pick a number from 2-4)\n"))
clear_screen()
generating = True
create_players()
player_turn()
