import socket
import random

def inject_error(data):
    if not data: return data
    data_list = list(data)
    error_type = random.choice(["sub", "del", "ins", "swap"])
    idx = random.randint(0, len(data_list)-1)
    
    if error_type == "sub": # Karakter Değiştirme
        data_list[idx] = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    elif error_type == "del" and len(data_list) > 1: # Karakter Silme
        data_list.pop(idx)
    elif error_type == "ins": # Karakter Ekleme
        data_list.insert(idx, 'X')
    elif error_type == "swap" and len(data_list) > 1: # Yer Değiştirme
        idx2 = (idx + 1) % len(data_list)
        data_list[idx], data_list[idx2] = data_list[idx2], data_list[idx]
        
    return "".join(data_list)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 5000))
    server.listen(1)
    print("Server Bekliyor (Bozucu)...")

    while True:
        conn, addr = server.accept()
        packet = conn.recv(1024).decode()
        if not packet: break
        
        data, method, control = packet.split("|")
        corrupted = inject_error(data)
        new_packet = f"{corrupted}|{method}|{control}"
        
        c2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c2.connect(('127.0.0.1', 6000))
        c2.send(new_packet.encode())
        print(f"Veri Bozuldu: {data} -> {corrupted}")
        conn.close()
        c2.close()

if __name__ == "__main__":
    start_server()