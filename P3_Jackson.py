"""

Program               P1_Jackson.py
Author(s)             Ernest Jackson
Date Last Updated     October 7, 2023

Problem Statement:
Move the Hero through the Cave, discovering the environment (mapping the Walls) as you go. Avoiding the Pit and Monster while trying to find the Treasure.

Customer Requirements:
The Cave (20x20 squares) is generated randomly (Hero, Walls, Pit, Monster, and Treasure)
The Hero’s Flashlight shines one(1) square in all directions (N, S, E, and W)
The Hero’s Spear can be thrown once in one(1) direction for two(2) squares
Attacking with the Spear will Kill the Monster (if two(2) squares away)
The Monster will Kill the Hero (if one(1) square away)
The Pit will Kill the Hero (if they are both in the same square)
The Hero hears the Wind coming from the Pit (if one(1) square away… can’t tell the direction)
The Hero hears the Snarling from the Monster (if two(2) squares away… can tell the direction)
Finding the Treasure will win the game (if the Hero is in the same square) 


Requiremets Analysis:
  - The Cave will need to represent the cave object woth a complex data structr e (such as a 2 demensional grid each "square" must contain informtion about that "square"
  - The solution will require a user interaction at the beginning of each turn.
  - The results of turn need to be stored/updated in the cave data structure as well as some "overall game data structure"
  
  Algorithm Design / Pseudocode"
  
1.1 Create a 20x20 grid representing the Cave.
1.2 Randomly place walls, pit, monster, and treasure in the Cave grid.
1.3 Randomly place the Hero in the grid (for example, at position (4, 7)).
1.4 Initialize the Cave data structure to store information about each square:
    - Each square has properties: isWall, hasPit, hasMonster, hasTreasure, isHero, isVisited.
    - Initially, set isWall, hasPit, hasMonster, hasTreasure to false for all squares.
    - Set isHero to true for the Hero's initial position.
    - Set isVisited to false for all squares.

2. Initialize Hero's Position, Inventory, and Game State:
2.1 Set Hero's initial position to (4, 7) or any other desired starting point.
2.2 Create a Hero object with properties: position (initial position), inventory (empty), flashlight (enabled), spear (disabled).
2.3 Create game state variables:
    - foundTreasure (boolean) initialized to false.
    - gameOver (boolean) initialized to false.

3. Handle Hero's Options and User Input:
3.1 Display the current state of the Cave, including Hero's position and adjacent squares.
3.2 Display Hero's available options: Move (N, S, E, W), Use Flashlight, Throw Spear (if available).
3.3 Prompt user for input:
    - Allow input for movement direction (N, S, E, W), flashlight (F), or throw spear (T).
    - Get user input (for example, stored in a variable called userInput).

4. Process Hero's Actions Based on User Input:
4.1 If userInput is Move direction:
    - Calculate new position based on input and Hero's current position.
    - Check for collisions with Walls, Pit, Monster, or out-of-bounds.
    - If collision with Pit or Monster, set gameOver = true.
    - If collision with Treasure, set foundTreasure = true and end the game.
    - Update Cave information based on the new position.
4.2 If userInput is Use Flashlight (F):
    - Check if Hero has flashlight in inventory.
    - Illuminate adjacent squares (N, S, E, W) from Hero's position.
    - Update Cave information to reflect illuminated squares.
4.3 If userInput is Throw Spear (T):
    - Check if Hero has a spear in inventory.
    - Prompt user for direction to throw spear (N, S, E, W).
    - Calculate target position based on input and Hero's current position.
    - If Monster is two squares away in the specified direction:
        - Hero kills the Monster.
        - Update Cave information to reflect Monster's demise.
    - If Monster is not in the specified direction, spear misses.
    - Hero loses the spear. 
5. While not gameOver and not foundTreasure:
   a. Display current state of the Cave to the Hero.
   b. Display Hero's options: Move (N, S, E, W), Use Flashlight, Throw Spear (if available).
   c. Prompt user for input.
   d. If input is Move direction:
      - Calculate new position based on input and Hero's current position.
      - Check for collisions with Walls, Pit, Monster, or out-of-bounds.
      - If collision with Pit or Monster, set gameOver = true.
      - If collision with Treasure, set foundTreasure = true and end the game.
      - Update Cave information based on new position.
   e. If input is Use Flashlight:
      - Check if Hero has flashlight in inventory.
      - Illuminate adjacent squares (N, S, E, W) from Hero's position.
      - Update Cave information to reflect illuminated squares.
   f. If input is Throw Spear:
      - Check if Hero has a spear in inventory.
      - Prompt user for direction to throw spear (N, S, E, W).
      - Calculate target position based on input and Hero's current position.
      - If Monster is two squares away in the specified direction:
         - Hero kills the Monster.
         - Update Cave information to reflect Monster's demise.
      - If Monster is not in the specified direction, spear misses.
      - Hero loses the spear.
   
   g. Check martin.edu\dfs\users\ernest.jackson\Desktop"
Old_File_IN = "TheCave.txt"
New_File_OUT = "TheCaveUpdated.txt"

    # Function to get input cave from a file
def getInputCave():
        inputFileName = os.path.join(os.getcwd(), path)  # Construct the full file path
        if not os.path.exists(inputFileName):
            inputFileName = Old_File_IN
        cave = []
        with open(inputFileName, 'r') as inTextFile:
            for line in inTextFile:
                rawRecord = line.split()  # creates list
                cave.append(rawRecord)
        return cave

    # Function to write the updated cave to a file
def writeUpdatedCave(cave):
        outFile = open(New_File_OUT, 'w')
        for row in cave:
            outFile.write(" ".join(row) + "\n")
        outFile.close()

    # Function to add hero to the cave
def addHeroToCave(cave):
    hero_row = random.randint(0, len(cave)-1)  # Generate a random row index
    hero_col = random.randint(0, len(cave[0])-1)  # Generate a random column index
    cave[hero_row][hero_col] = "H"  # Place the hero in the cave
    return cave

    # Main function
def main():
        cave = getInputCave()
        cave = addHeroToCave(cave)
        writeUpdatedCave(cave)
        print("Hero added to the cave and updated cave saved to", New_File_OUT)

if __name__ == "__main__":
        main()
for game over conditions: Hero killed by Monster or Pit.
   h. If Hero finds the Treasure, set foundTreasure = true and end the game.
   i. End turn and repeat.

6. If foundTreasure is true:
   - Display victory message.
   - End the game.
7. If gameOver is true:
   - Display defeat message.
   - End the game.
"""
import os
import random

    # Constants
path = r"\stmartin.edu\dfs\users\ernest.jackson\Desktop"
Old_File_IN = "TheCave.txt"
New_File_OUT = "TheCaveUpdated.txt"

    # Function to get input cave from a file
def getInputCave():
        inputFileName = os.path.join(os.getcwd(), path)  # Construct the full file path
        if not os.path.exists(inputFileName):
            inputFileName = Old_File_IN
        cave = []
        with open(inputFileName, 'r') as inTextFile:
            for line in inTextFile:
                rawRecord = line.split()  # creates list
                cave.append(rawRecord)
        return cave

    # Function to write the updated cave to a file
def writeUpdatedCave(cave):
        outFile = open(New_File_OUT, 'w')
        for row in cave:
            outFile.write(" ".join(row) + "\n")
        outFile.close()

    # Function to add hero to the cave
def addHeroToCave(cave):
    hero_row = random.randint(0, len(cave)-1)  # Generate a random row index
    hero_col = random.randint(0, len(cave[0])-1)  # Generate a random column index
    cave[hero_row][hero_col] = "H"  # Place the hero in the cave
    return cave

    # Main function
def main():
        cave = getInputCave()
        cave = addHeroToCave(cave)
        writeUpdatedCave(cave)
        print("Hero added to the cave and updated cave saved to", New_File_OUT)

if __name__ == "__main__":
        main()

