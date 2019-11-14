import csv
import sys


old_filename = sys.argv[1]
new_filename = sys.argv[2]

with open(old_filename, newline='') as old_file:
    reader = csv.reader(old_file, delimiter='|')
    rows = [line for line in reader]

with open(new_filename, mode='wt', newline='') as new_file:
    writer = csv.writer(new_file)
    writer.writerows(rows)