def findkeyword(userinput):  #~~~~~create a loop 
    #userinput = input("Please entre your keyword: ") #~~~~input the keyword
    
    userinput = userinput.lower()  #~~~~change the word to lower case
    
    if any(drink in userinput for drink in ("drink","drinking","club","bar")): 
       
        listofdrink = userinput #~~~~more precisely to the place
        listofdrink = listofdrink.lower()    
        
        if  listofdrink in "kabash":   #if it recoginses the loction,it will show the information
            return ["Kabash","club"]
        
        elif listofdrink in "scholars":
            return ["Scholars","club","bar"]
        elif listofdrink in "rainbows":
            return ["Rainbows","club"]
        else:                          #~~~~If it can't recoginse the keyword
            return None #~~~~it shows that it isn't defound
                        
    elif any(park in userinput for park in ("park","parking")):

        listofparking = userinput
        listofparking = listofparking.lower()
        
        if listofparking in ("commebe abbey coventry park"):
            return ["Commebe Abbey Coventry Park","car park"]
        elif listofparking in ("war memorial park"):
            return ["War Memorial Park","car park"]
        elif listofparking in ("brandon marsh nature reserve"):
            return ["Marsh Nature Reserve","car park"]
        else:                  
            return None
        
    elif any(clothe in userinput for clothe in ("clothing","clothe","shoe")):
        
        listofclothe = userinput
        listofclothe = listofclothe.lower()  
        
        if listofclothe in ("topshop"):
            return ["Topshop", "clothing"]
        elif listofclothe in ("h&m"):
            return ["H&M","clothing"]
        elif listofclothe in ("jd"):
            return ["JD","clothing"]
        else:
            return None
        
    elif any(event in userinput for event in ("event","activity")):
        
        listofevent = userinput
        listofevent = listofevent.lower()  
        
        if listofevent in ("coventry cathedral","activity"):
            return ["Coventry Cathedral", "e"]
        elif listofevent in ("james starley statue"):
            return ["James Starley Statue","activity"]
        elif listofevent in ("cook street gate"):
            return ["Cook Street Gate","activity"]
        else:
            return None
        
    else:
        return("Sorry,it is not in the list and try again")  #~~~repeat the code again, until recoginse the 'keyword'
