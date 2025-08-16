import socket as skt
import time
import threading as thr
s = skt.socket()

def al(s):
    print(s.recv(1024).decode())
while True:
    try:
        s.connect(('rnguo-94-54-8-159.a.free.pinggy.link',35095))
        break
    except Exception as e:
        print(f'Bağlanamadı. 5 saniye içinde tekrar deneniyor... Hata: {e}')
        time.sleep(5)

s.send('Hey, buradayim!!!'.encode())
thr.Thread(target=al,args=(s,),daemon=True).start()
while True:
    s.send(input().encode())