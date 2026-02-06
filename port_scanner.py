import socket

def port_scanner():
    target = input("Enter target (IP or domain): ")
    start_port = 1
    end_port = 1024

    print(f"\nScanning target: {target}\n")

    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)

        result = s.connect_ex((target, port))

        if result == 0:
            print(f"Port {port} is OPEN")

        s.close()

    print("\nScan completed.")

# Run the scanner
port_scanner()
