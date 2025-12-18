import socket
import binascii

def recalculate(data, method):
    if method == "PARITY":
        ones = bin(int.from_bytes(data.encode(), 'big')).count('1')
        return "Even-0" if ones % 2 == 0 else "Even-1"
    elif method == "CRC16":
        return hex(binascii.crc_hqx(data.encode(), 0)).upper()[2:]
    elif method == "2DPARITY":
        return f"R{len(data)}C{sum(ord(c) for c in data) % 10}"
    elif method == "HAMMING":
        return "H-" + "".join(str(ord(c) % 2) for c in data[:min(4, len(data))])
    return "0000"

def start_client2():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 6000))
    server.listen(1)
    print("Client 2 Bekliyor (Alıcı)...")

    while True:
        conn, addr = server.accept()
        packet = conn.recv(1024).decode()
        data, method, incoming_control = packet.split("|")
        
        computed = recalculate(data, method)
        
        print("\n" + "-"*35)
        print(f"Received Data: {data}")
        print(f"Method: {method}")
        print(f"Sent Check Bits: {incoming_control}")
        print(f"Computed Check Bits: {computed}")
        
        if incoming_control == computed:
            print("Status: DATA CORRECT")
        else:
            print("Status: DATA CORRUPTED")
        print("-"*35)
        conn.close()

if __name__ == "__main__":
    start_client2()