print("Vitejte v kalkulatoru na vypocet plateb")
# Kolik mate celkem zaplatit? V restauraci 100.
# Kolik chcete dat spropitne (v %) 50 
# Mezi kolik lidi se ma rozdelit castka? 2
# Kazdy clovek by mel zaplatit 75.0
platba_celkem = int(input("K platbe celkem Kc: "))
sprop =int(input("Kolik date spropitne v %?: "))
stravnici = int(input("Zadej pocet stravniku: "))

platba_vypocet = int((platba_celkem + (platba_celkem * sprop / 100))/ stravnici)
print(f"Kazdy z vas plati {platba_vypocet} Kc. Dekuji... nebo bude platit pan?")
print("Pauza v radu milisekund...")
print(f"Celkem to dela {platba_celkem+int(sprop/platba_celkem)} Kc.")