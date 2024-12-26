import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
p2 = random.randint(0,2)
p1 = int(input("Enter 0 for rock, 1 for paper and 2 for scissors:"))
print("You choose:\n")
if p1 == 0:
    print(rock)
if p1 == 1:
    print(paper)
if p1 == 2:
    print(scissors)

print("\nComputer choose:\n")
if p2 == 0:
    print(rock)
if p2 == 1:
    print(paper)
if p2 == 2:
    print(scissors)

if p1 == p2:
    print("It was a draw")
elif (p1 == 0 and p2== 1) or (p1 == 1 and p2 == 2) or (p1 == 2 and p2 == 0):
    print("You win")
else:
    print("You loose")


