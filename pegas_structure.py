import os
user_data = os.environ()

rightmoves =  # Load rightmoves from JSON file game_structure.json

dragons_places =  # Load dragons_places from JSON file game_structure.json

backflag =  # Load backflag from JSON file game_structure.json
level_var =  # Load level_var from JSON file game_structure.json

file = open("log", "w")

for i in range(len(rightmoves)):
    if rightmoves[i] == "heart":
        # Create a logging_function(message, save=True) for the below 2 lines and use it in the next lines.
        # print("Congratulations, you find heart. That's help you to free the Pegasus!")
        # print("Congratulations, you find heart. That's help you to free the Pegasus!", file=file, flush=True)
        continue
    if rightmoves[i] == "level":
        level_var += 1
        print("Well done, you rich level " + str(level_var))  # logging_function
        print("Well done, you rich level " + str(level_var), file=file, flush=True)
        continue

    input_var = input("Choose direction (right, up, left, down):")

    if rightmoves[i] == input_var:
        # Create check_right_move(move) function. Function should return the backflag variable value
        # file.write('User direction: {}'.format(input_var + "\n"))
        # print("Good job! One small step for a hero one giant leap for a python knowledge meaning")  #logging_function will be called from check_right_move function
        # print("Good job! One small step for a hero one giant leap for a python knowledge meaning", file=file,
        #       flush=True)

        #  Create set_backward(input_var) function. Function should set/return the backflag variable value
        # if input_var == "right":
        #     backflag = "left"
        # elif input_var == "left":
        #     backflag = "right"
        # elif input_var == "up":
        #     backflag = "down"
        # else:
        #     backflag = "up"
        continue
    elif is_backward_move(input_var):
        #  Create is_backward_move(move) function. Function should return True if the backflag variable value equal to input_var

        # file.write('User direction: {}'.format(input_var + "\n"))
        # print(
        #     "You can't go back to where you were before! Dragons will smell your fear and will find you")  # logging_function
        # print("You can't go back to where you were before! Dragons will smell your fear and will find you", file=file,
        #       flush=True)
        # return backflag == input_var
        break
    elif is_dragons_trap(input_var):
        #  Create is_dragons_trap(move) function. Function should return True if dragons_places[i] == input_var
        # file.write('User direction: {}'.format(input_var + "\n"))
        # print("The hero died. Try to save Pegasus again")  # logging_function
        # print("The hero died. Try to save Pegasus again", file=file, flush=True)
        break
    elif dragons_places[i] == "any":
        # Add this functionality to/from is_dragons_trap(move) function
        file.write('User direction: {}'.format(input_var + "\n"))
        print("The hero died. Try to save Pegasus again")  # logging_function
        print("The hero died. Try to save Pegasus again", file=file, flush=True)
        break
    else:
        #  Create is_wrong_way(move) function
        file.write('User direction: {}'.format(input_var + "\n"))
        print("Wrong-way to go! You lose one or more hearts")  # logging_function
        print("Wrong-way to go! You lose one or more hearts", file=file, flush=True)
        break
else:
    print("Congratulation! You have save the Pegasus") # logging_function
    print("Congratulation! You have save the Pegasus", file=file, flush=True)

file.close()

