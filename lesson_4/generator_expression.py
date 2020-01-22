"""File contains expression generator for 100 strings from source.csv data to destination.txt"""

path_src = "source.csv"
path_dest = "destination.txt"

fios = []
cities = []
credit_cards = []
deposits = []
mortgages = []

file_src = open(path_src, "r")

# read header and skip it
file_src.readline()

while True:
    line = file_src.readline()
    if line == "":
        break

    # unpacking list items
    fio, city, card, deposit, mortgage = line.split(";")
    fio = fio.rstrip()
    if fio != "":
        fios.append(fio)
    city = city.rstrip()
    if city != "":
        cities.append(city)
    card = card.rstrip()
    if card != "":
        credit_cards.append("+" if card == "1" else "-")
    deposit = deposit.rstrip()
    if deposit != "":
        deposits.append("+" if deposit == "1" else "-")
    mortgage = mortgage.rstrip()
    if mortgage != "":
        mortgages.append("+" if mortgage == "1" else "-")

file_src.close()

gen_exp = (fio + " " + city + " " + card + " " + deposit + " " + mortgage
           for fio in fios
           for city in cities
           for card in credit_cards
           for deposit in deposits
           for mortgage in mortgages)

first_100_list = list(gen_exp)[:100]

file_dst = open(path_dest, "w")
file_dst.write("\n".join(first_100_list))
file_dst.close()
