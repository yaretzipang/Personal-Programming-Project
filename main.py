## Personal Programming Project - Yaretzi Pang
import os, time


def clear_screen():

    print("(clearing screen)")
    for i in range(3):
        print(".")
        time.sleep(1)
    os.system("cls")


def create_players(num_of_players):

    for i in range(num_of_players):
        player_[i] = Player


class Player:

    player_cards = []
    num_of_cards = 0


print("""--------------
     UNO
--------------""")
num_of_players = int(input("How many players are playing (pick a number from 2-4)\n"))
clear_screen()
create_players(num_of_players)
