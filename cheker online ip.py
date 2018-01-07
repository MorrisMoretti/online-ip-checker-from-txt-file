import socket
import re


f = open('ip_list.txt', 'r') #Text file with many ip address
o = f.read()
ip1 = re.findall( r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", o )
hosts = ip1
ports = [80]
for host in hosts:
    for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((host, port))
            if result == 0:
                    print("  [*] Port " + str(port) + " open!" + host)
            else: print("[+] CLOSE HOST " + host + ":" + str(port))
        except:
            pass