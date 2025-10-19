# gera_senhas.py
import secrets
import string

def gerar_senha(tamanho=16):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
    return senha

if __name__ == "__main__":
    qtd = int(input("Quantas senhas deseja gerar? "))
    for i in range(qtd):
        print(f"Senha {i+1}: {gerar_senha()}")
