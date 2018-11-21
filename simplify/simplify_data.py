
# Read in from ../data/death.json and write out ../data/compact_death.json

import json

with open('../data/death.json') as json_data:
    d = json.load(json_data)


new_data = []

for item in d['data']:
    row = {'year': item[8] ,
           'cause': item[10],
           'state': item[11],
           'deaths': item[12],
           'rate': item[13]}
    new_data.append(row)

with open('../data/compact_death.json', 'w') as outfile:
    json.dump(new_data, outfile, sort_keys=True, indent=2)
