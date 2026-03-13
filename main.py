## Personal Programming Project - Yaretzi Pang
import os, time


players = []
player_turn = 1

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


def check_player_turn():
    pass

print("""--------------
     UNO
--------------""")
num_of_players = int(input("How many players are playing (pick a number from 2-4)\n"))
clear_screen()
create_players()
check_player_turn()