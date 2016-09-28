ipaddress=input("Please enter an IP Address: ")
ipaddress=ipaddress.split(".")
for i in range(len(ipaddress)):
    print("{:20s}".format("octet_"+"%s"%i),end="")
print("")
for i in range(len(ipaddress)):
    print("{:20s}".format(bin(int(ipaddress[i])))+" ", end="")
