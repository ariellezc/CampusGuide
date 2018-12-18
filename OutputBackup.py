def output(KeyName, FindInfo):
    '''Takes Keynam as a string, FindInfo as a list, puts the inputs in a message and ouputs the message as a string'''
    message = []    #Create an empyt list so the message can be edited
    message.append('The')
    message.append(KeyName)     #Add the keyword to the message
    message.append('in Coventry are;')
    count = 0
    for i in range(len(FindInfo)):  #Add each piece of information to the message
        if i < (len(FindInfo)-1):
            message.append(FindInfo[i]+',')
        else:
            message.append(FindInfo[i]+'.')
    return (' '.join(message))  #Combine the contents of the list to return the message as a string

