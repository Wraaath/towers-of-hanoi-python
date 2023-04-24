import time

# Lav pecs med diske
peg_1 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
peg_2 = []
peg_3 = []

# Print starten
print(
    "\nPeg 1:", peg_1, 
    "\nPeg 2:", peg_2, 
    "\nPeg 3:", peg_3
    )

# Lav funktion til at flytte diskene
def move_function(n, source, target, auxiliary):
    if n > 0:
        move_function(n-1, source, auxiliary, target)
        target.append(source.pop())
        print(
            "\nPeg 1:", peg_1, 
            "\nPeg 2:", peg_2, 
            "\nPeg 3:", peg_3
            )
        move_function(n-1, auxiliary, target, source)

# Udfør funktionen
start = time.time()
move_function(len(peg_1), peg_1, peg_3, peg_2)
end = time.time()

time = (end-start) * 1000
print("Time (ms):", time)
