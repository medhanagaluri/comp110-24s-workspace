"""EX01 - Simple Battleship - A cute step toward Battleship."""
 
__author__ = "730654170"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

boat_location_input = int(input("Pick a secret boat location between 1 and 4: "))
if boat_location_input < 1:
    print("Error! " + str(boat_location_input) + " too low!")
    quit()
elif boat_location_input > 4:
    print("Error! " + str(boat_location_input) + " too high!")
    quit()
boat_location_guess = int(input("Guess a number between 1 and 4: "))
if boat_location_guess < 1:
    print("Error! " + str(boat_location_guess) + " too low!")
    quit()
elif boat_location_guess > 4:
    print("Error! " + str(boat_location_guess) + " too high!")
    quit()
if boat_location_input == boat_location_guess:
    result = RED_BOX
    print("Correct! You hit the ship.")
else:
    result = WHITE_BOX
    print("Incorrect! You missed the ship.")
emoji_string: str = ""
if boat_location_guess == 1:
    emoji_string += result + BLUE_BOX * 3
elif boat_location_guess == 2:
    emoji_string += BLUE_BOX + result + BLUE_BOX * 2
elif boat_location_guess == 3:
    emoji_string += BLUE_BOX * 2 + result + BLUE_BOX
elif boat_location_guess == 4:
    emoji_string += BLUE_BOX * 3 + result
print(emoji_string)
