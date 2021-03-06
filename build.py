import csv
from pprint import pprint

# Get the source data
data = list(csv.DictReader(open("./statestyle/data.csv", "r")))

# Create the normalizer
crosswalk = {}
for row in data:
    for key, value in row.items():
        if value and key not in ['type', 'stateface']:
            crosswalk[value] = row
            crosswalk[value.lower()] = row
            try:
                crosswalk[int(value)] = row
            except:
                pass

print "CROSSWALK = ",
pprint(crosswalk)
