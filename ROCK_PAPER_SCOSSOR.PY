def rock_paper_scissor(num1, num2, bit1, bit2):
    if num1[bit1] == num2[bit2]:
        print("Tie!")
    elif (num1[bit1] == "Rock" and num2[bit2] == "Scissor") or \
         (num1[bit1] == "Scissor" and num2[bit2] == "Paper") or \
         (num1[bit1] == "Paper" and num2[bit2] == "Rock"):
        print("Player One Wins!")
    else:
        print("Player Two Wins!")


player_one = ["Rock", "Paper", "Scissor"]
player_two = ["Rock", "Paper", "Scissor"]

while True:
    print("Choices:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissor")

    num1 = int(input("Player One, enter your choice (1/2/3): "))
    num2 = int(input("Player Two, enter your choice (1/2/3): "))

    bit1 = int(input("Enter the secret bit position for player one: "))
    bit2 = int(input("Enter the secret bit position for player two: "))

    rock_paper_scissor(player_one, player_two, bit1 - 1, bit2 - 1)

    ch = input("Do you want to continue? (y/n): ")
    if ch.lower() != 'y':
        break