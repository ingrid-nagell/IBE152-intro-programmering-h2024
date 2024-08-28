# Oblig nr 2 - frist 19.09.24
# Innlevert av Ingrid Nagell

# Modulimport:
from datetime import datetime

# Konstanter
VERSJON = 0.2

KOMMANDOER = [
    "hjelp",
    "om",
    "vistid",
    "tegnrombe",
    "tegnapenboks",
]


# Kommandoer
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
    return f"mittskall.py Ingrid Nagell, v{VERSJON}, Lisens: None"

def hjelp() -> str:
    """Funksjon returnerer alle tilgjengelige kommandoer for å hjelpe brukeren videre."""
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
    "vistid": vistid,
    "tegnrombe": tegnrombe,
    "tegnapenboks": tegnapenboks,
}


def mittskall():
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


# Initiering av programmet
if __name__ == "__main__":
    # print(tegnapenboks("x", 5, 5))
    mittskall()
