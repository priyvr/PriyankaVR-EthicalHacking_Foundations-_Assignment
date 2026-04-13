import socket
from datetime import datetime

target = input("Enter target IP: ")

ports = [21, 22, 80, 443, 3306]
open_ports = []

print("\nScanning target...\n")

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    if s.connect_ex((target, port)) == 0:
        print(f"Port {port} OPEN")
        open_ports.append(port)
    else:
        print(f"Port {port} CLOSED")

    s.close()

# Create HTML report
file_name = "report.html"

with open(file_name, "w") as f:
    f.write("<html><head><title>Security Report</title></head><body>")
    f.write("<h2>Security Audit Report</h2>")
    f.write(f"<p>Target: {target}</p>")
    f.write(f"<p>Time: {datetime.now()}</p>")
    f.write("<h3>Open Ports:</h3><ul>")

    for p in open_ports:
        f.write(f"<li>Port {p}</li>")

    f.write("</ul></body></html>")

print("\nReport generated: report.html")