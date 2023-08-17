import random
i = 0

if __name__ == "__main__":
    n = random.randint(1,500)
    while(i<=10):
        ch = int(input("Enter your guess : "))
        if(i>9):
            print("Maximum guess Riched :( ")
            break
        
        if(ch==n):
            print("Congrats !! You Guess the number Right :) ")
            break
        elif(ch<n):
            print(f"Your Guess is too low Try Again \nYou have {8-i} attempts left")
        elif(ch>n):
            print(f"Your Guess is too High Try Again \nYou have {8-i} attempts left")
        
        i=i+1

