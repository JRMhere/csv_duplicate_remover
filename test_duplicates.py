import remove_duplicates_wip as rm_d
import csv

x = [{'x':1,'y':2,'z':3},{'a':4,'b':5,'c':6},{'d':7,'e':8,'f':9},{'x':5,'y':6,'z':3},{'d':5,'e':5}]

#Test rm_by_col
y = rm_d.rm_by_col(x)
print(y)
for item in y.items():
    print(item)
    print(item[1])

#Test dl_to_ld
z = rm_d.dl_to_ld(y)
print("List of dictionaries:")
print(z)

outfile = "out.csv"

o = z

with open(outfile, 'w', newline='') as csvfile:
        #when this is called, o should be a list of dictionaries by this point.
        fieldnames = []
        for item in o[0]:
            fieldnames.append(item)
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in o:
            writer.writerow(row)