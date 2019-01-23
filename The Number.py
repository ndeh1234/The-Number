                                                     #import random module

import random

                                                      #Implement GuessNumber method

def GuessNumber():

                                                      #Getting input from user

    print(" Guess a number within the range of 5-50. You have five chances to guess it.")

                                                     #Defining the range of numbers that contains the random numbers

    number = random.randint(5, 50)

                                                     #Innitializing countValue to 5

    countValue = 5

                                                      #Display the number of guesses

    print("Chance number", countValue ,end="")

    userGuess = int(input("? "))

                                                      #checking whether randomly generated number is the same as userGuess



    while number != userGuess:

        if (countValue == 10 or userGuess == number):

                                                      #Display warning message to user

           print("Sorry you have exhausted all your chances...the correct number is ", number)

           break;

        if userGuess < number:

            print(userGuess,"is too low")           # Providing feedback to user

            countValue = countValue + 1               #Increment countValue by 1

            print("Chance number", countValue,end="")

            userGuess = int(input("? "))

        elif userGuess > number:

            print(userGuess,"is too high")          # Providing feedback to user
                                                      # print("Chance number", countValue,end="")

            userGuess = int(input("? "))

        else:

            print ("you are right! I was thinking of ", userGuess,"!")

            break


                                                     #call GuessNumber method




GuessNumber()