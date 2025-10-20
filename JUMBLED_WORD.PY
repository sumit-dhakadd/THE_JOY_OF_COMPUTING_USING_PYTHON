def choose():
    import random
    words = ['python', 'java', 'kotlin', 'javascript', 'ruby', 'swift', 'html', 'css', 'react', 'angular']
    pick = random.choice(words)
    return pick

def jumble(word):
    import random
    jumbled = ''.join(random.sample(word, len(word)))
    return jumbled

def thanks(P1name, P2name, pp1, pp2):
    print("Thanks for playing!")
    print(f"{P1name}, your final score is {pp1}.")
    print(f"{P2name}, your final score is {pp2}.")
    if(pp1 > pp2):
        print(f"{P1name} wins!")
    elif(pp2 > pp1):
        print(f"{P2name} wins!")
    else:
        print("It's a tie!")
    print("Come Again!, Good Bye!")


def Play():
    P1name = input("Player 1, please enter your name: ")
    P2name = input("Player 2, please enter your name: ")
    print(f"Welcome {P1name} and {P2name} to the Jumbled Word Game!")
    pp1 = 0
    pp2 = 0
    turn = 0
    c = 1
    while(c == 1):
        picked_word = choose()
        qn = jumble(picked_word)
        print("The jumbled word is:", qn)
        if (turn%2 == 0):
            print(f"{P1name}, it is your turn.")
            ans = input("Please enter your answer: ")
            if(ans == picked_word):
                print(f"{P1name}, you are correct!")
                pp1 += 1
                print(f"{P1name}, your score is {pp1}.")    
            else:
                print(f"Sorry {P1name}, the correct answer is {picked_word}.")
            c = int(input("Press 1 to continue and 0 to quit: "))
            if(c == 0):
                thanks(P1name, P2name, pp1, pp2)
                break
            
        if(turn%2 != 0):
            print(f"{P2name}, it is your turn.")
            ans = input("Please enter your answer: ")
            if(ans == picked_word):
                print(f"{P2name}, you are correct!")
                pp2 += 1
                print(f"{P2name}, your score is {pp2}.")    
            else:
                print(f"Sorry {P2name}, the correct answer is {picked_word}.")
            c = int(input("Press 1 to continue and 0 to quit: "))
            if(c == 0):
                thanks(P1name, P2name, pp1, pp2)
                break
        turn += 1
Play()