import getpass
import telnetlib
import time
import re

HOST = "12.0.1.28"
#user = input("Enter your remote account: ")
#password = getpass.getpass()
user = "rviews"
password = "rviews"
print("\n\n**** Program To Test IP address reachability from the Internet ****\n")
z = "y"
while z == "y" or z == "Y":
    ipaddress = input("Please input the IP address to reachability from the internet: ")
    time.sleep(2)
    print("\n\nVerifying Reachability kindly wait\n\n")

    tn = telnetlib.Telnet(HOST)
    
    tn.read_until(b"login: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password:")
        tn.write(password.encode('ascii') + b"\n")

    #tn.write(b"ping 41.160.0.244 count 5\n")
    string1 = f"ping {ipaddress} count 5\n"
    tn.write(str.encode(string1))
    time.sleep(5)
    tn.write(b"exit\n")

    #print(tn.read_all().decode('ascii'))
    output = tn.read_all().decode('ascii')

    r1 = re.search(r", 0% packet loss",output)
    #print(r1.group())
    try:
        if r1.group() == ", 0% packet loss":
            print(f"\nThe IP Address: {ipaddress} is reachable from AT&T Route server without any loss")
            print(f"\nRouter server IP :\t 12.0.1.28\nRoute Server AS Number : 7018\n")
            z = input("\nPress y to continue, or press any key to exit:\t")
    


    except AttributeError:
            print(f"IP Address: {ipaddress} is not reachable from route server 12.0.1.28 , Please check if IP is advertised over internet")
            z = input("\nPress y to continue, or press any key to exit:\t")
    


    

