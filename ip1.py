#first of all import the socket library
import socket
#next create a pocket object
s = socket.socket()
print("Socket successfully created")
port = 40674
#reserve a port on your computer in our
#case it is 40674 but it can be
s.bind(('',port))
print("socket binded to %s" %(port) )
s.listen(5)
print("socket is listening")
while True:
    c, addr = s.accept() # single line ,multi variable assignment
    print('Got connnection from', addr)
    #b- msg going to client.process ip
    c.send(b'Thank you for connecting')
    c.close()

