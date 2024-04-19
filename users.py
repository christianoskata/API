import requests

# Caminho para o arquivo
arquivo = 'usuarios.txt'

with open(arquivo, 'r') as file:
    for linha in file:
        # Separa os dados de cada usuário, supondo que estão separados por vírgula
        partes = linha.strip().split(',')
        nome = partes[0]
        email = partes[1]
        idade = int(partes[2])  # Converte a string de idade para int

        # Dados JSON para enviar na requisição
        json_data = {
            "nome": nome,
            "email": email,
            "idade": idade
        }

        # URL da API (ajuste conforme necessário)
        url = 'http://localhost:5000/api/adicionar_usuario'

        # Faz a requisição POST
        response = requests.post(url, json=json_data)

        # Imprime a resposta do servidor (opcional)
        print(response.text)
