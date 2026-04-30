## Personal Programming Project - Yaretzi Pang
import os, time, random, cards, cards_test
from colorama import Fore, Back, Style


colours = ["R", "Y", "G", "B", "R", "Y", "G", "B", "R", "Y", "G", "B", "R", "Y", "G", "B", "WC"]
status_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "S", "2+", "Re", "Re", "Re", "Re", "Re", "Re", "Re", "Re", "Re", "Re", "Re", "Re", "Re", "Re", "Re", "Re", "Re", "Re", "Re", "Re", "Re", "Re"]
numbers = 0
turn = 1
round = 1
win = False
selected_card = ""
selected_colour = ""
stored_card = ""
reverse_status = False


def clear_screen():

    print("(clearing screen)")
    for i in range(3):
        print(".")
        time.sleep(1)
    os.system("clear")


def create_players():

    players = {}

    for i in range(num_of_players):
        
        players.update({f"{i}": [[], 0]})


    return players


def player_turn(turn, round, selected_card, selected_colour, stored_card, win, reverse_status):

    if round == 1:
        generating = True
    else:
        generating = False


    card_list = get_card_list(generating, turn)
    #output_player_cards(card_list, turn)
    if selected_card != "draw":
        stored_card = selected_card
    
    selected_card, card_list = get_selected_card(card_list, stored_card, turn, selected_colour, round)
    #time.sleep(1)
    print("Place the computer where everyone can see")
    #clear_screen()
    print(f"Player {turn} has placed down {selected_card}")
    if selected_card != "draw":
        output_card_design(selected_card)
        players[f"{turn - 1}"][1] -= 1

    turn, selected_colour, reverse_status = card_effect(selected_card, turn, reverse_status)

    win = check_win(card_list)

    if reverse_status == False:
        if turn < num_of_players:
            turn += 1
        elif turn == num_of_players:
            turn = 1
            round += 1
    else:
        if turn == 1:
            turn = num_of_players
            round += 1
        elif turn < num_of_players:
            turn -= 1
        

    #time.sleep(3)
    if win == False:
        print(Style.BRIGHT + f"Hand the computer to player {turn}" + Style.RESET_ALL)
        #clear_screen()
        player_turn(turn, round, selected_card, selected_colour, stored_card, win, reverse_status)
    else:
        print("WINNER!")


def card_effect(card, turn, reverse_status):

    selected_colour = ""

    if card[1:] == "2+":
        print(f"Player {turn + 1} now has 2 extra cards")
        players[f"{turn}"][1] += 2
        for i in range(2):
            card = draw_card()
            players[f"{turn}"][0].append(card)
    elif card[1:] == "S":
        print(f"Player {turn + 1}'s turn has been skipped")
        turn += 1
    elif card[1:] == "Re":
        print("The order of turns has now been switched")
        reverse_status = not reverse_status
    elif card[1:] == "C":
        selected_colour = input(f"Player {turn}, choose a colour\n")
        print(f"The colour is now {selected_colour}")


    return turn, selected_colour, reverse_status
    

def check_win(card_list):


    if len(card_list) != 0:
        win = False
    else:
        win = True


    return win
 

def get_selected_card(card_list, stored_card, turn, selected_colour, round):

    if stored_card != "":
        print(Style.BRIGHT + f"The previous card was {stored_card}" + Style.RESET_ALL)
    player_card = input(f"Please select what card you want to place down {card_list} or 'draw' to draw a card\n")
    valid_card = check_selected_card(stored_card, player_card, turn, selected_colour, round)

    while (player_card not in card_list or valid_card == False) and player_card != "draw":
        print(Fore.RED + Style.BRIGHT + "Sorry, you can't play that card" + Style.RESET_ALL)
        player_card = input(f"Please select what card you want to place down {card_list} or 'draw' to draw a card\n")
        valid_card = check_selected_card(stored_card, player_card, turn, selected_colour, round)


    if player_card == "draw":
        new_card = draw_card()
        players[f"{turn - 1}"][1] += 1
        card_list.append(new_card)
        print(f"Your cards are now {card_list}")
    else:
        card_list.remove(player_card)

    return player_card, card_list


def draw_card():

    card = ""
    status = random.choice(colours)
    card = card + status

    if status == "R" or status == "Y" or status == "G" or status == "B":
        status = random.choice(status_list)
    
        card = card + status


    return card


def check_selected_card(stored_card, selected_card, turn, selected_colour, round):

    valid_card = False

    if stored_card != "WC":

        if round == 1 and turn == 1:
            valid_card = True
        else:
            if stored_card[0] == selected_card[0] or (stored_card[1:] == selected_card[1:]) or selected_card == "WC":
                valid_card = True
            else:
                valid_card = False
           
    else:
        if selected_card[0] == selected_colour:
            valid_card = True
        else:
            valid_card = False

    if round == 1:
        if selected_card[1:] == "S" or selected_card[1:] == "Re" or selected_card[1:] == "2+" or selected_card[1:] == "C":
                    print(Fore.RED + "Special card cannot be played during round 1")
                    valid_card = False

    return valid_card


def output_player_cards(card_list, turn):

    print(f"Player {turn}, your cards are:")

    for card in card_list:
        output_card_design(card)
        time.sleep(1)



def get_card_list(generating, turn):

    if generating == True:
        card_list = generate_cards(turn)

        players[f"{turn - 1}"][0] = card_list

    card_list = players[f"{turn - 1}"][0]
    
    return card_list


def output_card_design(card):
    
    if card[1:] == "0":
        card_design = cards_test.status_num_0
    elif card[1:] == "1":
        card_design = cards_test.status_num_1
    elif card[1:] == "2":
        card_design = cards_test.status_num_2
    elif card[1:] == "3":
        card_design = cards_test.status_num_3
    elif card[1:] == "4":
        card_design = cards_test.status_num_4
    elif card[1:] == "5":
        card_design = cards_test.status_num_5
    elif card[1:] == "6":
        card_design = cards_test.status_num_6
    elif card[1:] == "7":
        card_design = cards_test.status_num_7
    elif card[1:] == "8":
        card_design = cards_test.status_num_8
    elif card[1:] == "9":
        card_design = cards_test.status_num_9
    elif card[1:] == "Re":
        card_design = cards_test.status_reverse
    elif card[1:] == "C":
        card_design = cards_test.status_wild
    elif card[1:] == "2+":
        card_design = cards_test.status_add_2
    elif card[1:] == "S":
        card_design = cards_test.status_skip
    
    for line in card_design:
            l = ""
            for char in line:

                if char == ":":
                    l += Style.RESET_ALL + Back.WHITE + char + Style.RESET_ALL

                elif card[0] == "R" or char == "/":
                    l += Style.RESET_ALL + Back.RED + char + Style.RESET_ALL
                elif card[0] == "Y" or char == "]":
                    l += Style.RESET_ALL + Back.YELLOW + char + Style.RESET_ALL
                elif card[0] == "B" or char == ";":
                    l += Style.RESET_ALL + Back.CYAN + char + Style.RESET_ALL
                elif card[0] == "G" or char == "[":
                    l += Style.RESET_ALL + Back.GREEN + char + Style.RESET_ALL
                else:
                        l += Style.RESET_ALL + char + Style.RESET_ALL
                


            print(l)


def generate_cards(turn):

    card_list = []

    for i in range(7):
        players[f"{turn - 1}"][1] += 1
        card = draw_card()
        card_list.append(card)

    
    return card_list





print("""--------------
     UNO
--------------""")
num_of_players = 0
while num_of_players < 2 or num_of_players > 4:
    num_of_players = int(input("How many players are playing (pick a number from 2-4)\n"))
clear_screen()
generating = True
players = create_players()
player_turn(turn, round, selected_card, selected_colour, stored_card, win, reverse_status)


