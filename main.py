import time
import os

# store possible options
yes = ["y", "Y", "yes", "Yes"]
no = ["no", "No", "n", "N"]
a = ["a", "A"]
b = ["b", "B"]
c = ["c", "C"]
d = ["d", "D"]
executive = False
legislative = False
judicial = False
rights = False
first_playthrough = True


# function that takes in an option (one of the lists above), the next branch, and an optional extra message
def branch(choice, option, next_branch, message=""):
    if choice in option:
        os.system("clear")
        print(message)
        next_branch()


# function that runs if the choice does not match any of the options (else statement)
def choice_not_option(current_branch):
    print("\nChoose one of the options")
    current_branch()


# play again function
def play_again():
    print("\nDo you want to play again?")
    choice = input(">>> ")
    if choice in no:
        print("\nGame Over")
        exit()
    branch(choice, yes, intro)
    choice_not_option(play_again)


#actual game
def intro():
    global first_playthrough
    if first_playthrough == True:
        print(
            "There are four doors, one on each side of the room, and standing in front of each door is someone dressed like they came out of a history textbook. Strangely, they are all slightly transparent and you can see the doorknob through them. \nOne of them speaks: \"We need your help to save the Constitution. It has been hidden in a place that you can only access by answering questions. We will do our best to guide you.\""
        )
        time.sleep(4)
        first_playthrough = False
    else:
        print("There are four doors, one on each side of the room.")
    print(
        "Which door do you want to go through?\nA: left door\nB: right door\nC: door in front\nD: door behind"
    )
    choice = input(">>> ")
    print(choice)
    branch(choice, a, executive_branch)
    branch(choice, b, judicial_branch)
    branch(choice, c, legislative_branch)
    branch(choice, d, rights_branch)
    choice_not_option(intro)


#executive branch
def executive_branch():
    global executive
    if executive == True:
        print(
            "It seems you've already completed this area! Maybe try a door you haven't opened yet."
        )
        input("Press enter to continue")
        os.system("clear")
        intro()
    else:
        print(
            "\"I am George Washington,\" the man in front of the door says. \"The first president of the United States. You will be presented with several questions, but do not worry if you do not known the correct response at first.\"\nNow, in order to enter, you must answer:"
        )
        article_two()


def article_two():
    print("What is Article II about?")
    time.sleep(1)
    print("A: Judicial branch\nB: Executive branch\nC: States' rights")
    choice = input(">>> ")
    branch(choice, a, article_two,
           "\"That's not quite the correct branch,\" Washington says.")
    branch(choice, b, stairs, "\"Correct!\" Washington exclaims.")
    branch(choice, c, article_two,
           "\"That's not quite the correct branch,\" Washington says.")
    choice_not_option(article_two)


def stairs():
    print("The door opens and reveals a split staircase.")
    print("Do you go up or down?")
    print("A: Upstairs\nB: Downstairs")
    choice = input(">>> ")
    branch(
        choice, a, voting_system,
        "You go up the stairs to find what looks like a polling station. There is a ballot with a question on it and three choices."
    )
    branch(choice, b, term_limit, "")
    choice_not_option(stairs)


#upstairs
def voting_system():
    print("What is the system the US uses to vote for President?")
    print("A: Electoral college\nB: Gerrymandering\nC: Lottery")
    choice = input(">>> ")
    branch(
        choice, a, voting_age,
        "\"That is correct! Each state gets a certain amount of electors that vote for president in the system known as the electoral college,\" Washington says.\nYou put your filled out ballot in the voting box and continue to the next polling station."
    )
    branch(
        choice, b, voting_system,
        "Washington shakes his head.\"Gerrymandering is when voting districts are manipulated to favor a certain candidate. It is certainly not how we wanted Americans to vote.\""
    )
    branch(
        choice, c, voting_system,
        "\"We do not choose our presidents randomly,\" Washington states. \"We thought that it was very important the president be chosen by the citizens of America.\""
    )
    choice_not_option(voting_system)


def voting_age():
    print("How old do you have to be to vote?")
    print("A: 16\nB: 21\nC: 18\nD: 35")
    choice = input(">>> ")
    branch(choice, a, voting_age,
           "\"That is still a little young,\" Washington says.")
    branch(choice, b, voting_age, "\"Very close!\"")
    branch(
        choice, c, president_law,
        "Washington nods.\"The voting age actually used to be 21, but it was lowered in 1970 to 18.\" You drop the ballot in the slot and notice one final door at the end of the room. When you enter, you see a big desk with a piece of paper on it. It says"
    )
    branch(choice, d, voting_age,
           "\"That would be a little too old,\" says Washington.")
    choice_not_option(voting_age)


#downstairs
def term_limit():
    print("I exist")


def president_law():
    print("i do not want to code this yet")


#judicial branch
def judicial_branch():
    global judicial
    if judicial == True:
        print(
            "It seems you've already completed this area! Maybe try a door you haven't opened yet."
        )
        input("Press enter to continue")
        os.system("clear")
        intro()
    else:
        print("send help please")


#legislative branch
def legislative_branch():
    global legislative
    if legislative == True:
        print(
            "It seems you've already completed this area! Maybe try a door you haven't opened yet."
        )
        input("Press enter to continue")
        os.system("clear")

        intro()
    else:
        print("send help please")


#bill of rights branch
def rights_branch():
    global rights
    if rights == True:
        print(
            "It seems you've already completed this area! Maybe try a door you haven't opened yet."
        )
        input("Press enter to continue")
        os.system("clear")

        intro()
    else:
        print("send help please")


print(
    "Welcome to Saving the Constitution! Type in your answer when presented with the prompt. Answers are not case sensitive. Best of luck!"
)
time.sleep(2)
print(
    "\nYou were really excited for the school trip to Washington DC, but this tour guide is seriously boring. You look around and notice a strange looking tile at the edge of the Reflecting Pool. When you step on it, it opens, revealing a descending a set of stairs. You scramble down before anyone notices, glad to finally be going on an adventure."
)
time.sleep(5)
input("Press enter to continue")
os.system("clear")
print("The stairs end in the center of a rather large room.")
intro()
