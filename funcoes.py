def metros():
    medida = float(input("um distância em metros: "))
    cm = medida * 100
    mm = medida * 1000
    print(f"a medida de {medida}m corresponde a {cm}cm e {mm}mm!")

def temperatura():
    c = float(input("informe a temperatura em °C: "))
    f = 9 * c / 5 + 32
    print(f"A temperatura de {c}°C corresponde a {f}°F!: ")

def velocidade():
    km_h = float(input("informe quantos Km/h: "))
    ms = km_h / 3.6
    print(f"{km_h}Km/h em M/s é {ms:.2f}M/s ")

def peso():
    kg = float(input("informe o peso: "))
    lb = kg * 2.2046
    print(f"O seu peso em libras é {lb:.2f}lb")