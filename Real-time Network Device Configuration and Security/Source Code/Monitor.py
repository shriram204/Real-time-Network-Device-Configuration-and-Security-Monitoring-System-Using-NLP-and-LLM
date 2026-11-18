from netmiko import ConnectHandler router = {
"device_type": "cisco_ios", "host": "192.168.222.133",
"username": "admin", "password": "admin123",
}
AUTHORIZED_INTERFACES = [
"FastEthernet0/0", "FastEthernet1/0", "FastEthernet1/1"
]
def monitor():
alerts = []
net = ConnectHandler(**router)
interfaces = net.send_command("show ip interface brief") net.disconnect()
lines = interfaces.splitlines() for line in lines[1:]:
parts = line.split() if len(parts) >= 6:
iface = parts[0] status = parts[4] proto = parts[5]
if iface not in AUTHORIZED_INTERFACES and status == "up" and proto == "up": alerts.append(f"Unauthorized interface ACTIVE -> {iface}")
 
if iface in AUTHORIZED_INTERFACES and (status != "up" or proto != "up"): alerts.append(f"Trusted interface DOWN -> {iface}")
return alerts
