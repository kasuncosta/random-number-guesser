#calsswork example 4 , loops

from random import randrange      #this is to be able to use randrange for the random number generator


print("Random number guessing name ")
print("Written by Franklin Araque")

print("\n you get 5 guessese to guess the number between 1 and 100")

#random number selector
randomNumber = randrange(1,100)      #this pick a random number when you run the program

#setting variables

Num=1                #the guessed number . e.g: "Guess #1"
numberOfGuess = 1    #int(Num)


#asking for input
useGuess= int(input("Guess #"+str(Num) +": "))

#print(randomNumber)

#checking input
if useGuess != randomNumber:  
    while Num<=5:
        if useGuess > randomNumber:
            print("Lower")
            #Num = Num+1
            #useGuess= int(input("Guess #"+str(Num)+": "))

        elif useGuess < randomNumber:
            print("Higher")
            #Num = Num+1
            #useGuess= int(input("Guess #"+ str(Num) +": "))


        #if the user guessed the number before reaching 5 tries
        elif useGuess == randomNumber:          
            print("You guessed the Number correctly, good job!")
            replay = input("want to play againy? (y/n): ")      #asking to play again


            #checking if user wnats to play again or not, if yes then asks for input again and resets "Num" number and resets the random number
            if replay.lower() == "y":
              randomNumber = randrange(1,100)                #resetting the random number
              Num = numberOfGuess                            #setting "Num" back to 1, since numberOfGuess is 1
              useGuess= int(input("Guess #"+str(Num) +": "))
              #print(randomNumber)

              #checking again the new value of the input number anc comparing it to the random number
              if useGuess > randomNumber:
                print("Lower")
           
              elif useGuess < randomNumber:
                print("Higher")
           
                 

            #if user types "n", program ends
            if replay.lower() == "n":
                print ("Thanks for playing!")
                break


            #user did not guess the number after 5 tries
        if Num ==5:                                                                               #stops asking once the number of guesses reaches 5 and promps next message
           print("You did not guess the number, the number was " + str(randomNumber))             #number was not guessed message

           Num = Num+1                                                                            #adding one more to "Num" in order to stop the loop so it doersnt go in an infinite loop 
                                                                                                  #since it will make "Num" be 6, thus higher than 5 making the loop end when it checks that is not equal to 5

      #here it checks the user input after each try, and then promps the user for input again
#*********************************************************************************************#
            #checking the user input, adding one more to "Num" and asking for input again if the number of questions is less than 5
        elif Num<5:                                                                               #check for number of guesses and to stop at guess #5
            Num = Num+1                                                                           #adding one more to "Num" after each time the user is asked for a anumber
            useGuess= int(input("Guess #"+str(Num) +": "))                                        #checking the user input and asking again for input
                   
 #*********************************************************************************************#           



        #if user input matches random number, then asks if they want to play again
        #elif useGuess == randomNumber:
            # print("You guessed the Number correctly, good job!")
             #replay = intput("want to play againy? (y/n): ")
             #if replay.lower() == "y":
               #Num = numberOfGuess
                #useGuess= int(input("Guess #"+str(Num) +": "))
             #elif replay.lower() == "n":
                 #print ("Thanks for playing!")
                 #break
       
 
#nice work Franky !!!
