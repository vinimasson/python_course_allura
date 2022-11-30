import hangman 
import guessing 

print("********************************")
print("*******Choose your Game!********")
print("********************************")

print("(1) Hangman (2) Guessing")
game = int(input("Wich game you want play?"))

if(game == 1):
    hangman.play_hangman()
elif(game == 2):
    guessing.play_guessing()

    




