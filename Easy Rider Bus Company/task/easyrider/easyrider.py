import json
from collections import defaultdict

data_base = json.loads(input())
stop_o = []
start = []
transfer = defaultdict(set)
trans_stop = []
finish = []
wrong = []
for line in data_base:
    transfer[line['stop_name']].add(line['bus_id'])
    if line['stop_type'] == 'S':
        start.append(line['stop_name'])
    elif line['stop_type'] == 'O':
        stop_o.append(line['stop_name'])
    elif line['stop_type'] == 'F':
        finish.append(line['stop_name'])

for k, v in transfer.items():
    if len(v) > 1:
        trans_stop.append(k)

for x in stop_o:
    if x in start or x in trans_stop or x in finish:
        wrong.append(x)

print('On demand stops test:')
if len(wrong) == 0:
    print('Wrong stop type: OK')
else:
    print(f'Wrong stop type: {sorted(wrong)}')
