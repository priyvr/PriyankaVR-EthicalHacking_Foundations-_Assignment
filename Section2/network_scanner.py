import socket
import time

target = input("Enter IP: ")
ports = [21, 22, 80, 443, 3306]

start = time.time()

file = open("scan_results.txt", "w")

for port in ports:
    s = socket.socket()
    s.settimeout(1)
    
    result = s.connect_ex((target, port))
    
    if result == 0:
        print(f"Port {port}: OPEN")
        file.write(f"Port {port}: OPEN\n")
    else:
        print(f"Port {port}: CLOSED")
        file.write(f"Port {port}: CLOSED\n")
    
    s.close()

end = time.time()

print("Scan completed in", end - start, "seconds")
file.close()