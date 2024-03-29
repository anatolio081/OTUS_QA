import csv

# без множеств не смог сделать данные уникальными, так как такие значения как города, карта, вклад, ипотека - дублируются
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
# описал генератор на 4х множествах
g = ((na, ci, ca, de, mo) for na in name for ci in city for ca in card for de in deposit for mo in mortgage)
i = 0
f = open('result.txt', 'w')
# построчно загоняю данные из множеств в строки с табуляциями и переходом на следующую, как на примере
while True:
    result_raw = next(g)
    f.write(result_raw[0] + result_raw[1] + "\t" + result_raw[2] + "\t" + result_raw[3] + "\t" + result_raw[4] + "\n")
    i += 1
    if i == 100:
        break
f.close()
