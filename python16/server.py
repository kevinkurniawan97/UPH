import socket

s = socket.socket()
host = socket.gethostname()
port = 4444
s.bind ((host,port))

s.listen(5)
c = None

while True:
    if c is None:
        print ("[Waiting for connection...]")
        c,addr = s.accept()
        print ("Got connection from ",addr)
    else:
        print ("[Waiting for response...]")
        print ("Client: ",c.recv(1024).decode())
        q = raw_input("Enter text to this client: ")
        c.send(q.encode())
