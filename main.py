import random
random.seed(random.randint(258,845791))
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

#Write your code below this line 👇
cmp =0
runn=0
user_points=0
while(runn!=5):
  user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
  if(user_choice==0):
    print(rock)
  elif(user_choice==1):
    print(paper)
  else:
    print(scissors)

  print("Computer chose:")
  comp_choice=random.randint(0,2)
  if(comp_choice==0):
    print(rock)
  elif(comp_choice==1):
    print(paper)
  else:
    print(scissors)
  if(user_choice==0 and comp_choice==1):
    cmp+=1
  elif(user_choice==0 and comp_choice==2):
    user_points+=1
  elif(user_choice==0 and comp_choice==0):
    print("Draw")
  elif(user_choice==1 and comp_choice==0):
    user_points+=1
  elif(user_choice==1 and comp_choice==1):
    print("Draw")
  elif(user_choice==1 and comp_choice==2):
    cmp+=1
  elif(user_choice==2 and comp_choice==0):
    cmp+=1
  elif(user_choice==2 and comp_choice==1):
    user_points+=1
  elif(user_choice==2 and comp_choice==2):
    print("Draw")
  runn+=1
if(cmp>user_points):
  print(f"computer got {cmp} you lose")
else:
  print(f"user got {user_points} you win")