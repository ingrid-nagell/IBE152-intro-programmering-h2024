Her skal det øves på kapittel 5 og 6. Lever minst 1 av deloppgavene.

Lever kun 1 fil som heter oblig3.py, den skal være basert på malfilen for oblig 3 som du finner under Filer. Der finner du også ønsket output av testkjøringene i egen txt-fil.

Når vi skal godkjenne innleveringen vil vi kjøre programmet oblig3.py og se hva som skrives ut.

Greit om dere jobber sammen (max 3). Lever individuelt (har ikke aktivert gruppeinnlevering). Skriv navnene inn som Python-kommentar (# Skrevet av A og B).

Du kan bruke alle hjelpemidler. Legg inn referanser som Python-kommentar hvis du kopierer kode helt eller delvis, f.eks. # hentet fra <url>. Gjelder også dialoger du har hatt med AI-er. Hvis du har fått vesentlig hjelp av noen skriver du # med hjelp fra NN

Oppgavene er gradert (enklest, middels, vanskelig) Du bestemmer selv om du vil gjøre en eller flere.  Alle må minimum ha utført den enkleste. Hvis du forsøker de andre to bestemmer du selv hvor mange deloppgaver du vil gjøre.

Ikke sitt mer enn 15 minutt før du tar en tenkepause eller spør noen.  Se Hjelp til programmering.

## Deloppgave 1 (enklest)
I denne oppgaven får du øvd på å lage boolsk funksjon.  Du får også en anledning til å øve på inkrementell utvikling.

Lag den boolske funksjonen innafor(x, fra, til) som svarer False, bortsett fra hvis x er mellom de to parametrene fra og til.  NB: Parameter fra trenger ikke være lavere enn parameter til, det kan også være likt eller mindre, slik vist i testlinje 1 og 2 under der vi tester området 40 til 80 og 70 til 30.

Her er et testprogram, hentet fra malfilen (nevnt over):

x=50
print (innafor(x,40,80))         # skal gi True i dette eksempelet
print (innafor(x,70,30))         # skal gi True i dette eksempelet
print (innafor(x,x,x))           # skal gi True uansett verdi av x
print (innafor(x,x-0.1,x-0.2))   # skal gi False uansett verdi av x
print (innafor(x,2*x,0.5*x))     # skal gi True uansett verdi av x
Mitt forslag til arbeidsgang er basert på kapittel 6.2 om incremental development

Prøv først med det Downey kaller et outline of the function, altså et minimalt skall med hode og kropp som bare returnerer noe, for eksempel False.  Sjekk at skallet virker ved å bekrefte at innafor(1,1,1) svarer False.
Legg til en print-setning som skriver ut de tre lokale parametrene. Sjekk ved å skrive innafor(3,2,1) og se parametrene skrevet ut på skjermen. Slike print-setninger er eksempel på det Downey kaller scaffolding ("stillasbygging" på norsk) og fjernes før leveranse.
Utvid med en enkel test som for eksempel return (fra>til), som svarer True kun hvis fra er større enn til. Sjekk at den virker ved å kjøre innafor(3,7,8) og innafor(3,8,7).
Utvid funksjonen inntil den oppfører seg som ønsket. Spør om du står fast.
Resten av deloppgave 1 er en utvidelse som legger inn en beskyttelse (engelsk: guardian, se kapittel 6). Den skal beskytte oss mot feil i parametrene.  innafor skal bruke en boolsk funksjon til dette.

Lag den boolske funksjonen erTall(a,b,c) som avgjør om de tre parametrene a, b og c faktisk er tall og i så fall svarer True.  Du kan bruke isinstance( ) for typetesting, slik nevnt i kapittel 6.  En annen test er med funksjonen type, som i type(x)==int. Den er beskrevet i læreboken.

Kun heltall og desimaltall er å regne som tall i denne oppgaven.

innafor(x,y,z) skal altså kalle på erTall for hjelp til typejsekk, og innafor skal svare False hvis erTall(x,y,z) svarer False.  Her er en test:

print (innafor("kake",2*x,0.5*x)) # skal gi False uansett verdi av x
Her er en variant av pseudokode:

innafor(x,fra,til):
    hvis not erTall(x,fra,til): return False
    ellers: svar True kun hvis x er mellom fra og til
(slutt deloppgave 1)

## Deloppgave 2 (middels)
Denne oppgaven gir deg øvelse i rekursjon, betingelser, heltallsdivisjon og generalisering.

Ta utgangspunkt i funksjonen countdown(n) fra kapitlet om rekursjon i boka. Sjekk at den virker for både negative og positive verdier av n.

Dessverre skriver den ut alle heltallene.  Det vi trenger er en nedtelling som kun skriver ut partall eller oddetall.  Og vi må kunne velge om vi vil ha partall eller oddetall.

Lag først en funksjon countdownOdde(n) som er ekspert på å skrive oddetall.  countdownOdde(6) skriver ut 5, 3 og 1.  Dette krever flere tester, kanskje det er nyttig med en nested conditional slik beskrevet i boken.

Lag så en funksjon countdownPar(n) som gjør det motsatte.  countdownPar(6) skriver ut 6, 4 og 2.

Lag avslutningsvis en generalisering countdown2(n, parFlagg) som skriver ut partallene hvis parFlagg er True og oddetallene hvis parFlagg er False.  Denne skal gjøre alt arbeidet selv, altså IKKE kalle på de to foregående funksjonene.

countdown2(10,True) vil skrive ut 10, 8, 6, 4 og 2.  countdown2(3,False) vil skrive ut 3 og 1.

## Deloppgave 3 (vanskeligst)
Du har fått en jobb av Posten. Kundene skal kunne få avgjort om en boksformet pakke er innenfor gitte maksimumsmål.  Pakkens størrelse og maksimumsmålet angis med tre verdier; bredde, dybde og høyde.

Du skal lage den boolske funksjonen boksInnenfor(a,b,c,x,y,z) som sjekker om pakkens mål (a,b,c) er innenfor maksmålet (x,y,z). Vi vet at maksmålet er sortert, slik at x >= y >= z.  Kunden kan oppgi pakkens mål (a, b og c) i hvilken som helst rekkefølge.

Hint: En måte å avgjøre dette på, er å først sjekke pakkens største side mot maksmålets største (som er x), dernest om nødvendig, sjekke pakkens mellomste mot y, og om nødvendig, til sist sjekke pakkens minste verdi mot z.

Eksempel:

boksInnenfor(90, 20, 50, 100, 30, 20) gir False fordi pakkens mellomste verdi (50) overgår maksmålets mellomste verdi (30).

boksInnenfor(10, 20, 30, 30, 20, 10) gir True fordi pakken akkurat får plass.

(slutt oblig 3)
