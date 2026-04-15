from colorama import Fore, Style, Back
import os, time, ticket_to_ride_cards, random

map = [['  ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],
       [' 1','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
       [' 2','.','.','.','.','.','.','.','.','.','.','@','B','B','B','B','&','T','T','.','.','.','.','.','.','.','.'],
       [' 3','.','.','.','.','.','{','.','.','.','.','R','.','.','.','.','.','.','T','.','.','.','.','.','.','.','.'],
       [' 4','.','.','.','.','.','L','.','.','.','.','R','.','.','.','.','.','.','}','H','H','H','H','.','.','.','.'],
       [' 5','.','.','.','.','.','L','.','.','R','R','R','.','P','%','F','F','F','F','.','.','.','H','.','.','.','.'],
       [' 6','.','!','L','L','L','[','.','.','^','.','.','.','P','.','.','.','.','.','.','.','.','$','C','C','C','.'],
       [' 7','.','.','.','.','.','B','.','.','.','.','.','.','P','.','.','.','.','.','.','.','.','.','.','.','C','.'],
       [' 8','.','.','.','.','.','B','.','.','.','.','.','.','P','.','.','.','.','|','L','L','L',':','.','.','C','.'],
       [' 9','.','.','.','.','.','B','.','.','.','.','.','.','#','C','C','C','C','C','.','.','.','P','.','.',']','.'],
       ['10','.','.','.','.','.','B','.','.','.','.','.','.','L','.','.','.','.','.','.','.','.','P','.','.','.','.'],
       ['11','.','.','.','.','.','B','?','P','P','P','(','.','L','.','.','.','.','.','.','>','P','P','.','.','.','.'],
       ['12','.','.','.','.','.','.','H','.','.','.','.','.','L','.','.','.','.','.','.','R','.','.','.','.','.','.'],
       ['13','.','.','.','.','.','.','H','.','.','.','.','.','L','.','.','.','.','.','.','R','.','.','.','.','.','.'],
       ['14','.','.','.','L','L','L','/','F','F','+','F','F','<','T','T','T','T','T','T','*','F','F','F','.','.','.'],
       ['15','.','.','.','L','.','.','.','.','.','P','.','.','R','.','.','.','.','.','.','.','.','.','F','.','.','.'],
       ['16','.','.','.',')','.','.','.','.','.','P','.','.','R','.','.','.','.','.','.','.','.','.','F','.','.','.'],
       ['17','.','.','.','.','.','.','.','.','.','P','.','.','R','R','R','-','.','.','.','.','.','.','F','.','.','.'],
       ['18','.','.','.','.','.','.','.','.','.','P','.','.','.','.','.','.','.','.','.','.','.','.','~','.','.','.'],
       ['19','.','.','.','.','.','.','.','.','.',';','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.'],
       ['20','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.','.']]
       
characters = "abcdefghijklmnopqrstuvwxyz 1 2 3 4 5 6 7 8 91011121314151617181920"
colours = ["blue", "red", "green", "yellow", "black"]
train_cards = ["B","B","B","B","B","B","B","B","B","B","B","B", "P","P","P","P","P","P","P","P","P","P","P","P"]
cards = "BPTRFHCL"
destinations = "@&{%}![^$|#]?(>/+<*)-;~:"
turn = 1
round = 1
generate = True

def clear_screen():

    print("(clearing screen)")
    for i in range(3):
        print(".")
        time.sleep(1)
    os.system("clear")



def create_players():

    players = {}

    for i in range(num_of_players):

        player_name = input(Style.BRIGHT + f"What is player {i + 1}'s name?\n" + Style.RESET_ALL)
        
        players.update({f"{i}": [player_name, colours[i], 45, []]})
        print(players[f"{i}"][3])

        #time.sleep(1)


    return players



def print_scoreboard(players):

    length = 0

    for i in range(num_of_players):
        if len(players[f"{i}"][0]) > length:
            length = len(players[f"{i}"][0])

    spaces = length + 6

    print(Style.BRIGHT + f"""NUMBER    NAME{" " * (spaces - 4)}COLOUR      SCORE""" + Style.RESET_ALL)
    print(f"==============={spaces * "="}")

    for i in range(num_of_players):
        print(f"{i + 1}         {players[f"{i}"][0]}{" " * (spaces - len(players[f"{i}"][0]))}0")
        print(f"---------------{spaces * "-"}")



def print_destination_cards(generate, turn):

    if generate == True:
        card = random.choice(ticket_to_ride_cards.destination_cards)
    

    destination_str = ""

    for line in card:
        for char in line:
            if char in destinations:
                destination_str += char
    
    print(Style.BRIGHT + f"You Must Connect Destination {destination_str[0]} To Destination {destination_str[1]}")
    print(f"This Ticket is Worth {card[-1][-1]} Points")

    for line in card:
        l = ""
        for char in line:
            
            if char == "=":
                l += Style.RESET_ALL + Fore.BLUE + char
            elif char in destinations:
                l += Style.RESET_ALL + Back.RED + char + Style.RESET_ALL
            elif char in characters:
                l += Style.RESET_ALL + Fore.YELLOW + char + Style.RESET_ALL
            else:
                l += Style.RESET_ALL + char

            l += " "

        print(l)
    print("\n")

    return card


def player_turn(players, turn, generate):

    if round == 1:
        generate == True
    else:
        generate = False

    chosen_card = choose_destination_card(generate)
        
    print(players)
        

def choose_destination_card(generate):
    
    for i in range(num_of_players):

        chosen_card = 0

        card_1 = print_destination_cards(generate, turn)
        card_2 = print_destination_cards(generate, turn)
        card_3 = print_destination_cards(generate, turn)


        while chosen_card < 1 or chosen_card > 3:

            chosen_card = int(input(f"{players[f"{i}"][0]}, pick 1 of the 3 destination cards (1, 2, 3)\n"))

            if chosen_card == 1:
                players[f"{i}"][3].append(card_1)
                ticket_to_ride_cards.destination_cards.remove(card_1)
            elif chosen_card == 2:
                players[f"{i}"][3].append(card_2)
                ticket_to_ride_cards.destination_cards.remove(card_2)
            elif chosen_card == 3:
                players[f"{i}"][3].append(card_3)
                ticket_to_ride_cards.destination_cards.remove(card_3)
            else:
                print("Sorry, you can't choose that card")
                chosen_card = int(input(f"{players[f"{i}"][0]}, pick 1 of the 3 destination cards (1, 2, 3)\n"))

    return chosen_card

def print_board():
    for line in map:
        l = ""
        for char in line:
            
            if char in characters or char == "P":
                l += Style.RESET_ALL + Style.BRIGHT + char
            elif char == "B":
                l += Style.RESET_ALL + Fore.MAGENTA + char
            elif char == "T":
                l += Style.RESET_ALL + Fore.BLUE + char
            elif char == "R":
                l += Style.RESET_ALL + Fore.YELLOW + char
            elif char == "F":
                l += Style.RESET_ALL + Fore.CYAN + char
            elif char == "H":
                l += Style.RESET_ALL + Style.DIM + char
            elif char == "C":
                l += Style.RESET_ALL + Fore.RED + char
            elif char == "L":
                l += Style.RESET_ALL + Fore.GREEN + char
            elif char == ".":
                l += Style.RESET_ALL  + char
            else:
                l += Back.RED + char + Style.RESET_ALL
            
            l += "  "
        print(l + Style.RESET_ALL)

print(Style.BRIGHT + """----------------------
    TICKET TO RIDE
----------------------""")
num_of_players = 0
while num_of_players < 2 or num_of_players > 5:
    num_of_players = int(input("How many players are playing (pick a number from 2-4)\n" + Style.RESET_ALL))
players = create_players()
clear_screen()
print_board()
print_scoreboard(players)
player_turn(players, turn, generate)