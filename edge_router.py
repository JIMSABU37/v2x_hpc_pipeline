import socket

EDGE_HOST = '127.0.0.1'
EDGE_PORT = 64000
HPC_HOST = '127.0.0.1'
HPC_PORT = 65000

# Step 1: Listen for the Vehicle
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
    server_sock.bind((EDGE_HOST, EDGE_PORT))
    server_sock.listen()
    print(f"Edge Unit listening for Vehicle on {EDGE_HOST}:{EDGE_PORT}...")
    
    vehicle_conn, vehicle_addr = server_sock.accept()
    with vehicle_conn:
        print(f"Vehicle connected from {vehicle_addr}")
        
        # Step 2: Connect to the HPC Core to offload data
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as hpc_sock:
            hpc_sock.connect((HPC_HOST, HPC_PORT))
            print("Edge Unit connected to HPC Core.")
            
            while True:
                data = vehicle_conn.recv(1024)
                if not data:
                    break
                print(f"Edge routing telemetry -> {data.decode()}")
                
                # Forward to HPC and wait for the acknowledgement
                hpc_sock.sendall(data)
                hpc_response = hpc_sock.recv(1024)
                print(f"Edge received from HPC: {hpc_response.decode()}")