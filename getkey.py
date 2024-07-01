import requests
import re
import sys

def extrair_key_executor(link):
    try:
        # Headers personalizados para simular um navegador
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        # Fazendo a requisição GET ao link fornecido com headers
        response = requests.get(link, headers=headers)

        # Verificando se a requisição foi bem sucedida
        response.raise_for_status()

        # Definir o padrão de regex para encontrar a key
        padrao = r'KEY_[a-fA-F0-9]+'

        # Procurar pela key no conteúdo da resposta usando regex
        match = re.search(padrao, response.text)

        # Verificar se encontrou a key
        if match:
            return match.group(0)  # Retorna a key encontrada
        else:
            return None  # Retorna None se não encontrar a key no conteúdo

    except requests.exceptions.RequestException as e:
        print(f"Erro ao fazer a requisição: {str(e)}")
        return None
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")
        return None

# Função principal para executar o programa
def main():
    try:
        # Pegar o link do usuário
        link_do_executor = input("Digite o link do executor: ").strip()

        # Extrair a key do executor
        key_encontrada = extrair_key_executor(link_do_executor)

        if key_encontrada:
            print(f"A key do executor é: {key_encontrada}")
        else:
            print("Não foi possível encontrar a key do executor no link fornecido.")

    except KeyboardInterrupt:
        print("\nOperação cancelada.")
        sys.exit(1)
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

if __name__ == "__main__":
    main()
