Dette er oblig 5.  Dette er den siste som legges ut i IBE152. Du må ha 4 av 5 obliger godkjent for å få ta eksamen. Om du har de 4 første godkjent trenger du ikke gjøre oblig 5. Mangler du 1 av de 4 første, trenger du oblig 5 godkjent.

Her skal det øves på filer og lister som i hovedsak ble introdusert i kapittel 9 og 10. Lever kun 1 fil som heter mittskall5.py.

Greit om dere jobber sammen (max 3). Lever individuelt (har ikke aktivert gruppeinnlevering). Skriv navnene inn som Python-kommentar (# Skrevet av A og B).

Du kan bruke alle hjelpemidler. Legg inn referanser som Python-kommentar hvis du kopierer kode helt eller delvis, f.eks. # hentet fra <url>. Gjelder også dialoger du har hatt med AI-er. Hvis du har fått vesentlig hjelp av noen skriver du # med hjelp fra NN

Oppgavene er gradert (enklest, middels, vanskelig) Du bestemmer selv om du vil gjøre en eller flere.  Alle må minimum ha utført den enkleste. Hvis du forsøker de andre to bestemmer du selv hvor mange deloppgaver du vil gjøre.

Ikke sitt mer enn 15 minutt før du tar en tenkepause eller spør noen.  Se Hjelp til programmering.



ENKEL:  TRENE PÅ TELLERE OG SKRIVING TIL FIL

Vi ønsker å lagre alle kommandoer som er skrevet inn. Du skal utvide skallet ditt slik at alle kommandoer lagres til tekstfilen mittskall.log. Hver gang en ny kommando skrives, skal programmet legge følgende linje til filen:

<tidspunkt>  <kommando>
Bruk time.time() som tidspunkt.  Det gir antall sekunder siden 1. januar 1970 kl 0:0.0.   Her er eksempel som viser logfil med 4 linjer:

PS C:\users\kd\documents\ibe152\h24> type mittskall.log
1727680052.3586853 hjelp
1727680054.4310753 om
1727680055.5021412 vistid
1727680056.6946135 avslutt
Hver linje inneholder en inntastet kommando med tidspunkt.  Kronologisk.

Sjekk at logfilen blir laget og får lagt til nye tidspunkt og kommandoer etter hvert.

Ved "avslutt" skal programmet skrive:  "Takk og farvel! La til <x> kommandoer i logfilen", der x er antall kommandoer som brukeren skrev inn siden programmet startet. Dette krever en kommandoteller.  Her er eksempel:

mittskall >avslutt
Takk og farvel!
La til 11 kommandoer i logfilen
Om du har lyst å trene på innlesing av fil kan du se på neste del (middels).



MIDDELS:  TRENE PÅ LESING TIL FIL OG INPUTKONTROLL

Når programmet starter skal det kalle på funksjonen les_logfil().  Denne skal lese gjennom logfilen og skrive "les_logfil: antall linjer lest inn er <n>". Dette krever en linjeteller. Det er greit om du (som i eksempelet under) skriver ut hver innleste, det gjør det jo lettere å se om innlesingen virker.

Det er tre krav/kriterier til hver linje. Det skal være eksakt to felt, adskilt av blanke tegn. Det første feltet skal være et desimaltall (tidspunktet) og det andre skal være en streng (kommandoen).  Hvis programmet oppdager feil på en linje i logfilen (ved innlesing), skal det skrive "Feil i logfilen på linje <n>" og linjen skal ignoreres.

Legg inn feil i loggfilen for å sjekke at feilsjekkingen din faktisk virker for de 3 kriteriene.

Her er eksempel, der innleste linjer vises med et par feilmeldinger underveis:

PS C:\users\kd\documents\ibe152\h24> python mittskall5.py
les_logfil: leste inn linje nr.  1 : 1727684701.0976758 hjelp
les_logfil: leste inn linje nr.  2 : 1727684714.5533595 regnut
les_logfil: leste inn linje nr.  3 : 1727684722.1055923 finnprogram
les_logfil: leste inn linje nr.  4 : 1727684816.3232172 statiskboks
les_logfil: leste inn linje nr.  5 : 1727684832.1718252 pnyeste
les_logfil: feil type i tidspunkt på linje 6 :  could not convert string to float: 'x727684834.5461948'
les_logfil: leste inn linje nr.  7 : 1727684924.9246335 pnyeste
les_logfil: Feil antall felt på linje 8
les_logfil: leste inn linje nr.  9 : 1727685461.0765605 finnprogram
les_logfil: antall linjer lest inn er 9 - Antall kommandoer lest inn er 7

Velkommen til Mitt Skall v0.01.  Skriv "om" eller "hjelp" for mer info
mittskall >
Legg merke til at programmet også skal skrive ut hvor mange kommandoer som ble godkjent og lest inn (7 i eksemplet over).

Generell teknikk for å gjøre noe uten å krasje: try: ... except Exception as e: print("Feil...", e).

Det skal ikke lages noe automatikk for å forsøke å reparere på feil i logfilen. Reparasjon må eventuelt gjøres manuelt i en teksteditor.



VANSKELIG:  LISTE-TRENING

Dette er utvidelse av den middels vanskelige delen. Når programmet starter, skal det også bygge opp en intern liste som heter kmdlog. Denne listen er initielt tom. Hver innlest kommando legges til listen kmdlog, for eksempel med et tuple ( tidspunkt, kmd).  Etter innlesingen vil kmdlog[0] inneholde eldste kommando og kmdlog[-1] ferskeste kommando.

Hver nye kommando skal legges til kmdlog (i tillegg til at den skrives til fil, det du gjorde i del 1). Den skal altså holdes oppdatert under kjøring.

Når bruker skriver "pnyeste" vil programmet be bruker oppgi n og vise de n siste (ferskeste) kommandoene i listen.

Skriver man "peldste" skal bruker oppgi n og programmet vise de n første (eldste) kommandoene.

Utskriften skal vise kommandonummeret slik at brukeren kan referere til for eksempel kommando nummer 17.

I tillegg til å kunne skrive "p" for å få utført siste kommando, skal bruker kunne be om en hvilken som helst av de tidligere kommando. Hvis brukeren skriver "p <n>" utføres kommando nummer n, der n=0 betyr eldste, n=1 betyr nest eldste, n=-1 betyr nyeste (siste), -2 betyr nest siste.  Her er altså <n> det samme som posisjonen i kmdlog, det forenkler oppgaven litt.

Her er eksempel:

mittskall >peldste
   Viser de N eldste kommandoer. Oppgi N:3
0 1727684701.0976758 hjelp
1 1727684702.0091004 om
2 1727684703.06433 vistid
mittskall >p 2
2024-09-30 10:38:09.996908
...
mittskall >pnyeste
   Viser de N nyeste kommandoer. Oppgi N:10
15 1727685343.7468967 finnprogram
16 1727685461.0765605 finnprogram
17 1727685485.5411777 peldste
18 1727685489.996908 vistid
19 1727685600.9110923 vistid
20 1727685604.0871623 finnprogram
21 1727685613.3913126 visfiler
22 1727685614.7187011 vispath
23 1727685616.3505456 visfiler2
24 1727685624.5193596 pnyeste
mittskall >p -4
['code', 'code-tunnel.exe', 'code.cmd', 'mittskall.log']
mittskall >
"p -4" viste fjerde siste kommando, som var "visfiler".
