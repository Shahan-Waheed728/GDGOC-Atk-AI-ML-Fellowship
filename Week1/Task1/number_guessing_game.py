# python program to guess the correct number
import random
computer = random.randint(1,100)
user = 0
count = 0
print("Guess number between 1 & 100")
while(user!=computer and count < 10):
  count +=1
  user = int(input("Guess number: "))  
  difference = user - computer
  if(difference == 0):
     print(f"Correct! You guessed after {count} attempt.")
     break
  elif(difference <= -10):
    print("Very low")
  elif(difference < 0 ):
        print("Little Low")
  elif(difference <= 10):
     print("Little High")  
  else:
     print("Very High")
if user != computer:
  print(f"Correct number was {computer}")