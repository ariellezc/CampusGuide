from keyname import findkeyword
from Keywords import findKeywords
from InfoGather import findInfo
from OutputBackup import output

# Generate responce

def serverProcessing(serverInput):
    serverInput = serverInput.lower()
    KeyName = findKeywords(serverInput)
    if KeyName == []:
        return "Sorry no keywords found"
    FindInfo = findInfo(KeyName)
    if FindInfo == "No information found":
        return "Sorry I do not know how to deal with the request"
    Output = output(KeyName,FindInfo)
    return Output
