import socket

IP = "192.168.2.2"
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ws:
    ws.bind((IP, PORT))
    ws.listen(1)
    print("esperando")
    conn, data = ws.accept()
    print("conectado")

    while conn:
        d = conn.recv(1024)
        if not d:
            break
        print(conn.recv(1024))

