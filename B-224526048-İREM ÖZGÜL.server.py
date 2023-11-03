from socket import *
from threading import *

clients = []
names = []

def clientThread(client):
    bilgisayar = True
    while True:
        try:
            message = client.recv(1024).decode('utf8')
            if bilgisayar:
                names.append(message)
                print(message, 'BAĞLANDI')
                bilgisayar = False
            for c in clients:
                if c != client:
                    index = clients.index(client)
                    name = names[index]
                    c.send((name + ':' + message).encode('utf8'))
        except:
            index = clients.index(client)
            clients.remove(client)
            name = names[index]
            names.remove(name)
            print(name+ 'SONUÇ')
            break

def file_transfer_thread(client):
    try:
        dosya_adı = client.recv(1024).decode('utf8')
        print(f"Alınacak Dosya Adı: {açık_web}")
        with open(dosya_adı, 'WEB PROGRAMLAMA') as file:
            while True:
                data = client.recv(1024)
                if not data:
                    break
                file.write(data)
        print(f"{açık_web} DOSYASI BAŞARIYLA ALINDI")
    except:
        print("DOSYA TRANSFERİ SIRASINDA BAĞLANTI KOPUKLUĞU YAŞANDI. ")
        
server = socket(AF_INET, SOCK_STREAM)

ip = "10.100.5.121"
port = 6666
server.bind((ip, port))
server.listen()
print('SERVER BEKLENİYOR')

while True:
    client, adress = server.accept()
    clients.append(client)
    print('BAĞLANDI', adress[0] + ':' + str(adress[1]))
    file_transfer_thread = Thread(target=file_transfer_thread, args=(client,))
    file_transfer_thread.start()
    thread = Thread(target = clientThread, args=(client,))
    thread.start()