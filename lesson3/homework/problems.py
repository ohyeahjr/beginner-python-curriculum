# Problem 1
# Ask user for two test scores.
# If BOTH scores are at least 50, print "You passed both!"
# Otherwise, print "You failed at least one."
score1 = int(input("enter first score: "))
score2 = int(input("enter second score:"))
if score1 >=50 and score2 >=50:
    print("you passed both!")
else:
    print("you failed at least one.")
# Problem 2
# Ask user if they brought lunch and water (yes/no).
# If they brought lunch OR water, print "You're somewhat ready."
# If they brought both, print "You're fully ready!"
# If they brought neither, print "You're not ready."
lunch: input("did you bring lunch? (yes/no):")
water: input("did you bring water? (yes/no):")
if lunch == "yes" and water == "yes":
    print("you're fully ready!")
elif lunch == "no" and water == "no":
    print("you're not ready.")
else:
    print("you're somewhat ready.")
# Problem 3
# Ask user to enter a number.
# If the number is NOT between 1 and 10 (inclusive), print "Out of range."
# Otherwise, print "In range."
num = int(input("enter a number: "))
if not (num >= 1 and num <= 10):
    print("out of range")
else:
    print("in range")
# Problem 4
# Ask the user for a test score (0-100).
# Print the grade based on score:
#   90 and above: "A"
#   80 to 89: "B"
#   70 to 79: "C"
#   60 to 69: "D"
#   below 60: "F"
score = int(input("enter a score 1-100:"))
if score >=90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
# Problem 5
# Ask the user for two numbers.
# If one is divisible by 5 AND the other is NOT divisible by 2, print "Interesting pair!"
# Otherwise, print "Plain pair."
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
if num1 % 5 == 0 and num2 % 2 != 0:
    print("interesting pair!")
else:
    print("plain pair.")