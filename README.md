# Sistema de Gerenciamento de Pedidos

## Visão Geral
Este sistema foi desenvolvido para facilitar a gestão de pedidos, produtos e usuários através de uma API REST, utilizando o microframework Flask e SQLAlchemy para a interação com um banco de dados MySQL. Ideal para pequenas e médias empresas que necessitam de uma solução simples e eficiente para gerenciar suas operações de venda.

## Configuração do Ambiente

### Pré-requisitos
- Python 3.x
- MySQL
- Pip (gerenciador de pacotes Python)

## Instalação

1. Clone o repositório do projeto:

```bash
git clone https://github.com/PPrrooggrraammeerr/API.git

### Configuração do Banco de Dados
Antes de iniciar a aplicação, é necessário configurar o banco de dados:
1. Crie o banco de dados e as tabelas utilizando o script `database.sql`.
2. Ajuste as credenciais de acesso ao banco de dados no arquivo `app.py` conforme seu ambiente.

### Instalação das Dependências
Instale as dependências necessárias para rodar a aplicação:
```bash
pip install -r requirements.txt

Execução
Iniciar o Servidor
Para rodar o servidor Flask, navegue até o diretório do projeto e execute:

bash
Copy code
python app.py
O servidor será iniciado na porta 5000 e estará pronto para receber requisições HTTP.

Utilização dos Scripts
Usuários: O script users.py lê o arquivo usuarios.txt e adiciona usuários ao banco de dados através da API.
Produtos: O script produtos.py lê o arquivo products.txt e adiciona produtos ao banco de dados através da API.
Pedidos: O script pedidos.py utiliza dados de pedidos.txt para criar pedidos associados a usuários existentes.


Endpoints POST da API
Adicionar Usuário
URL: /api/adicionar_usuario

Método: POST
Corpo da Requisição: JSON com nome, email, e idade.
Resposta: Confirmação da criação do usuário ou mensagem de erro.
Adicionar Produto
URL: /api/adicionar_produto
Método: POST

Corpo da Requisição: JSON com nome e preco.
Resposta: Confirmação da criação do produto ou mensagem de erro.
Adicionar Pedido
URL: /api/adicionar_pedido
Método: POST
Corpo da Requisição: JSON com descricao, status e usuario_id.
Resposta: Confirmação da criação do pedido ou mensagem de erro.
Modelos de Dados
Os seguintes modelos representam as estruturas do banco de dados:

Usuario: Armazena informações dos usuários como nome, email e idade.
Produto: Mantém registro dos produtos disponíveis, com nome e preço.
Pedido: Relaciona pedidos a usuários, contendo descrição e status.


Endpoints GET da API
Buscar Usuário
URL: /api/buscar_usuario
Método: GET
Parâmetros da Requisição: email
Resposta: Retorna os detalhes do usuário ou uma mensagem de erro se não encontrado.

Exemplo de Uso:
Para buscar um usuário pelo email, você pode usar a seguinte URL em seu navegador ou cliente HTTP:
Browser
http://localhost:5000/api/buscar_usuario?email=exemplo@exemplo.com


Consultar Produto
URL: /api/consultar_produto
Método: GET
Parâmetros da Requisição: id
Resposta: Retorna os detalhes do produto ou uma mensagem de erro se não encontrado.

Exemplo de Uso:
Para consultar um produto pelo ID, utilize:
Browser
http://localhost:5000/api/consultar_produto?id=1


Listar Pedidos
URL: /api/listar_pedidos
Método: GET
Parâmetros da Requisição: usuario_id
Resposta: Retorna uma lista de pedidos associados ao usuário ou uma mensagem de erro se não encontrado.

Exemplo de Uso:
Para listar todos os pedidos de um usuário específico:
Browser
http://localhost:5000/api/listar_pedidos?usuario_id=123
