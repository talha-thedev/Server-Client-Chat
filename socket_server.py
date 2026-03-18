import socket as skt
import threading as thrd

def al(bagt):
    while True:
     print(bagt.recv(1024).decode('utf-8', errors='ignore'))

def ver(bagt):
   bagt.send(input("You'r message:").encode())


s= skt.socket(skt.AF_INET,skt.SOCK_STREAM)
s.bind(('',the port you wanted(has to be same as your client.))) #this will take your default IP adress 
print('Dinliyorum...')
s.listen(1)
bagt, addr=s.accept()

thrd.Thread(target=al,args=(bagt,),daemon=True).start()
while True:
   bagt.send(input().encode())
   pass
