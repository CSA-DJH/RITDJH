import sys
ipaddress=sys.argv[1].split(".")
ipaddressbin=[]
for i in range(len(ipaddress)):
    ipaddressbin.append(bin(int(ipaddress[i])))
print("%s\t\t%s\n%s\t\t%s"%("IP address","Binary",ipaddress,(".".join(repr(i)for i in ipaddressbin).replace("'",""))))
