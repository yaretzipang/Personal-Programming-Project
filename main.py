## Personal Programming Project - Yaretzi Pang
import os, time


def clear_screen():
    for i in range(3):
        print(".")
        time.sleep(3)
    print("clear screen")
    os.system("clear")


print("""--------------
     UNO
--------------""")
num_of_players = int(input("How many players are playing (pick a number from 2-4)\n"))
clear_screen()