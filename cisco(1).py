input=open("input.txt")
output=open("output.txt", "w")
output.write("\t{:20s} {:20s}\n".format("ip_prefix","as_path"))
for row in input:
    subrow=row.split(" ")
    output.write("\t{:20s} {:20s}\n".format(str(subrow[1]),str(subrow[4:-1])))
    print(str(subrow[1])+" "+str(subrow[4:-1]))
output.close()
input.close()
