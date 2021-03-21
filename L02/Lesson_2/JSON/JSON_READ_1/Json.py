import json as j

def Open():
    with open('JSON/JSON_READ_1/states.json','r') as f:
        vals=j.load(f)
    
    for x in vals['states']:
        print(str(x['name'])+'---'+x['abbreviation'])

if __name__=='__main__':
    Open()