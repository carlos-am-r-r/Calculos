
## ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦
## autor = Carlos Adrian
## ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦


## ╞═════𖠁𐂃𖠁═════╡
## seleção de tela
## ╞═════𖠁𐂃𖠁═════╡

start = int(input("▐░░░░░░░░░░░░░░░░▌\nSelecione o programa.\n▐░░░░░░░░░░░░░░░░▌\n\n"
                  "1 - Esfera.\n2 - Água.\n3 - Distância.\n4 - Classificação.\n5 - Peso.\n"))

intro = '⠂⠄⠄⠂⠁⠁⠂⠄⠄⠂⠁⠁⠂⠄⠄⠂ ⠂⠄⠄⠂☆\nVocê escolheu:'

# ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦
# Primeiro problema: Esfera
# ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦

if start == 1:
    print(f"{intro} Esfera.\n") #saída
    raio = float(input('Insira o raio da esfera.\n')) #entrada
    volume = (raio ** 3) * 4 * 3.1415 / 3 #calculo
    print(f'Raio: {raio}\nVolume: {volume}') #saída

# ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦
# Segundo problema: Água
# ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦

if start == 2:
    print(f"{intro} Água.\n") #saída
    Peso = float(input('Insira o peso do indivíduo em quilogramas.\n')) #entrada
    Agua = Peso * 0.03 #calculo
    print(f'Peso: {Peso}\nDose ideal: {Agua}') #saída

# ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦
# Terceiro problema: Distância
# ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦

if start == 3:
    print(f"{intro} Distância.\n")
    X1 = float(input('Insira o valor X do primeiro ponto.\n')) #entrada
    Y1 = float(input('Insira o valor Y do primeiro ponto.\n')) #entrada
    X2 = float(input('Insira o valor X do segundo ponto.\n')) #entrada
    Y2 = float(input('Insira o valor Y do segundo ponto.\n')) #entrada
    dist = ((X1 - X2)**2 + (Y1 - Y2)**2) ** (1/2) #calculo
    print(f'Ponto 1: ({X1}, {Y1})\nPonto 2: ({X2}, {Y2})\n'
          f'Distância entre os pontos: {dist}') #saída

# ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦
# Quarto problema: Ordem
# ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦

if start == 4:
    print(f"{intro} Classificação.\n")
    A = int(input('Insira o primeiro valor.\n')) #entrada
    B = int(input('Insira o segundo valor.\n')) #entrada
    if A > B: #calculo
        print(f'Ordem crescente: {B}, {A}.') #saída
    else: #calculo
        print(f'Ordem crescente: {A}, {B}.') #saída

# ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦
# Quinto problema: Peso
# ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦

if start == 5:
    print(f"{intro} Peso.\n")
    Ask = int(input('Selecione o sexo.\n1 - Masculino\n2 - Feminino\n')) #entrada
    Altura = float(input('selecione a altura em metros.\n')) #entrada
    if Ask == 1: #calculo
        ideal = (72.7 * Altura) - 58 #calculo
    elif Ask == 2: #calculo
        ideal = (62.1 * Altura) - 44.7 #calculo
    else:
        ideal = 'erro.'
        print('entrada incorreta')
    print(f'Peso ideal: {ideal}') #saída

# ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦
# Fim do programa
# ✦ . 　⁺ 　 . ✦ . 　⁺ 　 . ✦

print('\n»»————-　♡　————-««\nObrigado por usar o meu programa.')