import requests

# Caminho para o arquivo
arquivo = 'products.txt'

with open(arquivo, 'r') as file:
    for linha in file:
        # Separa o nome do produto e o preço, supondo que estão separados por vírgula
        partes = linha.strip().split(',')
        nome_produto = partes[0]
        preco_produto = float(partes[1])  # Converte a string de preço para float

        # Dados JSON para enviar na requisição
        json_data = {
            "nome": nome_produto,
            "preco": preco_produto
        }

        # URL da API
        url = 'http://localhost:5000/api/adicionar_produto'

        # Faz a requisição POST
        response = requests.post(url, json=json_data)

        # Imprime a resposta do servidor (opcional)
        print(response.text)
