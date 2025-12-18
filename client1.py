import socket
import binascii

def calculate_checksum(data, method):
    if method == "1": # Parity
        ones = bin(int.from_bytes(data.encode(), 'big')).count('1')
        return "Even-0" if ones % 2 == 0 else "Even-1"
    elif method == "2": # CRC16
        return hex(binascii.crc_hqx(data.encode(), 0)).upper()[2:]
    elif method == "3": # 2D Parity Simülasyonu
        return f"R{len(data)}C{sum(ord(c) for c in data) % 10}"
    elif method == "4": # Hamming
        return "H-" + "".join(str(ord(c) % 2) for c in data[:min(4, len(data))])
    return "0000"

def start_client1():
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('127.0.0.1', 5000))
        
        text = input("Gönderilecek Metin: ")
        print("Yöntemler: 1-Parity, 2-CRC16, 3-2D Parity, 4-Hamming")
        choice = input("Seçiminiz: ")
        
        m_list = {"1":"PARITY", "2":"CRC16", "3":"2DPARITY", "4":"HAMMING"}
        method_name = m_list.get(choice, "PARITY")
        control = calculate_checksum(text, choice)
        
        packet = f"{text}|{method_name}|{control}"
        client.send(packet.encode())
        print(f"Paket Gönderildi: {packet}")
        client.close()
    except Exception as e:
        print(f"Hata: {e}. Önce server.py'yi çalıştırdığınızdan emin olun.")

if __name__ == "__main__":
    start_client1()