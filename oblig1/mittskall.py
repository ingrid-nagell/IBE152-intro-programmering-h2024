# Oblig nr 1 - frist 05.09.24
# Innlevert av Ingrid Nagell

# Øvrige referanser jeg har brukt:
# Docstring conversions: https://peps.python.org/pep-0257/

# Modulimport:
from datetime import datetime
import math
import os

# Konstanter
VERSJON = 0.01

KOMMANDOER = [
    "hjelp",
    "om",
    "vistid",
    "vismappe",
    "byttmappe",
    "visfiler",
    "vismiljø",
    "visbrukernavn",
    "vispath",
    "nyprompt",
    "hvorlenge",
    "kakeplanlegger",
]

# Kommandofunskjoner
def hjelp() -> None:
    """Funksjon returnerer alle tilgjengelige kommandoer for å hjelpe brukeren videre."""
    hjelp_innhold = "Kommandoer som støttes: "
    for kommando in KOMMANDOER:
        hjelp_innhold += f"\n\t*{kommando}"
    print(hjelp_innhold)

def om() -> None:
    print(f"mittskall.py Ingrid Nagell, v{VERSJON}, Lisens: None")

def vistid() -> None:
    """Funksjon returnerer nåværende dato og klokkeslett som tekststreng,
    inkludert beskrivelse.
    ref: https://pynative.com/python-datetime-format-strftime/
    """
    ts = datetime.now()
    formatted_ts = ts.strftime("Nå er det den %d-%m-%Y, klokken %H:%M")
    print(formatted_ts)

def vismappe() -> None:
    """Funksjon lar brukeren printe nåværende mappesti"""
    print(f"Nåværende mappe: {os.getcwd()}")

def byttmappe() -> None:
    """Funskjon lar brukeren bytte mappe sti.

    Ref. try/except: https://www.w3schools.com/python/python_try_except.asp
    """
    vismappe()
    nymappe = input("Tast inn ny mappesti: ")
    try:
        os.chdir(nymappe)
    except(FileNotFoundError):
        print("Feilet. Sjekk om oppgitt sti er gyldig.")
    else:
        print("Suksess! ")
        vismappe()

def visfiler() -> None:
    """Funskjonen printer tilgjengelige filer."""
    print(f"Filer tilgjengelig i mappen: {os.listdir()}")

def vismiljo() -> None:
    """Funksjonen printer informasjon om miljø."""
    print(os.environ) #TODO: Print ved hjelp av løkke for prettyprint

def visbrukernavn() -> None:
    """Funskjeonen printer brukernavn fra miljøvariabler."""
    print(os.environ['USERNAME']) #TODO: Burde hatt try/exceptblokk her og

def vispath() -> None:
    """Funksjonen printer søkesti fra miljøvariabler."""
    print(os.environ['PATH']) # TODO: Burde hatt try/exceptblokk her og
    # TODO: kunne laget en funksjon som ber brukeren velge variabel fra miljø

def nyprompt(gammel_prompt) -> str:
    ny_prompt = input("Oppgi ny prompt ([r] for å resette til opprinnelig prompt): ")
    if ny_prompt.lower() == "r":
        return "----\nSkriv inn kommando (tast [a] eller [avslutt] for å ende programmet):\n"
    commit_ny_prompt = input(f"Vil du sette [{ny_prompt}] som ny prompt? [ja]/[nei] ").lower()
    if commit_ny_prompt in ["ja", "j"]:
        return ny_prompt + " "
    else:
        return gammel_prompt

def hvorlenge(start: datetime) -> None:
    """Funksjonen printer antall sekunder programmet har kjørt hittil."""
    naa = datetime.now()
    delta = naa - start
    print(f"Programmet har kjørt i: {round(delta.total_seconds())} sekunder.")

def kakeplanlegger() -> None:
    """Funksjonen printer antall kaker som er nødvendig"""
    print("Velkommen til kakeplanleggeren. Her kan du beregne hvor mange kaker du trenger å bake!")
    antall_gjester = int(input("Hvor mange gjester skal spise kake?"))
    kakestykker = int(input("Hvor mange stykker gir en kake?"))
    antall_kaker = math.ceil(antall_gjester / kakestykker)
    print(f"Du trenger {antall_kaker} kaker for å mette {antall_gjester} gjester!\nGod baking!🎂")

kommandoer_dict = {
    "hjelp": hjelp,
    "om": om,
    "vistid": vistid,
    "vismappe":vismappe,
    "byttmappe": byttmappe,
    "visfiler":visfiler,
    "vismiljo": vismiljo,
    "visbrukernavn": visbrukernavn,
    "vispath": vispath,
    "kakeplanlegger": kakeplanlegger,
}


# Hovedfunksjon
def mittskall():
    """Funksjon som samler all funskjonalitet i ett program.
    """
    program_start = datetime.now()
    avslutt = False
    print(f"""
    -----------------------------------------
        Velkommen til Mitt Skall v{VERSJON}
    -----------------------------------------
    """)
    print(hjelp())
    prompt = "----\nSkriv inn kommando (tast [a] eller [avslutt] for å ende programmet):\n"

    while avslutt == False:
        tekst_inn = input(prompt).lower()
        if tekst_inn in ('a', 'avslutt'):
            print("Takk og farvel!")
            avslutt = True
        elif tekst_inn in kommandoer_dict.keys():
            action = kommandoer_dict.get(tekst_inn)
            action()
        elif tekst_inn == "hvorlenge":
            hvorlenge(program_start)
        elif tekst_inn == "nyprompt":
            prompt = nyprompt(prompt)
        else:
            print(f"{tekst_inn} er ikke en gyldig kommando. Tast [hjelp] for å se gyldige kommandoer.")

# Initiering av programmet
if __name__ == "__main__":
    mittskall()
