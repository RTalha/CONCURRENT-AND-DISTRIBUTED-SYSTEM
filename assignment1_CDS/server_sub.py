def fun(string):
    left = ''
    right = ''
    flag = False
    for i in string:
        if(i != '/' and flag == False):
            left += i
        elif(i != '/' and flag == True):
            right += i
        else:
            flag = True
    left = float(left)
    right = float(right)
    return left-right

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
s.bind(('192.168.1.9', port))         
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
