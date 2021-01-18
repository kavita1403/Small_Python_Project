print("Total no of atmost guesses u have:9")
n=18
for i in range(1,10):
    n1=int(input("enter the no. that you have quessed:"))
    if n1>n:
        print("sorry! you have guessed the larger no.")
        print("No. of guesses left",9-i)
        if 9-i==0:
            print("Game Over")
    elif n1<n:
        print("sorry! you have guessed the smaller no.")
        print("No. of guesses left",9-i)
        if 9-i==0:
            print("Game Over")
    elif n1==n:
        print("congratulations! you won.")
        print("No. of guesses you took to finish",i) 
        break
   


