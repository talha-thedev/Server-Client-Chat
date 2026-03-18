import socket as skt
import time
import threading as thr
s = skt.socket()

def al(s):
    print(s.recv(1024).decode())
while True:
    try:
        s.connect(('Your IP adress',the port you want to use))
        break
    except Exception as e:
        print(f"Can't connect. Trying again in 5 seconds... Err: {e}")
        time.sleep(5)

s.send('Hey, buradayim!!!'.encode())
thr.Thread(target=al,args=(s,),daemon=True).start()
while True:
    s.send(input().encode())