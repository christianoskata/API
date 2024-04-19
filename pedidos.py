import requests
import random

arquivo_pedidos = 'pedidos.txt'
url = 'http://localhost:5000/api/adicionar_pedido'

# Supondo que você queira escolher aleatoriamente um único usuário para cada pedido
usuarios_ids = random.sample(range(1, 11), 5)  # Assumindo que existam pelo menos 5 usuários

# Carrega as informações do arquivo em uma lista
pedidos = []
with open(arquivo_pedidos, 'r') as file:
    for linha in file:
        partes = linha.strip().split(',')
        pedidos.append({
            "descricao": partes[0],
            "status": partes[1]
        })

# Embaralha a lista de pedidos para garantir aleatoriedade na ordem de envio
random.shuffle(pedidos)

# Envie cada pedido para a API com um usuário aleatório
for pedido in pedidos:
    usuario_id = random.choice(usuarios_ids)  # Escolhe um usuário aleatório para cada pedido
    produto_id = random.choice(range(1, 11))  # Escolhe um produto aleatório para cada pedido

    json_data = {
        "usuario_id": usuario_id,
        "descricao": pedido["descricao"],
        "status": pedido["status"],
        "produto_id": produto_id
    }

    response = requests.post(url, json=json_data)
    if response.status_code == 201:
        print(f"Pedido adicionado com sucesso: {response.text}")
    else:
        print(f"Erro ao adicionar pedido: {response.text}")
