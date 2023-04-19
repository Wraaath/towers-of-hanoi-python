# Lav pecs med diske
pec_1 = [6, 5, 4, 3, 2, 1]
pec_2 = []
pec_3 = []

# Print starten
print(
    "\nPec 1:", pec_1, 
    "\nPec 2:", pec_2, 
    "\nPec 3:", pec_3
    )

# Lav funktion til at flytte diskene
def move_function(n, source, target, auxiliary):
    if n > 0:
        move_function(n-1, source, auxiliary, target)
        target.append(source.pop())
        print(
            "\nPec 1:", pec_1, 
            "\nPec 2:", pec_2, 
            "\nPec 3:", pec_3
            )
        move_function(n-1, auxiliary, target, source)

# Udfør funktionen
move_function(len(pec_1), pec_1, pec_3, pec_2)