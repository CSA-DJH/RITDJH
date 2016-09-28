input=open("input.txt")
output=open("output.txt", "w")
output.write("{:20s} {:20s}\n".format("ip_prefix","as_path"))
for row in input:
    subrow=row.split(" ")
    output.write("{:20s} {:20s}\n".format(str(subrow[3]),str(subrow[6:-1])))
    print(str(subrow[3])+" "+str(subrow[6:-1]))
output.close()
input.close()
