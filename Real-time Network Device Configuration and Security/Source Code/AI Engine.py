def generate_commands(intent): intent = intent.lower()
cmds = []
print("[INFO] Mock AI processing intent...") if "ssh" in intent:
cmds += [
 
"ip domain-name project.local",
"username admin privilege 15 secret admin123", "crypto key generate rsa modulus 1024",
"ip ssh version 2", "line vty 0 4", "login local", "transport input ssh"
]
if "logging" in intent: cmds.append("logging buffered 64000") if "gateway" in intent:
cmds += [
"interface FastEthernet1/0",
"ip address 192.168.1.1 255.255.255.0",
"no shutdown", "exit",
"interface FastEthernet1/1",
"ip address 192.168.2.1 255.255.255.0",
"no shutdown", "exit"
]
if "ospf" in intent:
cmds += [ "router ospf 1",
"network 192.168.1.0 0.0.0.255 area 0",
"network 192.168.2.0 0.0.0.255 area 0", "exit"
]
return "\n".join(cmds)
