# Oblig nr 2 - frist 17.10.24

# Innlevert av Ingrid Nagell

# Har løst oppgaver under nivå enkel og vanskelig
# Har løst oblig på egenhånd, gjort noen google-søk for å finne helt riktig syntax, for å lete
# gjennom key, value i dictionaries og hvordan split() ble brukt og os.walk() feks.

# Jeg ser at jeg bruker print og ikke return, og at en del funksjoner dermed returnere None når de blir kallet på.
# Har bare ikke orket å fikse det i denne omgang.

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
    "innafor",
    "vispath2",

    # vanskelig
    "finn",

    "vismappe",
    "byttmappe",
    "vistid",
    "tegnrombe",
    "tegnapenboks",
]


# kommandoer oblig 4
def regnut():
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


# jeg kjenner løkker i python litt fra før, så valgte å teste rekursjon igjen, da jeg ikke er særlig vandt til å bruke det.
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


def erTall(verdi, innafor_funksjon) -> bool: # endret denne til å ta valgfri antall args
    """ returnerer True kun hvis alle parametrene er int eller float """
    try:
        float(verdi)
    except:
        print("\nKan ikke konvertere input til tall.\nPrøv igjen.")
        innafor_funksjon()
    else:
        return float(verdi)


def innafor() -> str:
    """ "innafor" som finner ut om et tall er mellom to andre tall. Bruker oppgir
    alle tre tallene. Programmet bruker innafor() fra oblig 3 til å finne svaret,
    og innafor() bruker erTall(). Svaret til bruker (sluttbruker) er "innafor" eller
    "Ikke innafor".
    """
    print("Oppgi input som tall. Du skal oppgi testverdi og grenseverdier.")
    testverdi = erTall(input("Tall som skal testes: "), innafor) # erTall kaller på innafor hvis input ikke representerer ett tall
    fra = erTall(input("Grenseverdi 1: "), innafor)
    til = erTall(input("Grenseverdi 2: "), innafor)
    if testverdi or fra or til != None:
        grenseverdier = [fra, til]
        if min(grenseverdier) <= testverdi <= max(grenseverdier):
            return "Innafor"
    else:
        print("Input er ikke oppgitt som tall")
    return "Ikke innafor"


# vanskelig
def finn():
    """Legg til skallkommandoen "finn" som ber bruker oppgi en søketekst X og et startpunkt.

    Derpå skal programmet gå til startpunktet (en mappe, hvis den finnes) og rekursivt søke
    seg gjennom alle undermappene på jakt etter filer og mapper som har X i navnet.

    Et treff per linje med full sti og filnavn.

    ref: https://www.google.com/search?q=python+search+a+directory+for+a+program
    """
    program = input("Hvilket program ser du etter? Skriv inn deler eller helt navn > ")
    dir = input("Hvilken mappe er øverste mappe som skal søkes i?")

    for dirpath, dirnames, files in os.walk(os.path.abspath(dir)):
        # Her var dte vel egentlig meningen å gjøre dette manuelt med løkke og navigasjon mellom directories,
        # men siden jeg fant walk-funksjonen tok jeg den enkleste veien :-)
        for file in files:
            if program in file:
                print(f"Path: {dirpath} - Filnavn: {file}")


# eldre kommandoer
def vismappe() -> None:
    """Funksjon lar brukeren printe nåværende mappesti"""
    return f"Nåværende mappe: {os.getcwd()}"


def byttmappe() -> None:
    """Funskjon lar brukeren bytte mappe sti.

    Ref. try/except: https://www.w3schools.com/python/python_try_except.asp
    """
    vismappe()
    nymappe = input("Tast inn ny mappesti: ")
    try:
        os.chdir(nymappe)
    except(FileNotFoundError):
        return "Feilet. Sjekk om oppgitt sti er gyldig."
    else:
        print("Suksess! ")
        vismappe()


def tegnrombe(tegn: str, høyde: int, bredde: int) -> str:
    """Romben tegnes av funksjonen tegnrombe (tegn, høyde, bredde). Eksempel: tegnrombe ("*", 3, 2) gir følgende:
        **
         **
          **
    """
    rombe = ""
    for i in range(0, høyde):
        rombe+="\n"+" "*i+f"{tegn}"*bredde
    return(rombe)


def tegnapenboks(tegn: str, høyde: int, bredde: int) -> str:
    """Boksen tegnes av tegnåpenboks (tegn, høyde, bredde).Med argumentene ("+", 4, 4) får vi:
        ++++
        +  +
        +  +
        ++++
    """
    boks = ""
    for i in range(0, høyde):
        if i==0 or i == høyde-1:
            boks += "\n"+f"{tegn}"*bredde
        else:
            boks += "\n"+f"{tegn}"+" "*(bredde-2)+f"{tegn}"
    return(boks)


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


def vistid() -> str:
    """Funksjon returnerer nåværende dato og klokkeslett som tekststreng,
    inkludert beskrivelse.
    ref: https://pynative.com/python-datetime-format-strftime/
    """
    ts = datetime.now()
    formatted_ts = ts.strftime("Nå er det den %d-%m-%Y, klokken %H:%M")
    return formatted_ts


def velkommen() -> str:
    msg = f"""
    -----------------------------------------
        Velkommen til Mitt Skall v{VERSJON}
    -----------------------------------------
    """
    hjelp_msg = hjelp()
    return msg + "\n" + hjelp_msg


kommandoer_dict = {
    "hjelp": hjelp,
    "om": om,

    "regnut": regnut,
    "visfiler2": visfiler2,
    "vismiljø2": vismiljo2,
    "vispath2": vispath2,
    "innafor": innafor,

    "finn": finn,

    "vismappe": vismappe,
    "byttmappe": byttmappe,
    "vistid": vistid,
    "tegnrombe": tegnrombe,
    "tegnapenboks": tegnapenboks,
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
            if tekst_inn == "tegnrombe" or tekst_inn == "tegnapenboks":
                action = kommandoer_dict.get(tekst_inn)
                print("Tast inn dimensjoner")
                tegn = input("Tast inn tegn: ")
                høyde = int(input("Tast inn høyde: "))
                bredde = int(input("Tast inn bredde: "))
                print(action(tegn=tegn, høyde=høyde, bredde=bredde))
            else:
                action = kommandoer_dict.get(tekst_inn)
                print(action())
        else:
            print(f"{tekst_inn} er ikke en gyldig kommando. Tast [hjelp] for å se gyldige kommandoer.")


# initiering av programmet
if __name__ == "__main__":
    main()

    # for dev:
    # finn()
    # print(innafor())
    # print(40 % 20)
