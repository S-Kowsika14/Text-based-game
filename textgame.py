import time

# Define game scenes
def start_game():
    print("Welcome to the Text-Based Adventure Game!")
    time.sleep(1)
    print("You find yourself in a mysterious forest...")
    time.sleep(1)
    scene1()

def scene1():
    print("\nYou encounter a fork in the path. Which way do you go?")
    choice = input("Enter 'left' or 'right': ").lower()
    if choice == "left":
        print("You venture left and find a treasure chest!")
        time.sleep(1)
        print("Congratulations! You win!")
    elif choice == "right":
        print("You stumble upon a bear den and get chased away!")
        time.sleep(1)
        print("You narrowly escape! But beware of bears next time.")
        scene2()
    else:
        print("Invalid choice. Please enter 'left' or 'right'.")
        scene1()

def scene2():
    print("\nYou come across a river. How do you cross it?")
    choice = input("Enter 'swim' or 'build a raft': ").lower()
    if choice == "swim":
        print("You attempt to swim across but get swept away by the current!")
        time.sleep(1)
        print("You wash ashore downstream.")
        scene3()
    elif choice == "build a raft":
        print("You build a sturdy raft and successfully cross the river!")
        time.sleep(1)
        print("Well done! Onward to the next adventure!")
        scene3()
    else:
        print("Invalid choice. Please enter 'swim' or 'build a raft'.")
        scene2()

def scene3():
    print("\nYou reach a clearing and see a cave entrance. Do you enter?")
    choice = input("Enter 'yes' or 'no': ").lower()
    if choice == "yes":
        print("You cautiously enter the cave...")
        time.sleep(2)
        print("Suddenly, the cave collapses!")
        time.sleep(1)
        print("You're trapped!")
        game_over()
    elif choice == "no":
        print("You decide to avoid the cave and continue your journey.")
        time.sleep(1)
        print("Good choice! Onward to the next adventure!")
        # Add more scenes or endings to continue the game
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")
        scene3()

def game_over():
    print("\nGame over! Would you like to play again?")
    choice = input("Enter 'yes' or 'no': ").lower()
    if choice == "yes":
        start_game()
    elif choice == "no":
        print("Thanks for playing!")
        # Add option to save game or exit
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")
        game_over()

# Start the game
start_game()
