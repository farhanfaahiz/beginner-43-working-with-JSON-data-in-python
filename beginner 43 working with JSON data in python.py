import json

a = {
    'name': 'max',
    'age': 22,
    'marks': [90, 50, 80, 40],
    'pass': True,
    'object': {
        'color':('red', 'blue')
    } 
}

with open('demo.json', 'w') as fh:
    fh.write(json.dumps(a, indent=2, sort_keys=True))
    

with open('demo.json', 'r') as fh:
    json_str = fh.read()
    json_value = json.loads(json_str)
    print(type(json_value))
    print(json_value['object'])
    
with open('demo.json', 'r') as fh:
    print(fh.read())