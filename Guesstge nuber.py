import random
num = random.randint(1,10)
attempts = 0
max_attempts = 7

while attempts < max_attempts:
    guess = int(input("guess:"))
    attempts+=1 
    if guess<num:
        print("very small")
    elif guess>num:
        print("very large")
    elif guess==num:
        print("you are ABSOLUTELY CORRECT...")
else:
    print("out of attempts")
               
