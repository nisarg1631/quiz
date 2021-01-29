import json
with open(f'./quiz_data/tagged/mela.json') as f1:
    lo_data = json.load(f1)
for x in lo_data:
    print(x[0],x[1])