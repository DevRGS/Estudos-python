import itertools
import time

key = input('Digite uma palavra: ')

alfa = ('a', 'e', 'i', 'o', 'u', 'ba', 'be', 'bi', 'bo', 'bu', 'ca', 'ce', 'ci', 'co', 'cu', 'da', 'de', 'di', 'do', 'du', 'fa', 'fe', 'fi', 'fo', 'fu', 'ga', 'ge', 'gi', 'go', 'gu', 'ha', 'he', 'hi', 'ho', 'hu', 'ja', 'je', 'ji', 'jo', 'ju', 'ka', 'ke', 'ki', 'ko', 'ku', 'la', 'le', 'li', 'lo', 'lu', 'ma', 'me', 'mi', 'mo', 'mu', 'na', 'ne', 'ni', 'no', 'nu', 'pa', 'pe', 'pi', 'po', 'pu', 'qa', 'qe', 'qi', 'qo', 'qu', 'ra', 're', 'ri', 'ro', 'ru', 'sa', 'se', 'si', 'so', 'su', 'ta', 'te', 'ti', 'to', 'tu', 'va', 've', 'vi', 'vo', 'vu', 'wa', 'we', 'wi', 'wo', 'wu', 'xa', 'xe', 'xi', 'xo', 'xu', 'ya', 'ye', 'yi', 'yo', 'yu', 'za', 'ze', 'zi', 'zo', 'zu', 'A', 'E', 'I', 'O', 'U', 'BA', 'BE', 'BI', 'BO', 'BU', 'CA', 'CE', 'CI', 'CO', 'CU', 'DA', 'DE', 'DI', 'DO', 'DU', 'FA', 'FE', 'FI', 'FO', 'FU', 'GA', 'GE', 'GI', 'GO', 'GU', 'HA', 'HE', 'HI', 'HO', 'HU', 'JA', 'JE', 'JI', 'JO', 'JU', 'KA', 'KE', 'KI', 'KO', 'KU', 'LA', 'LE', 'LI', 'LO', 'LU', 'MA', 'ME', 'MI', 'MO', 'MU', 'NA', 'NE', 'NI', 'NO', 'NU', 'PA', 'PE', 'PI', 'PO', 'PU', 'QA', 'QE', 'QI', 'QO', 'QU', 'RA', 'RE', 'RI', 'RO', 'RU', 'SA', 'SE', 'SI', 'SO', 'SU', 'TA', 'TE', 'TI', 'TO', 'TU', 'VA', 'VE', 'VI', 'VO', 'VU', 'WA', 'WE', 'WI', 'WO', 'WU', 'XA', 'XE', 'XI', 'XO', 'XU', 'YA', 'YE', 'YI', 'YO', 'YU', 'ZA', 'ZE', 'ZI', 'ZO', 'ZU', '!', '@', '#', '$', '%', '&', '*', '1', '2','3','4','5','6','7','8','9','0')

# Informações do processador
clock = 3.20  # GHz (velocidade do processador)
cores = 8  # Número de núcleos

# Função para calcular o número total de combinações
def calcular_numero_combinacoes():
    total_combinacoes = 0
    for length in range(1, len(key) + 1):  # De 1 até o comprimento da palavra-chave
        total_combinacoes += len(alfa) ** length
    return total_combinacoes

# Função para estimar o tempo necessário
def estimar_tempo_necessario(numero_combinacoes_medidas, tempo_medido):
    numero_combinacoes_totais = calcular_numero_combinacoes()
    tempo_por_combinacao = tempo_medido / numero_combinacoes_medidas
    tempo_total = tempo_por_combinacao * numero_combinacoes_totais
    return tempo_total

# Função para converter segundos em outras unidades de tempo
def converter_tempo(segundos):
    minutos, segundos = divmod(segundos, 60)
    horas, minutos = divmod(minutos, 60)
    dias, horas = divmod(horas, 24)
    semanas, dias = divmod(dias, 7)
    anos, semanas = divmod(semanas, 52)
    return anos, semanas, dias, horas, minutos, segundos

# Execução principal
inicio = time.time()
for length in range(1, len(key) + 1):  # De 1 até o comprimento da palavra-chave
    for combo in itertools.product(alfa, repeat=length):
        y = ''.join(combo)
        if y == key:
            print(y)
            print('Encontrei a senha')
            fim = time.time()  # Marca o tempo de fim
            tempo_decorrido = fim - inicio
            print("Tempo decorrido:", tempo_decorrido, "segundos")
            anos, semanas, dias, horas, minutos, segundos = converter_tempo(tempo_decorrido)
            print(f"Tempo decorrido (formatado): {anos} anos, {semanas} semanas, {dias} dias, {horas} horas, {minutos} minutos e {segundos:.5f} segundos")
            exit()

# Se a palavra não for encontrada
print("Palavra não encontrada.")
