import random
name = input("Enter your name: ")
items = ["Clock", "Jelly", "Wheat", "Flute", "Peach", "Arrow", "Brick", "Chalk", "Sword", "Torch",
         "Crown", "Spoon", "Beads", "Bills", "Dryer", "Badge", "Glass", "Boots", "Fence", "Brush",
         "Kites", "Pouch", "Pizza", "Floss", "Cable", "Scarf", "Skate", "Stamp", "Plate", "Train",
         "Bulbs", "Lever", "Linen", "Pills", "Booth", "Whisk", "Board", "Sheep", "Stars", "Quill",
         "Snake", "Crust", "Troll", "Docks", "Paint", "Crate", "Glove", "Fruit", "Shirt", "Table"]

chosen_index = random.randint(0, len(items) - 1)
chosen_one = items[chosen_index].capitalize()
print("★°　.　*.　　°☆°　.　*.　　°★°　.　*.　　°☆°　.　*.　　°★")
print(f"Hello, {name}! Welcome to the game of Guess the Word.")
print("You have 6 attempts to guess the word.")
print("★°　.　*.　　°☆°　.　*.　　°★°　.　*.　　°☆°　.　*.　　°★")


def get_feedback(chosen_one, guess):
    feedback = ""
    correct_chars = []
    used_indices = []
    count_correct = {}
    for char in chosen_one.lower():
        count_correct[char] = count_correct.get(char, 0) + 1  
    for i in range(len(chosen_one)):
        if chosen_one[i].lower() == guess[i].lower():
            feedback += chosen_one[i]
            used_indices.append(i)
            count_correct[chosen_one[i].lower()] -= 1
        else:
            feedback += "-"
    for i in range(len(guess)):
        if guess[i].lower() in count_correct and count_correct[guess[i].lower()] > 0 and i not in used_indices:
            correct_chars.append(guess[i])
            count_correct[guess[i].lower()] -= 1
    return feedback, correct_chars


def guess_word():
    attempts = 6
    while attempts > 0:
        guess = input("Enter your guess: ").strip()
        while len(guess) != 5:
            print("Please enter a 5-letter word.")
            guess = input("Enter your guess: ").strip()
        feedback, correct_chars = get_feedback(chosen_one, guess)
        print(f"Feedback: {feedback}")
        if correct_chars:
            print(f"Other characters present: {' '.join(correct_chars)}")
        else:
            print("No other characters present.")
        if feedback == chosen_one:
            print("☆　　.✵　*　.　　　★　　.　　　☆　　.✵　*　.　　　★")
            print("Congratulations!!! You've guessed the word correctly!")
            print("☆　　.✵　*　.　　　★　　.　　　☆　　.✵　*　.　　　★")
            return
        attempts -= 1
        print(f"Attempts remaining: {attempts}")
    print("------------------------------------------------------------")
    print(f"Sorry, you've used all attempts. The word was: {chosen_one}")
    print("------------------------------------------------------------")
guess_word()
