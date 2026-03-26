## Personal Programming Project - Yaretzi Pang
import os, time, random, cards, colorama

colours = ["R", "Y", "G", "B", "R", "Y", "G", "B", "R", "Y", "G", "B", "WC"]
status_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "S", "2+", "Re"]
numbers = 0
turn = 1
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
    os.system("clear")


def create_players():

    players = {}

    for i in range(num_of_players):
        
        players.update({f"{i}": [[], 7]})


    return players


def player_turn(players):

    card_list = get_card_list(generating)

    output_player_cards(card_list)
    get_selected_card(card_list)
    print("Place the computer where can see")
    #output_selected_card()


def get_selected_card(card_list):
    player_card = input(f"Please select what card you want to place down {card_list}\n")



def output_player_cards(card_list):

    if round == 1:
        generating = True
    else:
        generating = False

    print(f"Player {turn}, your cards are:")
    print(card_list)
    for card in card_list:
        card_design = find_card_design(card)
        time.sleep(1)
        print(card)

        # if card[0] == "R":
        #     for char in card_design:
        #         if char == "-" or char == "|" or char == " ":
        #             print(colorama.Back.RED + char, end = "")

        print(card_design)


def get_card_list(generating):

    if generating == True:
        card_list = generate_cards()

        if turn == 1:
            players["0"][0] = card_list
        elif turn == 2:
            players["1"][0] = card_list
        elif turn == 3:
            players["2"][0] = card_list
        elif turn == 4:
            players["3"][0] = card_list

    if turn == 1:
        card_list = players["0"][0]
    elif turn == 2:
        card_list = players["1"][0]
    elif turn == 3:
        card_list = players["2"][0]
    elif turn == 4:
        card_list = players["3"][0]
    
    return card_list


def find_card_design(card):
    
    if card[1:] == "0":
        card_design = cards.status_num_0
    elif card[1:] == "1":
        card_design = cards.status_num_1
    elif card[1:] == "2":
        card_design = cards.status_num_2
    elif card[1:] == "3":
        card_design = cards.status_num_3
    elif card[1:] == "4":
        card_design = cards.status_num_4
    elif card[1:] == "5":
        card_design = cards.status_num_5
    elif card[1:] == "6":
        card_design = cards.status_num_6
    elif card[1:] == "7":
        card_design = cards.status_num_7
    elif card[1:] == "8":
        card_design = cards.status_num_8
    elif card[1:] == "9":
        card_design = cards.status_num_9
    elif card[1:] == "Re":
        card_design = cards.status_reverse
    elif card[1:] == "C":
        card_design = cards.status_wild
    elif card[1:] == "2+":
        card_design = cards.status_add_2
    elif card[1:] == "S":
        card_design = cards.status_skip
    

    return card_design


def generate_cards():

    card_list = []

    for i in range(7):
        card = ""
        status = random.choice(colours)
        card = card + status

        if status == "R" or status == "Y" or status == "G" or status == "B":
            status = random.choice(status_list)
        
            card = card + status

        card_list.append(card)

    
    return card_list





print("""--------------
     UNO
--------------""")
num_of_players = int(input("How many players are playing (pick a number from 2-4)\n"))
#clear_screen()
generating = True
players = create_players()
player_turn(players)