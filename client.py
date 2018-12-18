import socket # import socket

def sendmessage(Message):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 12344
    client.connect(('localhost', port)) # connect to port

    try:
            msg = Message
            client.send( msg.encode('utf-8') ) # sends the message

            returnmsg = client.recv(1024) # return message
            message = returnmsg.decode('utf-8').rstrip('\r\n')
            #print(message) #output the message
            return message

    except KeyboardInterrupt:
        print('Shutdown')
        client.shutdown(1)
        client.close()
