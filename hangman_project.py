import random
word = ["apple","banana","mahindra"]
p1_word=random.choice(word)
p1_list = list(p1_word)
x = len(p1_list)
print("Welcome to Hangman Game !")
print(f"You need to guess {x} letters ")
attempts = len(p1_list)
p2_word = str(input(f"Enter the letter you are guessing only you have {attempts} attempts :"))
letter = 1  
p2_list = "" 
while letter<len(p1_list):
    
    if p2_word in p1_list:
       p2_list+=p2_word
       print("You Guessed a correct letter ")
       p2_word = str(input(f"Enter the letter you are guessing :"))
       letter+=1  
        
    elif p2_word not in p1_list:
       print("OOPS! , You guessed wrong letter ") 
       attempts-=1
       p2_word = str(input(f"Enter the letter you are guessing only you have {attempts} attempts :"))
       letter+=1
       
if p2_list == p1_word:
    print("Player 2 won the game")
    
else:
    print("Player 1 won the game") 
    
print("Thanks , For playing the game")           