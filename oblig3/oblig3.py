# IBE152 høst 2024, oblig 3, Ingrid Nagell, 02. september 2024

# referanser:
# Gjennomført det meste på egenhånd, men med tidligere erfaring med grunnleggende python

# Googlet:
# "python optional args" og brukte denne stackoverflow: https://stackoverflow.com/questions/9539921/how-do-i-define-a-function-with-optional-arguments
# "python median function" og fant pakken og funksjonen statistics.median() fra første overskrift i søket.

# pakker:
from statistics import median


# ---------------------- deloppgave 1
print("\n--------\n- DEL1 -\n--------")

def erTall (*args) -> bool: # endret denne til å ta valgfri antall args
    """ returnerer True kun hvis alle parametrene er int eller float """
    for e in args:
        if type(e) not in [int, float]:
            return False
    return True

print(f"\nTester erTall: {erTall(2, '4', 5.5)}")
print(f"Tester erTall: {erTall(2, 5.5)}")

def innafor (x, fra, til) -> bool:
    """ returner True kun hvis x er mellom fra og til på tallinjen."""
    grenseverdier = [fra, til]
    if erTall(x):
        if min(grenseverdier) <= x <= max(grenseverdier):
            return True
    return False

x=50.5
print ("\ntest av innafor:")
print (innafor(x,40,80)) # True
print (innafor(x,70,30)) # True
print (innafor(x,x,x)) # True
print (innafor(x,x-0.1,x-0.2)) # False
print (innafor(x,2*x,0.5*x)) # True
print (innafor("x",2*x,0.5*x)) # False


# ---------------------- deloppgave 2
print("\n--------\n- DEL2 -\n--------")
def countdown(n: int) -> None: # original fra boka
    """ skriver ut heltallene fra n til 0"""
    if n <= 0:
        print("Blastoff")
    else:
        print(n)
        countdown(n-1)
print("\nCOUNTDOWN FRA BOKA MED RECURSION:")
countdown(5)

# def countdownOddeX(n: int) -> None:
#     """skriver ut oddetallene fra n ned til 0"""
#     logikk = -1 if n > 0 else 1 # uttrykk for å få riktig min verdi og riktig inkrementell verdi, (begge parmeterne skal være 1 hvis n er negativ og -1 hvis n er positiv)
#     for n in range(n, logikk, logikk): # teller ned til 0 hvis n er positiv, teller opp til 0 hvis n er negativ
#         if n % 2 != 0:
#             print(n)

def countdownOdde(n):
    if n <= 0:
        print("Blastoff")
    else:
        if n % 2 != 0:
            print(n)
        countdownOdde(n-1)

print ("\ntest countdownOdde(6):")
countdownOdde(6)

# def countdownPar(n: int) -> None:
#     """skriver ut partallene fra n ned til 0"""
#     logikk = -1 if n > 0 else 1 # uttrykk for å få riktig min verdi og riktig inkrementell verdi, (begge parmeterne skal være 1 hvis n er negativ og -1 hvis n er positiv)
#     for n in range(n, logikk, logikk): # teller ned til 0 hvis n er positiv, teller opp til 0 hvis n er negativ
#         if n % 2 == 0 and n != 0:
#             print(n)

def countdownPar(n):
    if n <= 0:
        print("Blastoff")
    else:
        if n % 2 == 0:
            print(n)
        countdownPar(n-1)

print ("\ntest countdownPar(6):")
countdownPar(6)

# def countdown2(n: int, parFlagg: bool) -> None:
#     """ skriver ut heltallene fra n til 0.
#     hvis parFlagg er True skrives kun partallene, ellers kun oddetallene"""
#     logikk = -1 if n > 0 else 1 # uttrykk for å få riktig min verdi og riktig inkrementell verdi, (begge parmeterne skal være 1 hvis n er negativ og -1 hvis n er positiv)
#     for n in range(n, logikk, logikk): # teller ned til 0 hvis n er positiv, teller opp til 0 hvis n er negativ
#         if parFlagg:
#             if n % 2 == 0 and n != 0:
#                 print(n)
#         else:
#             if n % 2 != 0:
#                 print(n)


def countdown2(n, parFlagg):
    if n <= 0:
        print("Blastoff")
    else:
        if parFlagg:
            if n % 2 == 0:
                print(n)
        else:
            if n % 2 != 0:
                print(n)
        countdown2(n-1, parFlagg)

print ("\ntest countdown2(6,True):")
countdown2 (6, parFlagg=True)
print ("test countdown2(6,False):")
countdown2 (6, False)


# ---------------------- deloppgave 3
print("\n--------\n- DEL3 -\n--------")

def boksInnenfor (a: int, b: int, c: int, x: int, y: int, z: int) -> bool:
    """ a,b,c er dimensjon på boks (usortert)
    x,y,z er maksmålet (x >= y >= z)
    svarer True hvis boks får plass innenfor maksmålet """
    maal_pakke = [a, b, c]
    if max(maal_pakke) > x or median(maal_pakke) > y or min(maal_pakke) > z:
        return False
    return True

print ( "\ntest boksInnenfor(90, 20, 50, 100, 30, 20):" )
print ( boksInnenfor(90, 20, 50, 100, 30, 20))
print ( "test boksInnenfor(10, 20, 30, 30, 20, 10):")
print ( boksInnenfor(10, 20, 30, 30, 20, 10) )
