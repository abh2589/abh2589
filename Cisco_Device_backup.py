from netmiko import ConnectHandler
from getpass import getpass
import telnetlib
import time
import re

z = "y"
while z == "y" or z == "Y":
    print("\n\n**** This Program will save the running configuration of the Cisco device in .txt format ****\n")
    print("\n\nPress 1 if device is accessible via Telnet\nPress 2 if the device is accessible via SSH\n")
    userinput = input("Enter your choice:\t")

    HOST = input("Enter Ip address:\t")
    user = input("Enter Username:\t")
    password = getpass()


    device = {
    'device_type': 'cisco_ios',
    'host': HOST,
    'username': user,
    'password': password,
    'ssh_config_file': './ssh_config',
    } 
    
    if int(userinput) == 1:
        tn = telnetlib.Telnet(HOST)
        tn.read_until(b"login as: ")
        tn.write(user.encode('ascii') + b"\n")
        if password:
            tn.read_until(b"Password: ")
            tn.write(password.encode('ascii') + b"\n")
    
        tn.write(b"terminal len 0")
        tn.write(b"sh run")
        time.sleep(5)
        tn.write(b"exit\n")

        output = tn.read_all().decode('ascii')
        newfile = open(HOST+".txt", "w")
        newfile.write(output)
        newfile.close()
        print(f"Config Backup completed successfully check {HOST}.txt file in the folder ")
        z = input("\nPress y to continue, or press any key to exit:\t")
    
    elif int(userinput) == 2:
        net_connect = ConnectHandler(**device)
        net_connect.send_command("terminal len 0")
        output = net_connect.send_command("show run")
        textfile = open(HOST+".txt", "w")
        textfile.write(output)
        textfile.close()
        print(f"Config Backup completed successfully check {HOST}.txt file in the folder ")
        z = input("\nPress y to continue, or press any key to exit:\t")
    else:
        print("Invalid Choice")
        z = input("\nPress y to continue, or press any key to exit:\t")
    