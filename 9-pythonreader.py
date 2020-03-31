import csv

"""
# 'r' means read-only
file_for_reading = open('reading_file.txt', 'r')
# 'w' is write -- will destroy the file if it already exists!
file_for_writing = open('writing_file.txt', 'w')
# 'a' is append -- for adding to the end of the file
file_for_appending = open('appending_file.txt', 'a')
# don't forget to close your files when you're done
file_for_writing.close()

with open('test.txt', 'r') as f:
    for line in f:
        if re.match("^#", line):
            print(line)


def get_domain(email_address):
    return email_address.lower().split("@")[-1]


with open('email_addresses.txt', 'r') as f:
    domain_counts = Counter(get_domain(line.strip()) for line in f if '@' in line)

"""

with open('tab_delimited_stock_prices.txt', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    print('----File without headers----')
    for row in reader:
        date = row[0]
        symbol = row[1]
        closing_price = float(row[2])
        print(date, symbol, closing_price)

with open('colon_delimited_stock_prices.txt', 'r') as f:
    reader = csv.DictReader(f, delimiter=':')
    print('----File with headers----')
    for row in reader:
        date = row['date']
        symbol = row['symbol']
        closing_price = row['closing_price']
        print(date, symbol, closing_price)

today_prices = {'AAPL': 90.91, 'MSFT': 41.68, 'FB': 64.5}
with open('comma_delimited_stock_prices.txt', 'w') as f:
    writer = csv.writer(f, delimiter=',')
    for stock, price in today_prices.items():
        writer.writerow([stock, price])

results = [["test1", "success", "Monday"], ["test2", "success, kind of", "Tuesday"]]
with open('comma_in_string.txt', 'w') as f:
    writer = csv.writer(f, delimiter=',')
    for test_num, status, day in results:
        writer.writerow([test_num, status, day])


