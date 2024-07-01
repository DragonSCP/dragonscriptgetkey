import re
import sys

def extrair_key_executor(link):
    # Definir o padrão de regex para encontrar a key
    padrao = r'\bkey=([a-zA-Z0-9_-]+)\b'
    
    # Procurar pela key no link usando regex
    match = re.search(padrao, link)
    
    # Verificar se encontrou a key
    if match:
        return match.group(1)  # Retorna o valor da key capturada pelo regex
    else:
        return None  # Retorna None se não encontrar a key no link

# Função para pegar o link do usuário pelo terminal
def pegar_link_do_usuario():
    try:
        link = input("Digite o link do executor: ").strip()
        return link
    except KeyboardInterrupt:
        print("\nOperação cancelada.")
        sys.exit(1)

# Função principal para executar o programa
def main():
    try:
        # Pegar o link do usuário
        link_do_executor = pegar_link_do_usuario()
        
        # Extrair a key do executor
        key_encontrada = extrair_key_executor(link_do_executor)
        
        if key_encontrada:
            print(f"A key do executor é: {key_encontrada}")
        else:
            print("Não foi possível encontrar a key do executor no link fornecido.")
            
    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

if __name__ == "__main__":
    main()
