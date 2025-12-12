import random

def roll_dice():

    player_roll = random.randint(1, 6)
    computer_roll = random.randint(1, 6)
    rolls = {"player": player_roll, "computer": computer_roll}
    return rolls

def check_winner(player, computer):
    print(f"You rolled {player}, computer rolled {computer}")
    if player > computer:
        return "You win!"
    elif player < computer:
        return "You lose!"
    else:
        return "It's a tie!"


rolls = roll_dice()
result = check_winner(rolls["player"], rolls["computer"])
print(result)