from netmiko import ConnectHandler router = {
"device_type": "cisco_ios", "host": "192.168.222.133",
"username": "admin", "password": "admin123",
"ssh_config_file": "/home/apsal/my_prjt/ssh_config",
}
def deploy(commands):
print("[INFO] Deploying configuration...") net = ConnectHandler(**router) net.send_config_set(commands.split("\n")) net.disconnect()
print("[SUCCESS] Configuration applied.")
