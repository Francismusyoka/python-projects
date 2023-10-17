# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import random
# Initialize game variables
player1_score = 0
player2_lives = 3
game_count = 0

# Word and explanation data for level one
level_one_data = {
    "cat": "A house pet that is liked by many",
    "dog": "A domesticated animal that barks",
    "sun": "The star at the center of our solar system",
    "bat": "A mammal that flies"

}

# Function to ask a question
def ask_question():
    word, explanation = random.choice(list(level_one_data.items()))
    print(f"Player 1: {word} Explanation: {explanation}")
    guess = input("Player 2, what's your guess? ").strip().lower()
    return guess == word

# Main game loop
while game_count < 5:
    if player2_lives == 0:
        game_count += 1
        player2_lives = 3
        print(f"Out of lives! Starting game {game_count + 1}")

    if ask_question():
        player1_score += 1
        if player1_score == 3:
            print("Player 2 advances to the next level!")
            break
    else:
        player2_lives -= 1
        print(f"Wrong guess! Lives left: {player2_lives}")

# Game result
if player1_score == 3:
    print("Player 2 wins and advances to the next level!")
else:
    print("Player 1 wins the game. Congratulations!")