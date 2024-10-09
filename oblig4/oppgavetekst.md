Her skal det øves på kapittel 7 til 10.  Lever kun 1 fil som heter mittskall4.py.

Greit om dere jobber sammen (max 3). Lever individuelt (har ikke aktivert gruppeinnlevering). Skriv navnene inn som Python-kommentar (# Skrevet av A og B).

Du kan bruke alle hjelpemidler. Legg inn referanser som Python-kommentar hvis du kopierer kode helt eller delvis, f.eks. # hentet fra <url>. Gjelder også dialoger du har hatt med AI-er. Hvis du har fått vesentlig hjelp av noen skriver du # med hjelp fra NN

Oppgavene er gradert (enklest, middels, vanskelig) Du bestemmer selv om du vil gjøre en eller flere.  Alle må minimum ha utført den enkleste. Hvis du forsøker de andre to bestemmer du selv hvor mange deloppgaver du vil gjøre.

Ikke sitt mer enn 15 minutt før du tar en tenkepause eller spør noen.  Se Hjelp til programmering.



## ENKLEST:  LITT MERE I SKALLET

Legg til følgende kommandoer i skallet du har bygd så langt.

"regnut" ber bruker skrive et regneuttrykk, som så evalueres (med eval()) og svar eller feilmelding skrives ut. Hvis bruker skriver "2+3" skal programmet svare "5". Skal ikke krasje. Bruk f.eks. try ... except Exception as e: print("Feil", e) for å unngå krasj.

"visfiler2" skal forbedres til å vise filene linjevis (en fil per linje).  For hver 20de linje skal vising pauses og det står "Har vist X av Y filer. Trykk Enter for å gå videre".  X og Y er heltall.

"vismiljø2" er som "vismiljø", men endres til å vise linjevis, en variabel per linje, som i "<var> har verdien <verdi>"

"vispath2" er som "vispath", men hver mappe i PATH vises på egen linje. Hint: split(";")

"innafor" som finner ut om et tall er mellom to andre tall. Bruker oppgir alle tre tallene. Programmet bruker innafor() fra oblig 3 til å finne svaret, og innafor() bruker erTall(). Svaret til bruker (sluttbruker) er "innafor" eller "Ikke innafor".



## MIDDELS:  EKSEKVERING

Legg til følgende funksjoner i skallet ditt.

"finnprogram" ber bruker om et programnavn (X) og viser alle mappene der et ligger et eksekverbart program X. Avgrens letingen til mappene i PATH.  Ignorer mapper i PATH som ikke finnes. Et treff per linje med full sti og filnavn.   Hvis jeg skriver "notepad.exe" blir det nok kun 1 treff, men andre programnavn kan man finne flere versjoner av på ulike steder.

"åpne" vil be brukeren om å oppgi navn på fil som skal åpnes. Så åpnes filen med et egnet program. Hvis bruker oppgir "stråhatt.jpg", vil den åpnes av egnet bildeviser, "studieplan.pdf" åpnes av egnet PDF-viser. Se gjerne min dialog med ChatGPTLinks to an external site. for hint.



## VANSKELIG:  SØKING

Legg til skallkommandoen "finn" som ber bruker oppgi en søketekst X og et startpunkt. Derpå skal programmet gå til startpunktet (en mappe, hvis den finnes) og rekursivt søke seg gjennom alle undermappene på jakt etter filer og mapper som har X i navnet.   Et treff per linje med full sti og filnavn.
