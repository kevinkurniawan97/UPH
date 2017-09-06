import socket

s = socket.socket()
host = socket.gethostname()
port = 4444

s.connect ((host,port))
print ("Connected to", host)

while True:
    z = raw_input("Enter text for the server: ")
    s.send(z.encode())

    print ("[Waiting for response...]")
    print ("Server: ",s.recv(1024).decode())

