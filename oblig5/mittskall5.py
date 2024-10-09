# Oblig nr 5

# Innlevert av Ingrid Nagell

# Har løst oblig på egenhånd, gjort noen google-søk for å finne helt riktig syntax.

# Modulimport:
from datetime import datetime
from operator import contains
import os



# Konstanter
VERSJON = 4.0

KOMMANDOER = [
    "hjelp",
    "om",

    # enkel ob.4
    "regnut",
    "visfiler2",
    "vismiljø2",
    "vispath2",
]


# kommandoer i skallet, tidligere oblig'er
def om() -> str:
    return f"mittskall.py Ingrid Nagell, for oblig v{VERSJON}, Lisens: None"


def hjelp() -> str:
    """ Funksjon returnerer alle tilgjengelige kommandoer for å hjelpe
    brukeren videre.
    """
    hjelp_innhold = "Kommandoer som støttes: "
    for kommando in KOMMANDOER:
        hjelp_innhold += f"\n\t*{kommando}"
    return hjelp_innhold


def velkommen() -> str:
    msg = f"""
    -----------------------------------------
        Velkommen til Mitt Skall v{VERSJON}
    -----------------------------------------
    """
    hjelp_msg = hjelp()
    return msg + "\n" + hjelp_msg


def regnut() -> str:
    """"regnut" ber bruker skrive et regneuttrykk, som så evalueres
    (med eval()) og svar eller feilmelding skrives ut. Hvis bruker
    skriver "2+3" skal programmet svare "5". Skal ikke krasje. Bruk
    f.eks. try ... except Exception as e: print("Feil", e) for å unngå
    krasj.
    """
    uttrykk = input("Skriv inn et regneuttrykk, feks 2 + 3:\n>")
    try:
        resultat = eval(uttrykk)
    except:
        return uttrykk + " er ikke et gyldig regneuttrykk"
    else:
        return f"Du skrev inn: {uttrykk}, resultatet er {resultat}"


def visfil(fil_nr, filer):
    """Støttefunksjon til visfiler2, da jeg ønsket å prøve rekursjon igjen
    siden jeg ikke er så godt kjent med det fra før.
    """
    if fil_nr >= len(filer):
        print("Alle filer er vist")
    else:
        if fil_nr > 0 and (fil_nr+1) % 20 == 0:
            if input(f"Har vist {fil_nr} av {len(filer)} filer. Trykk Enter for å gå videre") != "":
                return False # kanskje ikke beste måten å gjøre det på? Men slipper en ekstra else blokk med dobbel print statement
        print(f"Fil {fil_nr+1}:, {filer[fil_nr]}")
        visfil(fil_nr+1, filer)


def visfiler2():
    """"visfiler2" skal forbedres til å vise filene linjevis (en fil
    per linje).  For hver 20de linje skal vising pauses og det står
    "Har vist X av Y filer. Trykk Enter for å gå videre".  X og Y er
    heltall.
    """
    # os.chdir("C:\\Users\\G020772") #
    filer = os.listdir()
    fil_nr = 0
    visfil(fil_nr, filer)


def vismiljo2():
    """"vismiljø2" er som "vismiljø", men endres til å vise linjevis, en variabel per linje,
    som i "<var> har verdien <verdi>"

    ref: https://www.geeksforgeeks.org/python-os-environ-object/
    Her leste jeg at man kan pakke os.environ inn i dict() funsksjonen som endrer objektet til
    en dictionary isteden for et 'os._Environ'-objekt - sjekket med print(type(os.environ)).
    """
    miljo_dict = dict(os.environ)
    for k, v in miljo_dict.items():
        print(f"{k} har verdien {v}")


def vispath2():
    """ "vispath2" er som "vispath", men hver mappe i PATH vises på egen linje.
    Hint: split(";")
    """
    for e in os.environ['PATH'].split(";"):
        print(e)


# kommandoer i skallet, oblig 5
def kommandoteller(antall_kommandoer):
    return antall_kommandoer






# main app
kommandoer_dict = {
    "hjelp": hjelp,
    "om": om,

    "regnut": regnut,
    "visfiler2": visfiler2,
    "vismiljø2": vismiljo2,
    "vispath2": vispath2,
}

def main():
    """Funksjon som samler all funskjonalitet i ett program.
    """
    print(velkommen())
    prompt = "----\nSkriv inn kommando (tast [a] eller [avslutt] for å ende programmet):\n"

    while True:
        tekst_inn = input(prompt).lower()
        if tekst_inn in ('a', 'avslutt'):
            print("Takk og farvel!")
            break
        elif tekst_inn in kommandoer_dict.keys():
            action = kommandoer_dict.get(tekst_inn)
            print(action())
        else:
            print(f"{tekst_inn} er ikke en gyldig kommando. Tast [hjelp] for å se gyldige kommandoer.")

