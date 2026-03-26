## Personal Programming Project - Yaretzi Pang
import os, time, random

status_list = ["R", "Y", "G", "B", "S", "2+", "W", "Re"]
colours = ["R", "Y", "G", "B"]
numbers = 0
turn = 0
round = 1

class Player:

    def __init__(self):
        self.player_cards = []
        self.num_of_cards = 7


def clear_screen():

    print("(clearing screen)")
    for i in range(3):
        print(".")
        time.sleep(1)
    os.system("cls")


def create_players():

    players = {}

    for i in range(num_of_players):
        
        players.update({f"{i}": [[], 7]})


    return players


def player_turn(players):

    output_player_cards()
    #get_selected_card()
    #output_selected_card()


def output_player_cards():

    if round == 1:
        generating = True
    else:
        generating = False

    card_list = get_card_list(generating)

    print(card_list)



def get_card_list(generating):

    if generating == True:
        card_list = generate_cards(turn)

    
    if turn == 1:
        card_list = players[0][1][0]
    elif turn == 2:
        card_list = players[1][1][0]
    elif turn == 3:
        card_list = players[2][1][0]
    elif turn == 4:
        card_list = players[3][1][0]
    
    return card_list



def generate_cards(turn):

    for i in range(7):
        card = ""
        status = random.choice(status_list)
        card = card + status

        if status == "R" or status == "Y" or status == "G" or status == "B":
            status = str(random.randint(0, 9))
        elif status == "S" or status == "2+" or status == "Re":
            status = random.choice(colours)
        
        card = card + status

        if turn == 1:
            (players[0][1][0]).append(card)
        elif turn == 2:
            (players[1][1][0]).append(card)
        elif turn == 3:
            (players[2][1][0]).append(card)
        elif turn == 4:
            (players[3][1][0]).append(card)





print("""--------------
     UNO
--------------""")
num_of_players = int(input("How many players are playing (pick a number from 2-4)\n"))
# clear_screen()
generating = True
players = create_players()
player_turn(players)