import random

def guess_the_num_game() :

    num = random.randint(1, 20)

    print("Can you guess the number I am thinking? Its less than 20 ")
    print("4 chance only for you")

    guess = int(input("ENTER THE NUMBER :"))
    count = 0

    while num != guess :

        if count >= 2:
            print("you lose")
            break

        if guess > num:
            print("Your guess in higher")
        else:
            print("Your guess is lower")

        guess = int(input("Guess again: "))
        count += 1
    else:
        print("You won!")
    print("the number is ",num)

guess_the_num_game()