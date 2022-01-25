# Author: CRS 01/24/22
# Define function rps
def rps(p1, p2):
# Create list to say what beats what
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
# Create if statement to decide who wins
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"
# Test the code
print(rps("scissors", "paper"))
