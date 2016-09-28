ipaddress=input("Please enter an IP Address: ")
ipaddresslist=ipaddress.split(".")
ipaddresslist[3:3]=["0"]
print("\t{:20s} {:20s} {:20s}".format("NETWORK_NUMBER","FIRST_OCTET_BINARY","FIRST_OCTET_HEX"))
print("\t{:20s} {:20s} {:20s}".format(ipaddress,bin(int(ipaddresslist[0])),hex(int(ipaddresslist[0]))))
