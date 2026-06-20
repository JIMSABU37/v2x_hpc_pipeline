import socket
import time

EDGE_HOST = '127.0.0.1'
EDGE_PORT = 64000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((EDGE_HOST, EDGE_PORT))
    print("Vehicle connected to Edge Unit.")
    
    # Simulate streaming 5 telemetry bursts
    for i in range(1, 6):
        message = f"Dummy Telemetry Packet {i}"
        s.sendall(message.encode())
        print(f"Vehicle sent: {message}")
        time.sleep(1) # Wait 1 second between transmissions