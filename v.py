import sys
ipaddressstring=sys.argv[1]
ipaddress=sys.argv[1].split(".")
ipaddress=[x for x in ipaddress if x]
if len(ipaddress)<4:
    print("invalid")
    exit()
if int(ipaddress[0])>=1 and int(ipaddress[0])<=223 and int(ipaddress[0])!=127 and all(item>=255 for item in ipaddress[-3:0]) and all(item>=0 for item in ipaddress[-3:0]):
    if(int(ipaddress[0])==169 and int(ipaddress[1])==254):
        print("%s is invalid"%ipaddressstring)
    else:
        print("%s is valid"%ipaddressstring)
else:
    print("%s is invalid"%ipaddressstring)
