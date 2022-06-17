"""
Following program is a maze text adventure game.
The user must take the correct path to exit the maze and reaching a dead end will make them lose the game.
Three mazes were designed and they are more complicated than the previous depending on the difficulty.
The user being able to turn back and go all around the maze would be far too complicated to be made in a text
    adventure game, therefore whenever the user tries to go back, they will lose the game.
A timer is used to check how long the player took to solve the maze and will be used as the score.
The score and name of user will be saved in a text file. Of course losing the game means the score is zero.
Players will be asked to play the game, view the leader-board or quit the game when starting.
Player will also be constantly prompted until they enter a correct command when solving the maze
"""

import time


def introduction():
    """ Display a welcome message and an introduction of the game along with the rules """
    print("""Welcome to Lost in the Maze!
    
You were playing a fun hide-and-seek with your friends and looked for a good place to hide.
You fell into a crevice and ended up trapped in an unknown maze.
    
Find your way through the maze by going on the correct path.
You notice 'something' is following behind you and you feel it's unsafe to turn around.
Running to a dead-end will make you lose the game.
    
Use 'Go <direction>' to find your way through the maze. Directions: NORTH, WEST, EAST, SOUTH
Your score is determined by how fast you can escape the maze.
""")


responses = (
    "Path is blocked!",
    "You turned around and got killed by 'something'!",
    "You lost the game!",
    "You ran into a dead end!",
    "Congratulations, you solved the maze!"
)


def start_timer():
    """ Returns the time when starting the game """
    return time.perf_counter()


def stop_timer():
    """ Returns the time when finishing the game """
    return time.perf_counter()


def get_duration(initial_time, final_time):
    """ This is the score. Gets the difference between the times when the game started and when it finished """
    return int(final_time - initial_time)


def direction_to_move():
    """ Keeping prompting the user until they enter a valid input """
    while True:
        go_direction = str(input("> ")).lower()
        if go_direction == "go north" or go_direction == "north":
            return "north"
            break
        elif go_direction == "go west" or go_direction == "west":
            return "west"
            break
        elif go_direction == "go east" or go_direction == "east":
            return "east"
            break
        elif go_direction == "go south" or go_direction == "south":
            return "south"
            break


def player_turned_back():
    """ If user has tried to turn back, they are shown they were killed by something and loses the game """
    print(responses[1])
    print(responses[2])


def reached_dead_end():
    """ If user has reached a dead end, they will be informed of this and loses the game """
    print(responses[3])
    print(responses[2])


def easy_maze_path1():
    print("Moved east by two blocks")
    print("There's a path to the north")
    while True:
        movement2 = direction_to_move()
        if movement2 == "south" or movement2 == "east":
            print(responses[0])
        elif movement2 == "west":
            # Returning False since player has lost, meaning score is 0
            player_turned_back()
            return False
            break
        else:
            print("Moved north by two blocks")
            print("There's a path to the west")
            while True:
                movement3 = direction_to_move()
                if movement3 == "north" or movement3 == "east":
                    print(responses[0])
                elif movement3 == "south":
                    player_turned_back()
                    return False
                    break
                else:
                    print("Moved west by one block")
                    print("There's a path to the south")
                    while True:
                        movement4 = direction_to_move()
                        if movement4 == "north" or movement4 == "west":
                            print(responses[0])
                        elif movement4 == "east":
                            player_turned_back()
                            return False
                            break
                        else:
                            print("Moved south by one block")
                            print("There's a path to the west")
                            while True:
                                movement5 = direction_to_move()
                                if movement5 == "south" or movement5 == "east":
                                    print(responses[0])
                                elif movement5 == "north":
                                    player_turned_back()
                                    return False
                                    break
                                else:
                                    print("Moved west by one block")
                                    print("There's a path to the north")
                                    while True:
                                        movement6 = direction_to_move()
                                        if movement6 == "west" or movement6 == "south":
                                            print(responses[0])
                                        elif movement6 == "east":
                                            player_turned_back()
                                            return False
                                            break
                                        else:
                                            print("Moved north by one block")
                                            print("There's a path to the west")
                                            while True:
                                                movement7 = direction_to_move()
                                                if movement7 == "north" or movement7 == "east":
                                                    print(responses[0])
                                                elif movement7 == "south":
                                                    player_turned_back()
                                                    return False
                                                    break
                                                else:
                                                    print("Moved west by one block")
                                                    print("There's a path to the north")
                                                    while True:
                                                        movement8 = direction_to_move()
                                                        if movement8 == "west" or movement8 == "south":
                                                            print(responses[0])
                                                        elif movement8 == "east":
                                                            player_turned_back()
                                                            return False
                                                            break
                                                        else:
                                                            print("Moved north by one block")
                                                            print("There's a path to the west")
                                                            while True:
                                                                movement9 = direction_to_move()
                                                                if movement9 == "north" or movement9 == "east":
                                                                    print(responses[0])
                                                                elif movement9 == "south":
                                                                    player_turned_back()
                                                                    return False
                                                                    break
                                                                else:
                                                                    print("Moved west by one block")
                                                                    print("There's a path to the north and south")
                                                                    while True:
                                                                        movement10 = direction_to_move()
                                                                        if movement10 == "west":
                                                                            print(responses[0])
                                                                        elif movement10 == "east":
                                                                            player_turned_back()
                                                                            return False
                                                                            break
                                                                        elif movement10 == "south":
                                                                            # returning True/False
                                                                            return easy_maze_path2()
                                                                            break
                                                                        else:
                                                                            return easy_maze_path3()
                                                                            break
                                                                    break
                                                            break
                                                    break
                                            break
                                    break
                            break
                    break
            break


def easy_maze_path2():
    print("Moved south by three blocks")
    print("There's a path to the east")
    while True:
        movement11 = direction_to_move()
        if movement11 == "south" or movement11 == "west":
            print(responses[0])
        elif movement11 == "north":
            player_turned_back()
            return False
            break
        else:
            print("Moved east by one block")
            print("There's a path to the north")
            while True:
                movement12 = direction_to_move()
                if movement12 == "east" or movement12 == "south":
                    print(responses[0])
                elif movement12 == "west":
                    player_turned_back()
                    return False
                    break
                else:
                    # Returning False since player reached a dead end
                    print("Moved north by one block")
                    reached_dead_end()
                    return False
                    break
            break


def easy_maze_path3():
    print("Moved north by one block")
    print("There's a path to the east")
    while True:
        movement11 = direction_to_move()
        if movement11 == "north" or movement11 == "west":
            print(responses[0])
        elif movement11 == "south":
            player_turned_back()
            return False
            break
        else:
            print("Moved east by two blocks")
            print("There's a path to the north and south. You feel fresh air coming from the north path")
            while True:
                movement12 = direction_to_move()
                if movement12 == "east":
                    print(responses[0])
                elif movement12 == "west":
                    player_turned_back()
                    return False
                    break
                elif movement12 == "north":
                    # Returning True since player reached the exit
                    print("Moved north by one block")
                    print(responses[4])
                    return True
                    break
                else:
                    return easy_maze_path4()
                    break
            break


def easy_maze_path4():
    print("Moved south by one block")
    print("There's a path to the east")
    while True:
        movement13 = direction_to_move()
        if movement13 == "west" or movement13 == "south":
            print(responses[0])
        elif movement13 == "north":
            player_turned_back()
            return False
            break
        else:
            print("Moved east by two blocks")
            print("There's a path to the north")
            while True:
                movement14 = direction_to_move()
                if movement14 == "east" or movement14 == "south":
                    print(responses[0])
                elif movement14 == "west":
                    player_turned_back()
                    return False
                    break
                else:
                    print("Moved north by one block")
                    print("There's a path to the west")
                    while True:
                        movement15 = direction_to_move()
                        if movement15 == "north" or movement15 == "east":
                            print(responses[0])
                        elif movement15 == "south":
                            player_turned_back()
                            return False
                            break
                        else:
                            print("Moved west by one block")
                            reached_dead_end()
                            return False
                            break
                    break
            break


def medium_maze_path1():
    print("Moved west by two blocks")
    print("There's a path to north")
    while True:
        movement2 = direction_to_move()
        if movement2 == "west" or movement2 == "south":
            print(responses[0])
        elif movement2 == "east":
            player_turned_back()
            return False
            break
        else:
            print("Moved north by one block")
            print("There's a path to the east")
            while True:
                movement3 = direction_to_move()
                if movement3 == "north" or movement3 == "west":
                    print(responses[0])
                elif movement3 == "south":
                    player_turned_back()
                    return False
                    break
                else:
                    print("Moved east by one block")
                    print("There's a path to the north")
                    while True:
                        movement4 = direction_to_move()
                        if movement4 == "east" or movement4 == "south":
                            print(responses[0])
                        elif movement4 == "west":
                            player_turned_back()
                            return False
                            break
                        else:
                            print("Moved north by one block")
                            print("There's a path to the east")
                            while True:
                                movement5 = direction_to_move()
                                if movement5 == "north" or movement5 == "west":
                                    print(responses[0])
                                elif movement5 == "south":
                                    player_turned_back()
                                    return False
                                    break
                                else:
                                    print("Moved east by one block")
                                    print("There's a path to the north")
                                    while True:
                                        movement6 = direction_to_move()
                                        if movement6 == "east" or movement6 == "south":
                                            print(responses[0])
                                        elif movement6 == "west":
                                            player_turned_back()
                                            return False
                                            break
                                        else:
                                            print("Moved north by one block")
                                            print("There's path to the west and east")
                                            while True:
                                                movement7 = direction_to_move()
                                                if movement7 == "north":
                                                    print(responses[0])
                                                elif movement7 == "south":
                                                    player_turned_back()
                                                    return False
                                                    break
                                                elif movement7 == "east":
                                                    return medium_maze_path2()
                                                    break
                                                else:
                                                    return medium_maze_path3()
                                                    break
                                            break
                                    break
                            break
                    break
            break


def medium_maze_path2():
    print("Moved east by one block")
    print("There's a path to the south")
    while True:
        movement8 = direction_to_move()
        if movement8 == "east" or movement8 == "north":
            print(responses[0])
        elif movement8 == "west":
            player_turned_back()
            return False
            break
        else:
            print("Moved south by two blocks")
            print("There's a path to the west and south")
            while True:
                movement9 = direction_to_move()
                if movement9 == "east":
                    print(responses[0])
                elif movement9 == "north":
                    player_turned_back()
                    return False
                    break
                elif movement9 == "west":
                    print("Moved west by one block")
                    reached_dead_end()
                    return False
                    break
                else:
                    print("Moved south by one block")
                    reached_dead_end()
                    return False
                    break
            break


def medium_maze_path3():
    print("Moved west by one block")
    print("There's a path to the north and west. You feel fresh air coming from the north path")
    while True:
        movement8 = direction_to_move()
        if movement8 == "south":
            print(responses[0])
        elif movement8 == "east":
            player_turned_back()
            return False
            break
        elif movement8 == "north":
            print("Moved north by one block")
            print(responses[4])
            return True
            break
        elif movement8 == "west":
            return medium_maze_path4()
            break


def medium_maze_path4():
    print("Moved west by one block")
    print("There's a path to the south")
    while True:
        movement9 = direction_to_move()
        if movement9 == "north" or movement9 == "west":
            print(responses[0])
        elif movement9 == "east":
            player_turned_back()
            return False
            break
        else:
            print("Moved south by one block")
            reached_dead_end()
            return False
            break


def hard_maze_path1():
    print("Moved east by one block")
    print("There's a path to the north")
    while True:
        movement2 = direction_to_move()
        if movement2 == "east" or movement2 == "south":
            print(responses[0])
        elif movement2 == "west":
            player_turned_back()
            return False
            break
        else:
            print("Moved north by one block")
            print("There's a path to the east")
            while True:
                movement3 = direction_to_move()
                if movement3 == "north" or movement3 == "west":
                    print(responses[0])
                elif movement3 == "south":
                    player_turned_back()
                    return False
                    break
                else:
                    print("Moved east by one block")
                    print("There's a path to the south")
                    while True:
                        movement4 = direction_to_move()
                        if movement4 == "east" or movement4 == "north":
                            print(responses[0])
                        elif movement4 == "west":
                            player_turned_back()
                            return False
                            break
                        else:
                            reached_dead_end()
                            return False
                            break
                    break
            break


def hard_maze_path2():
    print("Moved north by two blocks")
    print("There's a path to the north and east")
    while True:
        movement2 = direction_to_move()
        if movement2 == "west":
            print(responses[0])
        elif movement2 == "south":
            player_turned_back()
            return False
            break
        elif movement2 == "east":
            return hard_maze_path3()
            break
        else:
            return hard_maze_path4()
            break


def hard_maze_path3():
    print("Moved east by two blocks")
    print("There's a path to the north")
    while True:
        movement3 = direction_to_move()
        if movement3 == "east" or movement3 == "south":
            print(responses[0])
        elif movement3 == "west":
            player_turned_back()
            return False
            break
        else:
            print("Moved north by one block")
            print("There's a path to the west")
            while True:
                movement4 = direction_to_move()
                if movement4 == "north" or movement4 == "east":
                    print(responses[0])
                elif movement4 == "south":
                    player_turned_back()
                    return False
                    break
                else:
                    print("Moved west by one block")
                    print("There's a path to the north")
                    while True:
                        movement5 = direction_to_move()
                        if movement5 == "west" or movement5 == "south":
                            print(responses[0])
                        elif movement5 == "east":
                            player_turned_back()
                            return False
                            break
                        else:
                            print("Moved north by two blocks")
                            print("There's a path to the east")
                            while True:
                                movement6 = direction_to_move()
                                if movement6 == "west" or movement6 == "north":
                                    print(responses[0])
                                elif movement6 == "south":
                                    player_turned_back()
                                    return False
                                    break
                                else:
                                    print("Moved east by one block")
                                    print("There's a path to the south")
                                    while True:
                                        movement7 = direction_to_move()
                                        if movement7 == "north" or movement7 == "east":
                                            print(responses[0])
                                        elif movement7 == "west":
                                            player_turned_back()
                                            return False
                                            break
                                        else:
                                            print("Moved south by one block")
                                            reached_dead_end()
                                            return False
                                            break
                                    break
                            break
                    break
            break


def hard_maze_path4():
    print("Moved north by one block")
    print("There's a path to the west")
    while True:
        movement3 = direction_to_move()
        if movement3 == "north" or movement3 == "east":
            print(responses[0])
        elif movement3 == "south":
            player_turned_back()
            return False
            break
        else:
            print("Moved west by one block")
            print("There's a path to north")
            while True:
                movement4 = direction_to_move()
                if movement4 == "south" or movement4 == "west":
                    print(responses[0])
                elif movement4 == "east":
                    player_turned_back()
                    return False
                    break
                else:
                    print("Moved north by one block")
                    print("There's a path to the west and east. You feel fresh air coming from the east path")
                    while True:
                        movement5 = direction_to_move()
                        if movement5 == "north":
                            print(responses[0])
                        elif movement5 == "south":
                            player_turned_back()
                            return False
                            break
                        elif movement5 == "west":
                            return hard_maze_path5()
                            break
                        else:
                            return hard_maze_path6()
                            break
                    break
            break


def hard_maze_path5():
    print("Moved west by two blocks")
    print("There's a path to the north")
    while True:
        movement6 = direction_to_move()
        if movement6 == "west" or movement6 == "south":
            print(responses[0])
        elif movement6 == "east":
            player_turned_back()
            return False
            break
        else:
            print("Moved north by one block")
            print("There's a path to the east")
            while True:
                movement7 = direction_to_move()
                if movement7 == "north" or movement7 == "west":
                    print(responses[0])
                elif movement7 == "south":
                    player_turned_back()
                    return False
                    break
                else:
                    print("Moved east by one block")
                    reached_dead_end()
                    return False
                    break
            break


def hard_maze_path6():
    print("Moved east by one block")
    print("There's a path to the north")
    while True:
        movement6 = direction_to_move()
        if movement6 == "east" or movement6 == "south":
            print(responses[0])
        elif movement6 == "west":
            player_turned_back()
            return False
            break
        else:
            print("Moved north by one block")
            print("There's a path to the west")
            while True:
                movement7 = direction_to_move()
                if movement7 == "north" or movement7 == "east":
                    print(responses[0])
                elif movement7 == "south":
                    player_turned_back()
                    return False
                    break
                else:
                    print("Moved west by one block")
                    print("There's a path to the north")
                    while True:
                        movement8 = direction_to_move()
                        if movement8 == "west" or movement8 == "south":
                            print(responses[0])
                        elif movement8 == "east":
                            player_turned_back()
                            return False
                            break
                        else:
                            print("Moved north by one block")
                            print(responses[4])
                            return True
                            break
                    break
            break


def hard_maze_path7():
    print("Moved west by two blocks")
    print("There's a path to the north")
    while True:
        movement2 = direction_to_move()
        if movement2 == "west" or movement2 == "south":
            print(responses[0])
        elif movement2 == "east":
            player_turned_back()
            return False
            break
        else:
            print("Moved north by one block")
            print("There's a path to the north and east")
            while True:
                movement3 = direction_to_move()
                if movement3 == "west":
                    print(responses[0])
                elif movement3 == "south":
                    player_turned_back()
                    return False
                    break
                elif movement3 == "east":
                    return hard_maze_path8()
                    break
                else:
                    return hard_maze_path9()
                    break
            break


def hard_maze_path8():
    print("Moved east by one block")
    print("There's a path to the north")
    while True:
        movement4 = direction_to_move()
        if movement4 == "east" or movement4 == "south":
            print(responses[0])
        elif movement4 == "west":
            player_turned_back()
            return False
            break
        else:
            print("Moved north by one block")
            reached_dead_end()
            return False
            break


def hard_maze_path9():
    print("Moved north by two blocks")
    print("There's a path to the west")
    while True:
        movement4 = direction_to_move()
        if movement4 == "north" or movement4 == "east":
            print(responses[0])
        elif movement4 == "south":
            player_turned_back()
            return False
            break
        else:
            print("Moved west by one block")
            print("There's a path to the south")
            while True:
                movement5 = direction_to_move()
                if movement5 == "north" or movement5 == "west":
                    print(responses[0])
                elif movement5 == "east":
                    player_turned_back()
                    return False
                    break
                else:
                    print("Moved south by three blocks")
                    reached_dead_end()
                    return False
                    break
            break


def easy_maze_walkthrough():
    """ Paths are split into several other paths:
    Path 1 is split into Path 2(Dead End) and Path 3,
    Path 3 is split into Exit Path and Path 4(Dead End)
    """
    while True:
        print("There's a path to the east")
        movement1 = direction_to_move()
        if movement1 == "east":
            return easy_maze_path1()
            break
        else:
            print(responses[0])


def medium_maze_walkthrough():
    """ Paths are split into several other paths:
    Path 1 is split into Path 2 and Path 3,
    Path 2 is split into two directions both leading to a Dead End,
    Path 3 is split into Exit Path and Path 4(Dead End)
    """
    while True:
        print("There's path to the west")
        movement1 = direction_to_move()
        if movement1 == "west":
            return medium_maze_path1()
            break
        else:
            print(responses[0])


def hard_maze_walkthrough():
    """ Paths are split into several other paths:
    Path is split into Path 1(Dead End), Path 2 and Path 7,
    Path 7 is split into Path 8 and Path 9 both leading to a Dead End,
    Path 2 is split into Path 3(Dead End) and Path 4,
    Path 4 is split into Path 5(Dead End) and Path 6(Exit)
    """
    while True:
        print("There's a path to the north, west and east")
        movement1 = direction_to_move()
        if movement1 == "east":
            return hard_maze_path1()
            break
        elif movement1 == "north":
            return hard_maze_path2()
            break
        elif movement1 == "west":
            return hard_maze_path7()
            break
        else:
            print(responses[0])


def get_score_file():
    """ Opens and returns the scores.txt file. If it's not in directory, creates a new one """
    try:
        # 'r+' is for Read and Writable file
        score_file = open("scores.txt", "r+")
    except FileNotFoundError:
        # Creates new file and opens it as a read\write file
        open("scores.txt", "x")
        score_file = open("scores.txt", "r+")

    return score_file


def username_dictionary():
    """ Storing username and score from the function get_score_file in a dictionary to, prevent duplicated names, and
    returning the dictionary """
    file_lines_dictionary = dict()

    score_file = get_score_file()

    while True:
        file_line = score_file.readline().replace("\n", "")
        if file_line == "":
            break

        file_line_list = file_line.split(",")
        file_lines_dictionary[file_line_list[0]] = file_line_list[1]

    return file_lines_dictionary


def display_leaderboard():
    """ Collecting data from the function username_dictionary to display the score and usernames in a tabular form """
    print("{0} {1:>10}".format("Score", "Username"))
    print("-----------------------------------")

    file_line_dictionary = username_dictionary()
    for username in file_line_dictionary:
        print("{0} {1:>12}".format(file_line_dictionary[username], username))

    print()


def get_user_score(user_name):
    """ Find the player's username in the function username_dictionary and return it. Return 0 if name not in file """
    file_line_dictionary = username_dictionary()
    if user_name in file_line_dictionary:
        return int(file_line_dictionary[user_name])
    else:
        return 0


def save_user_score(user_name, user_score):
    """ Adds/Updates player name with score in the the dictionary
    Clears the scores.txt file completely and stores the new data in the dictionary to the file
    """
    file_line_dictionary = username_dictionary()
    score_file = get_score_file()

    file_line_dictionary[user_name] = user_score

    # Clearing all file content and setting pointer to start of the file to avoid excess spaces being written
    score_file.truncate(0)
    score_file.seek(0)

    for a_name in file_line_dictionary:
        score_file.write("{0},{1}\n".format(a_name, file_line_dictionary[a_name]))


def main():
    """
    1. Gives an introduction of the game
    2. Ask the player if they want to Play, View LeaderBoard or Quit. Keep prompting them until a valid input is entered
    3. Display the LeaderBoard if 'l' is entered, End Program is 'q' is entered, Start the game if 'p' is entered
    4. Ask the player for their username and check their initial score if they already have one, otherwise their
        initial score is 0
    5. Ask the player which difficulty they like to choose and set the maze accordingly
    6. Save the initial time before starting the maze run
    7. If the player has lost the game by dying or running to a dead end, go back to step 2
    8. If the player solved the maze, save the final time and display their score
    9. If they don't have a score saved, ask them if they would like to save it. Keep prompting the player until they
        enter a valid input. Save the score or not according to the user input and go back to step 2.
    10. If they have made a new record(solved the maze faster than their last time), inform them they made a new record
        and ask if they want to save it. Keep prompting until they enter a valid input. Update the score or not
        according to the user input and go back to step 2.

    The algorithm for the maze walk-throughs are as follows:
    - A large chain of nested if statements will be used for the player to proceed through the maze
    - The player will be always be prompted to enter a direction(east, west, north, south) until a valid input is given
    - Moving in the correct direction is the only way to advance through the maze
    - The narrative provides hints to which direction the player must go in
    - If the user attempts to go to a direction where the path is blocked, they will be informed of the warning and
        again prompted to enter an input until they input the correct direction
    - If the user attempts to turn back from the direction which they took, they will be told that they were killed by
        a mysterious entity and has lost the game. (Eg: When the Player tried to move back South after they already
        moved North)
    - Break statements are used to end the progression of the maze after player loses or wins the game
    - If the player reaches a Dead End, they will be informed accordingly and lose the game
    - If they enter the exit of the maze, they will be shown a congratulations message and stops the game
    - Most of the narratives are taken from the global tuple 'responses'
    """

    introduction()

    while True:
        user_option = str(input("Play (p), View leader-board (l) or quit (q): ")).lower()
        if user_option == "l":
            display_leaderboard()

        elif user_option == "q":
            print("Thank you for playing the game! See you later!")
            break

        elif user_option == "p":
            user_name = str(input("Enter username: ")).lower()
            initial_score = get_user_score(user_name)

            # The main part: The Game
            while True:
                difficulty_level = str(input("Choose a difficulty: Easy(e), Medium(m), Hard(h): ")).lower()
                if difficulty_level == "e":
                    initial_time = start_timer()
                    solved_the_maze = easy_maze_walkthrough()
                    break
                elif difficulty_level == "m":
                    initial_time = start_timer()
                    solved_the_maze = medium_maze_walkthrough()
                    break
                elif difficulty_level == "h":
                    initial_time = start_timer()
                    solved_the_maze = hard_maze_walkthrough()
                    break

            """ The score saving is only carried out if the player has solved the maze, not when they lose the game """
            if solved_the_maze:
                final_time = stop_timer()
                score = get_duration(initial_time, final_time)
                print("You're score is", score, "seconds!")

                ''' Since the score is measured by time taken, the new score must be less than the initial score to be
                considered a personal best. If initial score is 0, meaning player's score isn't saved yet, it should
                count as a personal best '''
                if initial_score != 0:
                    if score < initial_score:
                        while True:
                            option_to_save_score = str(input("You made a new record! Save your score? (y/n): "))

                            if option_to_save_score == "y":
                                save_user_score(user_name, score)
                                print("Your score has been saved.")
                                break

                            elif option_to_save_score == "n":
                                break
                else:
                    while True:
                        option_to_save_score = str(input("Save your score? (y/n): "))

                        if option_to_save_score == "y":
                            save_user_score(user_name, score)
                            print("Your score has been saved.")
                            break

                        elif option_to_save_score == "n":
                            break

    get_score_file().close()


if __name__ == "__main__":
    main()
