import random #importing random fuction to allow for one of the greetings or responses to be chosen

greetings = ['Hey', 'hello', 'hi', 'Hi', 'Hello', 'hey' ]

responses = ['Alright', 'good', 'alright', 'sweet', 'Sweet' ]

question = ['How are you?', 'How are you doing?' ]

#used lists to be able to store information on responses that the bot should use but also accept

userInput = raw_input("Welcome to the chatbot... ") #user input, this should be changed when intergating with other code

if userInput in greetings:
    print (random.choice(greetings))  #This is giving the user a random greeting as an output
    
elif userInput in question:
    print (random.choice(responses))  #This is giving the user a random response as an output
    
else:
    print("I did not understand what you said")  
#This is used as a backup incase the user does not enter something in the lists and acts as an error message
