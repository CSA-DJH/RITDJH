input=open("input1.txt")
list=[]
for row in input:
    subrow=row.split(" ")
    subrow[:]=(value for value in subrow if value!="")
    if (subrow[-2]=="up" and subrow[-1]=="up\n") or (subrow[-2]=="up" and subrow[-1]=="up"):
        list.append(tuple(subrow))
print(list)
