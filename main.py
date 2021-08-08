import time
import random
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
  print("There are four doors, one on each side of the room, and standing in front of each door is someone dressed like they came out of a history textbook. Strangely, they are all slightly transparent and you can see the doorknob through them.\nWhich door do you want to go through first?")
  time.sleep(2)
  print("A: left door\nB: right door\nC: door in front\nD: door behind")
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
    print("It seems you've already completed this area! Maybe try a door you haven't opened yet.")
    input("Press enter to continue")
    os.system("clear")
    intro()
  else:
    print("you're a cool person")
    executive = True
    intro()

#judicial branch
def judicial_branch():
  global judicial
  if judicial == True:
    print("It seems you've already completed this area! Maybe try a door you haven't opened yet.")
    input("Press enter to continue")
    os.system("clear")
    intro()
  else:
    print("send help please")

#legislative branch
def legislative_branch():
  global legislative
  if legislative == True:
    print("It seems you've already completed this area! Maybe try a door you haven't opened yet.")
    input("Press enter to continue")
    os.system("clear")

    intro()
  else:
    print("send help please")


#bill of rights branch
def rights_branch():
  global rights
  if rights == True:
    print("It seems you've already completed this area! Maybe try a door you haven't opened yet.")
    input("Press enter to continue")
    os.system("clear")

    intro()
  else:
    print("send help please")



print("Welcome to Saving the Constitution! Type in your answer when presented with the prompt. Answers are not case sensitive. Best of luck!")
time.sleep(2)
print("You were really excited for the school trip to Washington DC, but this tour guide is seriously boring. You look around and notice a strange looking tile at the edge of the Reflecting Pool. When you step on it, it opens, revealing a descending a set of stairs. No one around you has noticed yet and you scramble down the stairs, glad to finally be going on an adventure.")
time.sleep(5)
input("Press enter to continue")
os.system("clear")
print("The stairs end in the center of a rather large room.")
intro()