# Import socket module 
import socket                
  
# Create a socket object   
# Define the port on which you want to connect 
port = 50123                
while True:
    # connect to the server on local computer
    a=input("enter first value")
    b=input("enter 2nd value")
    c=int(input("select 1 for add,2 for subtract,3 for multiply,4 for exit"))
    if c==1:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.1.5', port)) 

        # receive data from the server 
        s.send(str.encode(a+"/"+b))
        print (s.recv(1024).decode('UTF-8') )

        # close the connection 
        s.close()
    elif c==2:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.1.9', port)) 

        # receive data from the server 
        s.send(str.encode(a+"/"+b))
        print (s.recv(1024).decode('UTF-8') )

        # close the connection 
        s.close()
    elif c==3:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(('192.168.1.10', port)) 

        # receive data from the server 
        s.send(str.encode(a+"/"+b))
        print (s.recv(1024).decode('UTF-8') )

        # close the connection 
        s.close()
    elif c==4:
        break    
