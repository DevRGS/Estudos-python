import requests
import threading

# Configurações
url = "seu_site_aqui"  # substitua por seu site
num_threads = 100  # número de threads
num_requisicoes = 1000  # número de requisições por thread

def fazer_requisicao():
    for i in range(num_requisicoes):
        try:
            resposta = requests.get(url)
            print(f"Requisição {i+1} - Código de status: {resposta.status_code}")
        except Exception as e:
            print(f"Erro: {e}")

# Criação de threads
threads = []
for i in range(num_threads):
    t = threading.Thread(target=fazer_requisicao)
    threads.append(t)
    t.start()

# Aguarda término das threads
for t in threads:
    t.join()

print("Teste concluído.")

