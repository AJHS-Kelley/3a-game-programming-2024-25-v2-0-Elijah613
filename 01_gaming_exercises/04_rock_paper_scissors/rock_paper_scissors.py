# Rock, Paper, Scissors by Elijah Reed, v0.3

# MODULE IMPORTS
import random

# DATA STRUCTURES -- PLAYER
playerName = "Test Player"
playerChoice = None
playerScore =  0

# DATA STRUCTURES -- CPU
cpuScore = 0
cpuChoice = None

# PLAYER NAME INPUT
playerName = input("Please enter your name and press the ENTER key.\n")
print(f"Your name is {playerName}")
isCorrect = input("Is that correct? Type yes or no then press the ENTER key.\n").lower()

# .lower() can turn ALL input into lowercase
# .upper() can turn ALL input into uppercase

if isCorrect == "yes":
    print(f"Now {playerName}, let's play Rock, Paper, Scissors!\n")
else:
    playerName = input("Type your name correctly this time.\n")

# THE RULES using MUTLI-LINE STRINGS
print(f"""
Welcome {playerName} to the Rock, Paper, Scissors Robot!
We're going to play Rock, Paper, Scissors!

Here's how it works: Your opponent is the CPU. First to 5 wins gets the victory.
You will choose from Rock, Paper, or Scissors.
The CPU will also choose at random.
      
- ROCK BEATS SCISSORS
- SCISSORS BEATS PAPER
- PAPER BEATS ROCK

""")

# MULTI-LINE STRINGS CAN BE USED AS BIG COMMENTS
"""
According to my calculations,
Everything in between these quotes will be ignored.
I'm such a genius
"""
