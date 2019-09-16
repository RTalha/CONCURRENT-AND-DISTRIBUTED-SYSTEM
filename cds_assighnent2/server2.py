def fun(string):
    a=string.split("/")

    left = float(a[0])

    right = float(a[1])
    check=int(a[2])
    if(check==0):
        return add(left,right)
    elif(check==1):
        return sub(left,right)
    elif(check==2):
        return mul(left,right)
    else:
        return 0

def add(a,b):
    return a+b
def mul(a,b):
    return a*b
def sub(a,b):
    return a/b
 

# first of all import the socket library

import socket               

  

# next create a socket object

s = socket.socket()         

print ("Socket successfully created")

 

# reserve a port on your computer in our

# case it is 12345 but it can be anything

port = 50123               

  

# Next bind to the port

# we have not typed any ip in the ip field

# instead we have inputted an empty string

# this makes the server listen to requests 

# coming from other computers on the network

s.bind(('192.168.1.10', port))        

print ("socket binded to %s" %(port))

  

# put the socket into listening mode

s.listen(5)     

print ("socket is listening")

while True:

  

   # Establish connection with client.

    c, addr = s.accept()     

    print ('Got connection from', addr)

    a=c.recv(1024).decode('UTF-8')

    b=str(fun(a))

    c.send(str.encode(b))

 

   # Close the connection with the client

c.close()

 
