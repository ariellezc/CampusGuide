"""Gives distance and duration from origin and destination"""

#import library to access webpages
import urllib.request
import json
from key import key2, app_key #import key2, app_key

#userinput and converting it to lower case
userinput = input(""">""")
userinput.lower()

#function for removing irrelevant sentence from user input
def removesentenceTravel(userinput):
    listWords = userinput.split() #split userinput
    try: 
        listIndexWord = str([i for i in range(len(listWords)) if listWords[i] == 'to']) #finds the index of word containing "to"
        cStrT = str(listIndexWord).strip('[]') #removes square bracket
        cIntT = int(cStrT) #converts to int

        listIndexTravel = str([i for i in range(len(listWords)) if listWords[i] == '@travel']) #finds the index of word containing "@travel
        cStrKey = str(listIndexTravel).strip('[]') #removes square bracket
        cIntKey = int(cStrKey) #converts to int
        #slice operator
        originL = listWords[cIntKey+1:cIntT] #starts from the index where @travel (add 1 so it doesn't start with it) until the index where "to" is (what separates the origin and destination) 
        destinationL = listWords[cIntT+1:len(listWords)] #starts from the index where "to" (add 1 so it doesn't start with it) until the length of listWords (destination) 
       #replaces "," to "+" so it can be use in the url
        origin = ",".join(originL).replace(",","+")
        destination = ",".join(destinationL).replace(",","+")
        print(distanceMatrix(origin, destination))
    except:
        print("I think you got it wrong! To know the distance and duration just use @travel for example '@travel London to Coventry'") #output this if there's an error

#function for distance matrix (takes in 2 inputs)
def distanceMatrix(origin, destination): 
    #retrieve data from a website
    with urllib.request.urlopen("https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=" + origin + "&destinations=" + destination + key2) as response:
       rawWebData = response.read().decode('utf8') 
    
    List = []
    final = ""
    decodedWebData = json.loads(rawWebData) #decode data retrieved from json format into lists/dictionary
    if decodedWebData["status"] == "OK": #if the status is OK then there's information
        distance = decodedWebData["rows"][0]["elements"][0]["distance"]["text"] #distance
        duration = decodedWebData["rows"][0]["elements"][0]["duration"]["text"] #amount of time to travel
        #prints the information
        List.append("Distance: " + distance)
        List.append("Duration: " + duration)

    else: #if there's no information the place might be spelled incorrectly so print this
        return("I think you got it wrong! To know the distance and duration just use @travel for example '@travel London to Coventry'")
    
    for i in range(0,len(List)):
        final = final + "\n" + List[i]

    return(final)
    i+=1 #increment by 1
    
if "@travel" in userinput:
    removesentenceTravel(userinput)
elif "@travels" in userinput:
    print("You got it wrong please use '@travel' instead")
else:
    print("I think you got it wrong! To know the distance and duration just use @travel for example '@travel London to Coventry'")
