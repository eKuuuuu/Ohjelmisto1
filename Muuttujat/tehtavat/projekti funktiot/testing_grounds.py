# Initialize score dictionary for four players
scores = {
    "Player 1": 0,
    "Player 2": 0,
    "Player 3": 0,
    "Player 4": 0
}

# Function to update the score for a player
def update_score(player, points):
    if player in scores:
        scores[player] += points
        print(f"{player}'s score is now {scores[player]}")
    else:
        print(f"{player} not found!")

# Function to display the current scores
def display_scores():
    print("Current Scores:")
    for player, score in scores.items():
        print(f"{player}: {score}")

p1_new = int(input("New score for player 1: "))
p2_new = int(input("New score for player 2: "))
p3_new = int(input("New score for player 3: "))
p4_new = int(input("New score for player 4: "))


# Example of updating the score
update_score("Player 1", p1_new)
update_score("Player 2", p2_new)
update_score("Player 3", p3_new)
update_score("Player 4", p4_new)

# Display current scores
display_scores()
