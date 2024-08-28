
while True:
    output = lambda x : "Takk og farvel!" if x=="avslutt" else f"kommando: {x}"
    print(output(input('Tast inn kommando: ')))
