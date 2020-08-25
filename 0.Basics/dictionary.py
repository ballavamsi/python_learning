d = { 'name': 'vamsi', 'age': 'won''t say'}
print(d)
print(d.items())

print(d.keys())

d['age'] = 30

for i in d.items():
    print(i)

if 'action' in d.keys():
    d['action'] = 'Vamsi'
else:
    d['action'] = 'Nothing'

print(d)

s = "abcdefghijkalmnopqrstuvd"
li = list(s)
d = {}

for c in li:
    if not c in d.keys():
        d[c] = c

print(''.join(d.values()))

d = {}
for c in li:
    if c in d.keys():
        d[c] += 1
    else:
        d[c] = 1

print(d.keys())
print(d.values())
print(d)