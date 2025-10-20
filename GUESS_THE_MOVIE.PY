# -*- coding: utf-8 -*-
"""
Created on Tue May 29 17:04:32 2018
@author: malgudi
"""

import random

# list of movies
movies = ['anand', 'drishyam', 'nayakan', 'anbe sivam', 'gol maal', 
           'vikram vedha', 'black friday', 'dangal', 'chak de india', 
           'special 26', 'manichitrathazhu', 'tumbbad', 'swades', 
           'munna bhai mbbs', 'queen']

# Function to create a question by replacing letters with underscores
def create_question(movie):
    n = len(movie)
    question = ""
    for i in range(n):
        if movie[i] == " ":
            question += " "   # keep spaces as they are
        else:
            question += "*"
    return question

# Function to check if a letter is present in the movie name
def is_present(letter, movie):
    return letter in movie

# Function to unlock letters when a correct guess is made
def unlock(modified_qn, movie, letter):
    temp = ""
    n = len(movie)
    for i in range(n):
        if movie[i] == " ":
            temp += " "
        elif movie[i] == letter:
            temp += letter
        else:
            temp += modified_qn[i]
    return temp

# The main game function
def play():
    p1name = input("Player 1, please enter your name: ")
    p2name = input("Player 2, please enter your name: ")
    pp1 = 0
    pp2 = 0
    turn = 0
    willing = True

    while willing:
        if turn % 2 == 0:
            # Player 1's turn
            print(f"\n{p1name}, it's your turn.")
            picked_movie = random.choice(movies)
            qn = create_question(picked_movie)
            modified_qn = qn
            print("Guess the movie:", modified_qn)
            not_said = True

            while not_said:
                letter = input("Enter a letter: ").lower()
                if is_present(letter, picked_movie):
                    modified_qn = unlock(modified_qn, picked_movie, letter)
                    print("Updated:", modified_qn)
                    d = input("Press 1 to guess the movie or 2 to unlock another letter: ")
                    if d == "1":
                        ans = input("Your answer: ").lower()
                        if ans == picked_movie:
                            print("Correct answer! 🎉")
                            pp1 += 1
                            not_said = False
                            print(f"{p1name}, your score is {pp1}")
                        else:
                            print("Wrong answer! ❌")
                            not_said = False
                else:
                    print("Letter not found!")

        else:
            # Player 2's turn
            print(f"\n{p2name}, it's your turn.")
            picked_movie = random.choice(movies)
            qn = create_question(picked_movie)
            modified_qn = qn
            print("Guess the movie:", modified_qn)
            not_said = True

            while not_said:
                letter = input("Enter a letter: ").lower()
                if is_present(letter, picked_movie):
                    modified_qn = unlock(modified_qn, picked_movie, letter)
                    print("Updated:", modified_qn)
                    d = input("Press 1 to guess the movie or 2 to unlock another letter: ")
                    if d == "1":
                        ans = input("Your answer: ").lower()
                        if ans == picked_movie:
                            print("Correct answer! 🎉")
                            pp2 += 1
                            not_said = False
                            print(f"{p2name}, your score is {pp2}")
                        else:
                            print("Wrong answer! ❌")
                            not_said = False
                else:
                    print("Letter not found!")

        turn += 1
        c = input("\nDo you want to continue playing? (yes/no): ").lower()
        if c != 'yes':
            print("\nFinal Scores:")
            print(f"{p1name}: {pp1}")
            print(f"{p2name}: {pp2}")
            print("\nWinner: ", end="")
            if pp1 > pp2:
                print(p1name)
            elif pp2 > pp1:
                print(p2name)
            else:
                print("It's a tie!")
            willing = False


# Start the game
play()
