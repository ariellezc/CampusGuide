# List of keywords that are being checked for
keywords = ["pub","clothes","club","parks","where","drinking","drinks","nightclub","clothing","shops","shopping","pubs","shop","drink","clubs","fitness","gym","sport","activity","activities","museum","museums","cathedral","cathedrals","gallery","galleries","theatre","park","reserve","reserves","train","station"]
def isinlist(item):
    """ Takes an item and returns True if it is in the keywords list. Takes item as a string"""
    if item in keywords:
        return True
    else:
        return False


def findKeywords(serverinput): 
    """ Takes input from the server, returns a list of found keywords as a list """
    serverinput = str(serverinput)
    serverinput = serverinput.lower() # Makes the string lowercase
    wordlist = serverinput.split() # Splits the sentence into a list of words
    
    return list(filter(isinlist,wordlist)) # returns a list containing all of the words that match one of the keywords
