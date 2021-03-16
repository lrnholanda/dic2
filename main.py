anos = {
    'chris': 9,
    'italo': 16,
    'julia': 7,
}
lista = ['chris', 'julia']
#add new key & value
anos['mateus'] = 9

#print value
print(anos['chris'])

for k, v in anos.items():
    print(f"{k.title()}, {v}")

for k in anos.keys():
    print(f"\n{k.title()}")
    if k in lista:
        print(f"hello,{k.title()}")
