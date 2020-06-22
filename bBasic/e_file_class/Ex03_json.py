import json

f = open('data/temp.json', 'r', encoding='utf-8')
data = f.read()
print(data)
print('-'*50)

items = json.loads(data)
print(items)

for item in items:
    print('>', item)

for item in items.values():
    print('>', item)

for item in items.values():
    for a in item.values():
        print(a)



