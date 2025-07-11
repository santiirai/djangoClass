#research gold
#three way, straight->khola parkhine->dead, 
# tairine-> three trees -> first= end, second= win, third = khanirakhyo
# , left or right -> dead/end
# wait = input(print("I want to wait."))
# cross = input(print("I want to cross the river."))
# leftOrright = input(print("I want to go left or right of the river."))
wait = "w"
cross = "c"
leftOrright = "L"
decision = input("Command: There are three ways to pass the first step,\n Do you want to wait, go to left/right, wait or cross the river")

if(decision == "c"):
     (print("Now, there are three trees before you."))
     dig = input(print("Will you dig in the first tree, second tree or a third tree??"))
     if(dig == "first"):
          print("You're dead.")
     elif(dig == "third"):
          print("----")
     else:
          print("Congratulations, You found the gold.")    
else:
     print("Command: You lost.")

