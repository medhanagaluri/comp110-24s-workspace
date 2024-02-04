"""EX02 - One shot Battleship"""
__author__: str = "730654170"

#hard-coded the size, secret row, and column
grid_size: int = 4
secret_row: int = 3
secret_column: int = 2

#Input message to guess row
guess_row_input = int(input(f"Guess a row: "))

#initializes the row input loop variable
good_row: bool = False

#game loop for row input
while not good_row:
    #check if row input is less than or equal to grid size
    if guess_row_input <= grid_size:
       #loop variable set to True to exit the loop
       good_row = True
    #if row input is not less than or equal to grid size, try again
    else:
        guess_row_input = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))


#Input message to guess column
guess_column_input = int(input(f"Guess a column: "))

#initializes the column input loop variable
good_column: bool = False

#game loop for column input
while not good_column:
    #check if column input is less than or equal to grid size
    if guess_column_input <= grid_size:
       #loop variable set to True to exit the loop
       good_column = True
    #if column input is not less than or equal to grid size, try again
    else:
        guess_column_input = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))      

#initialize box variables
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

#the result will be a red box if the user is correct and white if wrong
if (guess_row_input == secret_row) and (guess_column_input == secret_column):
    result_box = RED_BOX
else:
    result_box = WHITE_BOX

#initialize row counter
row_counter: int = 1

#prints rows while row counter is less than or equal to grid size
while row_counter <= grid_size:
    #initialize row string
    row_string: str = ""
    #initialize column counter
    column_counter: int = 1
    #check if row counter is the user's guessed row
    if row_counter == guess_row_input:
        #while loop for columns
        while column_counter <= grid_size:
            #check if the column counter is the user's guessed column
            if column_counter == guess_column_input:
                row_string += result_box #concatenate row string to red or white
            else:
                row_string += BLUE_BOX #concatenate row string to blue
            column_counter += 1 #increase column counter by one
    else:
        #while loop for columns
        while column_counter <= grid_size:
            row_string += BLUE_BOX #concatenate row string to blue
            column_counter += 1 #increase column counter by one
    print(row_string) #emoji string is printed
    row_counter += 1 #increase row counter by one

#check if the guesses match the secret row annd column
if (guess_row_input == secret_row) and (guess_column_input == secret_column):
    print(f"Hit!")
#hint message if the user's guess was at the correct row but wrong column
elif (guess_row_input == secret_row) and (guess_column_input != secret_column):
    print(f"Close! Correct row, wrong column.")
#hint message if the user's guess was at the correct column but wrong row
elif (guess_row_input != secret_row) and (guess_column_input == secret_column):
    print(f"Close! Correct column, wrong row.")
else:
    print(f"Miss!")

