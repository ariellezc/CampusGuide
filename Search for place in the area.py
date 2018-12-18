"""Search for things related to a location and returns a list related to what was searched for"""

#import library to access webpage
import json
import requests #http://docs.python-requests.org/en/master/user/quickstart/
import urllib.request 
from key import key1, app_key, app_id, language #import from key.py

userinput = input(""">""") #enter user input
userinput.lower() #make userinput lower case
listSynonyms = [] #empty synonyms list

#function for putting all synonyms in list of synonyms
#documentation for API found in https://developer.oxforddictionaries.com/documentation under the synonyms section
def synonyms():
    
    wordSynonyms = ['near','close','in'] #list of words that will be searched for synonyms
    urlList = [] #empty url list
    n=0 #set the value of n as 0
    
    #appends the list of url for synonyms for each specfic word in wordSynonyms
    for n in range(len(wordSynonyms)): #iterates as many times as the length of wordSynonyms
        url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + wordSynonyms[n].lower() + '/synonyms' #
        n+=1 #increment n by 1
        urlList.append(url) #append url to urlList
    
    #get webpages listed in urlList
    near = requests.get(urlList[0], headers = {'app_id': app_id, 'app_key': app_key}) 
    close = requests.get(urlList[1], headers = {'app_id': app_id, 'app_key': app_key})
    pIn = requests.get(urlList[2], headers = {'app_id': app_id, 'app_key': app_key})

    #decode json data
    rawWebDict1 = near.json()
    rawWebDict2 = close.json()
    rawWebDict3 = pIn.json()

    i=0 #set value of i to 0

    #append the list according to their synonyms (near, close, in). 
    #This list contains synonyms of the word to allow other userinput related to the word
    for i in range(len(rawWebDict1["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["synonyms"])): #for every list of synonyms related to near
        synonyms1 = rawWebDict1["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["synonyms"][i]["text"] #goes to every list
        i+=1 #increment by 1
        listSynonyms.append(synonyms1) #append each synonyms to list of synonyms

    #same process happen but for word "close"
    for i in range(len(rawWebDict2["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["synonyms"])):
        synonyms2 = rawWebDict2["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["synonyms"][i]["text"]
        i+=1
        listSynonyms.append(synonyms2)
    #same process happen but for word "in"
    for i in range(len(rawWebDict3["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["synonyms"])):
        synonyms3 = rawWebDict3["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["synonyms"][i]["text"]
        i+=1
        listSynonyms.append(synonyms3)

#function for removing irrelevant sentence
def removesentence(userinput):
    listWords = userinput.split() #split the string
    if len(listWords) == 1: #if length of listWords is 1 -- this means the user input @places without any strings following it
        return 'I think you put an invalid place or your format is wrong. Remember you have to follow this format: @places bars near coventry.' #tells the user the correct format
    elif listWords[0] == "@places": #checks if the first element on the list is "@places"
        listWords.pop(0) #removes the index containing @places
        strings = str(listWords).strip('[]') #removes square brackets
        place = ",".join(listWords).replace(","," ") #joins together by a comma and separates by space
        print(placesearch(place))
    else: #if the above is not true then run this part of the code
        listIndex = [i for i in range(len(listWords)) if listWords[i] == '@places'] #takes the index containing @places
        cStr = str(listIndex).strip('[]') #strip the brackets
        cInt = int(cStr) #convert string to integer
        del listWords[0:cInt+1] #removes the first index until the index containing string
        place = ",".join(listWords).replace(","," ") #replace the comma and put a space to join the words
        print(placesearch(place)) #goes to the function placesearch(search)

def placesearch(search):
    synonyms() #goes to the synonyms function 
    validList = ["near","close by","close","in"] #list of validList
    placeSearch = search.replace(" ","+") #replace the separator with + so that it can be use for url
    #retrive data from a website
    with urllib.request.urlopen("https://maps.googleapis.com/maps/api/place/textsearch/json?query=" + placeSearch + key1 ) as response:
       rawWebData = response.read().decode('utf8') #decode web data

    #decode the data retrived from json format into lists/dictionaries
    decodedWebData = json.loads(rawWebData)
    List = [] 
    final = ""
    if decodedWebData["status"] == "OK": #this checks if there are actual search results
        
        if any(substring in search for substring in validList) or  any(substring in search for substring in listSynonyms): #checks if the input is in validList or listSynonyms https://stackoverflow.com/questions/16505456/how-exactly-does-the-python-any-function-work
            i=0  #set i equivalent to 0          
            for i in range(len(decodedWebData["results"])): #iterates by the number of results in the webData 
                #prints the relevant data related to what is searched for but checks if key exist           
                if "name" not in decodedWebData["results"][i]:
                    continue
                else:       
                    near = decodedWebData["results"][i]["name"]
                    List.append("\n"+near)

                if "formatted_address" not in decodedWebData["results"][i]:
                    continue
                else:
                    address = decodedWebData["results"][i]["formatted_address"]
                    List.append("Address: " + address)
                    
                if "rating" not in decodedWebData["results"][i]:
                    continue
                else:
                    rating = decodedWebData["results"][i]["rating"]
                    List.append("Rating: "+ str(rating))
                
                if "photos" not in decodedWebData["results"][i]:
                    continue
                else:
                    link = decodedWebData["results"][i]["photos"][0]["html_attributions"]
                    List.append("Link: " + str(link))
               
                for i in range(0,len(List)):
                    final = final + "\n" + List[i]
                i+=1 #increment by 1

            return(final)
                
    else: #if there is no search result then this means that the format is either invalid or the place is spelled incorrectly
        return 'I think you put an invalid place or your format is wrong. Remember you have to follow this format: @places bars near coventry.'

if "@places" in userinput:
    removesentence(userinput)
elif "@place" in userinput:
    print("You got it wrong please use '@places' instead")
else:
    print("I think you got it wrong! To search for places near the area just use @places: '@places bars near coventry'")
