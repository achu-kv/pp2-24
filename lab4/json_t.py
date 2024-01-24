import json

def report(data):
    print("Interface Status", "=" * 80, sep="\n")
    print("DN                                                 Description           Speed    MTU")
    print(f'{"-" * 50} {"-" * 20} {"-" * 7} {"-" * 6}')
    desc = " " * 20
    for i in data["imdata"]:
        dn = i["l1PhysIf"]["attributes"]["dn"]
        dn += " " * (50 - len(dn))
        spd = i["l1PhysIf"]["attributes"]["speed"]
        mtu = i["l1PhysIf"]["attributes"]["mtu"]
        print(dn, desc, spd, mtu, sep=" ")
        
        
with open("sample-data.json") as jsf:
    data = json.load(jsf)
report(data)