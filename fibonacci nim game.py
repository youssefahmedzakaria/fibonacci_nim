print(
    "- This program is a fibonacci nim Start with coins that the user wants\n- the players must input number of coins less than or equal the last player move\n- The one who takes the last coin loses")
print("\nGAME RULES: ")
print(
    "- you'll enter the number of coins you want to start with. \n- the first player will enter number of coins he wants to remove \n- then the next move must be less than or equal the double of the previous one till the game ends \n- the player takes last coin wins ")
# "Author : youssef zakaria"
# "Version: 2.0"
print(
    "\n-------------------------------------------------- Game Starts Now --------------------------------------------------\n")
# ------------------------------------------------------------------------------------

# initializing variables
take_turns = 0
previous = 0

# taking the number of coins to start the game with
number_of_coins = input("please enter number of coins: ")
while not number_of_coins.isdigit(): #checking number is digit or not
    number_of_coins = input("please enter a POSITIVE INTEGER!")
n_coins = int(number_of_coins)
while n_coins <= 1:
    number_of_coins = input("please enter a number more than 1: ")
    while not number_of_coins.isdigit():
        number_of_coins = input("please enter a NUMBER! ")
    n_coins = int(number_of_coins)


def play_fibonacci_nim(n_coins, take_turns):
    while n_coins != 0:
        print("Remaining coins = ", n_coins)
        if take_turns % 2 == 0:
            player_1_move = input("Player 1 Please enter coins: ")
            while not player_1_move.isdigit():
                player_1_move = input("Player 1 Please enter POSITIVE INTEGER!: ")

            move1 = int(player_1_move)

            # checking if valid or not
            while ((move1 == n_coins and take_turns == 0) or move1 < 1 or move1 > n_coins or (
                    take_turns > 0 and move1 > previous * 2)):
                player_1_move = input("please enter a valid number : ")
                while not player_1_move.isdigit():
                    player_1_move = input("play again. ENTER A NUMBER! ")
                move1 = int(player_1_move)

            # assigning value of previous to move 2 to compare it with next move of player 1
            previous = move1
            winner = True
            n_coins -= move1

        else:
            # taking the move number from the second player
            player_2_move = input("Player 2 Please enter coins: ")
            while not player_2_move.isdigit():
                player_2_move = input("Player 2 Please enter POSITIVE INTEGER!: ")

            move2 = int(player_2_move)

            # checking if valid or not
            while (move2 < 1 or move2 > n_coins or move2 > previous * 2):
                player_2_move = input("please enter a valid number : ")
                while not player_2_move.isdigit():
                    player_2_move = input("play again. ENTER A NUMBER! ")
                move2 = int(player_2_move)


            # assigning value of previous to move 2 to compare it with next move of player 1
            previous = move2
            winner = False
            n_coins -= move2
        take_turns = take_turns + 1

    if winner == True:
        print("\nPlayer 1 Won ! ")
    else:
        print("\nPlayer 2 Won ! ")


play_fibonacci_nim(n_coins, take_turns)

print("CONGRATULATIONS!")