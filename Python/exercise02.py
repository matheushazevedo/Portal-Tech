name = str(input("Enter your name: ")).title()
firstNote = float(input(f"{name}, enter your first note: "))
secondNote = float(input(f"Now, enter your second note: "))
faults = int(input(f"{name}, how many faults did you have? "))

average = float(firstNote + secondNote)/2

if (average < 7) or (faults > 3):
    print(f"{name}, unfortunately you didn't pass. His average was {average:.2f} points.")
elif (average >= 7):
    print(f"{name}, congratulations! You passed with an average of {average:.2f} points.")
else: print("An error has occurred, please try again.")