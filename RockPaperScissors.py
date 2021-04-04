import random
concent=input("Do you wanna play a game, Rock, Paper Scissor..? (Yes/No)")
concent=concent.lower()
if concent=="yes" or concent=="y":
    score=0
    tie=0
    while True:
        c=['Rock','Paper',"Scissors"]
        comp_guess=random.choice(c)
        print(comp_guess)
        attempt=input("Test your might, (choose between Rock, Paper and Scissors):")
        attempt.lower()
        print(comp_guess)
        #Paper beats rock
        #Rock beats scissors
        #scissors beats paper
        if attempt=="rock":
            if comp_guess=="Rock":
                print("It\'s a tie!")
                tie+=1
                print("Tie: {}".format(tie))
            elif comp_guess=="Paper":
                print("You lose, Paper beats Rock.")
            elif comp_guess=="Scissors":
                print("You win, Rock beats scissors.")
                score+=1
                print("Score {}".format(score))

            else:
                print("Whaty")
        elif attempt=="paper":
            if comp_guess=="Rock":
                print("You Win! paper beats rock.")
                score+=1
                print("Score {}".format(score))
            elif comp_guess=="Paper":
                print("It\'s a Tie.")
                tie+=1
                print("Tie: {}".format(tie))
            elif comp_guess=="Scissors":
                print("You lose! Paper beats Scissors.")
            else:
                print("")
        elif attempt=="scissors":
            if comp_guess=="Rock":
                print("You lose! Rock beats Scissors.")
            elif comp_guess=="Paper":
                print("You win paper beats scissors.")
                score+=1
                print("Score {}".format(score))
            elif comp_guess=="Scissors":
                print("It\'s a Tie.")
                tie+=1
                print("Tie: {}".format(tie))
            else:
                print("")
        else:
            print("Invalid Entry, Please Try again!!!")

elif concent=='no' or concent=='n':
    print("Successfully Exited")
    exit()
else:
    print("Invalid entry!!!")
    exit()