#vypocitejte BMI, ktere se pocita jako
# BMI = vaha v kg / (vyska v m)^2
vyska = input("zadejte svou vysku v metrech(oddelene teckou):\n")
vaha = input("zadejte svou vahu v kg:\n")
vyskanadruhou = float(vyska)**2
vahafloat = float(vaha)
print("Vas BMI je: "+ str(round(vahafloat / vyskanadruhou, 2)))