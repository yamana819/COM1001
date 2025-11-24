import random 
choosen=random.randint(1,100)

def recursive_random(target,high,low,guesses_left):
    if  guesses_left>0:
        guesses_left-=1
        guess=random.randint(low,high)
        if guess==target:
            print(f"Correct the target was {target}")
        else:
            if guess>target:
                print(f"{guess} was too high current range:[{low},{high}]")
                print(f"Remaining guesses:{guesses_left}")
                high=guess-1
                recursive_random(target,high,low,guesses_left)
            else:
                print(f"{guess} was too low current range:[{low},{high}]")
                print(f"Remaining guesses:{guesses_left}")
                low=guess+1
                recursive_random(target,high,low,guesses_left)
    else:
        print(f"You are out of guesses the target was {target}")
print(f"the target is:{choosen}")
recursive_random(choosen,100,1,7)
            