#předpoklad pruměrny vek doziti je 90 let.
#uzivatel zada vek (int), tak se dozvi..
#zbyva mu let
#zbyva mu měsíců
# zbývá mu týdnů
# zbývá mu dnů
# Vse se vypise do jedne smysluplne vety F-stringu
vek = input("Zadej svuj vek:\n")
vek = int(vek)
smrt = 90
let = smrt - vek
mesicu = (let*12)
tydnu = (mesicu*4)
dnu = (tydnu*7)
print(f"Staticky ti zbyva do smrti: {let}  let,  {mesicu} mesicu, {tydnu} tydnu a taky {dnu} dnu. \nTak si to sakra uvedom!!!")