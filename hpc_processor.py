import socket

HOST = '127.0.0.1'  # Localhost for local testing
PORT = 65000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"HPC Core listening on {HOST}:{PORT}...")
    
    conn, addr = s.accept()
    with conn:
        print(f"Connected to Edge Unit at {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"HPC received task: {data.decode()}")
            # Simulate processing and send an acknowledgement back
            conn.sendall(b"HPC ACK: Matrix processed")