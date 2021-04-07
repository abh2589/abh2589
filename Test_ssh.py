from netmiko import ConnectHandler
from getpass import getpass

host = input("Enter Ip address:\t")

device = {
    'device_type': 'cisco_ios',
    'host': host,
    'username': input("Enter your username:\t"),
    'password': getpass(),
    'ssh_config_file': './ssh_config',
} 

net_connect = ConnectHandler(**device)
net_connect.send_command("terminal len 0")
output = net_connect.send_command("show run")
textfile = open(host+".txt", "w")
textfile.write(output)
textfile.close()


