import csv


with open('fullnames.csv','r') as f:
    reader = csv.reader(f)
    newcsvdict = {"first name": [], "last name": []}
    for row in reader:
        first = row[0].split()[0]
        last = row[0].split()[1]
        newcsvdict["first name"].append(first)
        newcsvdict["last name"].append(last)


header = ['first name', 'last name']
with open('fullnames.csv', 'r') as infile, open('new.csv', 'w') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(header)
    writer.writerows(row[0].split() for row in csv.reader(infile))
