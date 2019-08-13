import csv

with open('data2.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)
    name = set()
    city = set()
    card = set()
    deposit = set()
    mortgage = set()
    for row in reader:
        name.add(row[0])
        city.add(row[1])
        card.add(row[2])
        deposit.add(row[3])
        mortgage.add(row[4])
g = ((na, ci, ca, de, mo) for na in name for ci in city for ca in card for de in deposit for mo in mortgage)
i = 0
f = open('result.txt', 'w')
while True:
    f.write(next(g)[0] + next(g)[1] + "\t" + next(g)[2] + "\t" + next(g)[3] + "\t" + next(g)[4] + "\n")
    i += 1
    if i == 100:
        break
f.close()
