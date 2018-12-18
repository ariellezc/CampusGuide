userinput = raw_input("welcome to the chatbot... ") #this input will be changed once integrated with other code

shopsDict = ['Wilkinsons', 'SPAR', 'Boots', 'Marks & Spencers' ]
clothingDict = ['Topshop', 'Topman', 'H&M', 'Riverisland', 'Debenhams', 'JD', 'Sportsdirect', 'Footlocker', 'Primark', 'Newlook' ]
upcomingGamesDict = ['Call of Duty WWII', 'Star Wars Battlefront II', 'Far Cry 5', 'Dragon Ball FighterZ' ]
eventsDict = ['Christmas lights_switch_on', 'Farmers market', 'CAIF peace concert', 'Christmas fair' ]
cinemaDict = ['Paddington 2', 'Thor Ragnarok', 'Jigsaw', 'Murder on the orient express', 'A bad moms christmas', 'Dispicable me 3']
clubbingDict = ['Kabash', 'Scholars', 'Rainbows', 'Catchtwentytwo', 'ClubM', 'DaddyCools', 'JJ', 'Rileys sports bar' ]
#Lists which allow for all the data to be stored allowing us to see what is avaliable in coventry

#if statments are used to be able to compare user information 
if any(drink in userinput for drink in ("drinking", "club", "bar")):
    print "The following are clubs in the Coventry area... "+ ', '.join(clubbingDict) 
    
elif any(shop in userinput for shop in ("shop", "shopping","shops", "store", "stores")):
    print "The following are shops in the Coventry area... "+ ', '.join(shopsDict)
    
elif any(clothe in userinput for clothe in ("clothing", "clothe", "shoe")):
    print "The following are clothing stores in the Coventry area... "+ ', '.join(clothingDict)
    
elif any(games in userinput for games in ("games", "game", "gaming", "video games")):
    print "The following are upcoming games... "+ ', '.join(upcomingGamesDict)
               
elif any(event in userinput for event in ("event", "events", "upcoming")):
    print "The following are events in the Coventry area... "+ ', '.join(eventsDict)
    
elif any(movie in userinput for movie in ("film", "films", "cinema", "movie")):
    print "The following are films showing in the Coventry area... "+ ', '.join(cinemaDict)
    
#These if statments will give the user an output of a list of all of the information as an output
    
else:
    print "I'm sorry I don't know what you said"
#this shows the alternative output making it clear to the user that it does not understand the input


