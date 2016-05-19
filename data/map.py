import json

with open('composers.json') as data_file:    
    data = json.load(data_file)

def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] 
             for i in range(wanted_parts) ]

def dump(alist, name):
    with open(name, 'w') as outfile:
            json.dump(alist, outfile)

data = split_list(data, wanted_parts=10)    

for index, alist in enumerate(data):
    dump(alist, 'composer' + str(index) + '.json')
