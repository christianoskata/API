
from flask import Flask, request, jsonify
from models import db, Usuario, Pedido, Produto, PedidoProduto
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/api/adicionar_usuario', methods=['POST'])
def adicionar_usuario():
    try:
        data = request.get_json()
        novo_usuario = Usuario(nome=data['nome'], email=data['email'], idade=data['idade'])
        db.session.add(novo_usuario)
        db.session.commit()
        return jsonify(message="Usuário adicionado com sucesso!"), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify(error="Erro ao adicionar usuário. Email já existe."), 400

@app.route('/api/buscar_usuario', methods=['GET'])
def buscar_usuario():
    email = request.args.get('email')
    usuario = Usuario.query.filter_by(email=email).first()
    if usuario:
        return jsonify(nome=usuario.nome, email=usuario.email, idade=usuario.idade), 200
    else:
        return jsonify(error="Usuário não encontrado."), 404

@app.route('/api/adicionar_produto', methods=['POST'])
def adicionar_produto():
    try:
        data = request.get_json()
        novo_produto = Produto(nome=data['nome'], preco=data['preco'])
        db.session.add(novo_produto)
        db.session.commit()
        return jsonify(message="Produto adicionado com sucesso!"), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify(error="Erro ao adicionar produto. Nome já existe ou preço inválido."), 400
    except Exception as e:
        db.session.rollback()
        return jsonify(error=str(e)), 500
        
@app.route('/api/consultar_produto', methods=['GET'])
def consultar_produto():
    id_produto = request.args.get('id')
    if id_produto is None:
        return jsonify({"mensagem": "O parâmetro 'id' é obrigatório"}), 400

    produto = Produto.query.get(id_produto)
    if produto:
        resultado = {"id": produto.id, "nome": produto.nome, "preco": str(produto.preco)}
        return jsonify(resultado), 200
    else:
        return jsonify({"mensagem": "Produto não encontrado"}), 404

@app.route('/api/adicionar_pedido', methods=['POST'])
def adicionar_pedido():
    try:
        data = request.get_json()
        usuario = Usuario.query.get(data['usuario_id'])
        if not usuario:
            return jsonify({'error': "Usuário não encontrado."}), 404

        produto = Produto.query.get(data['produto_id'])  # Alterado para corresponder ao nome enviado no JSON
        if not produto:
            return jsonify({'error': "Produto não encontrado."}), 404

        novo_pedido = Pedido(usuario_id=data['usuario_id'], descricao=data['descricao'], status=data['status'])
        db.session.add(novo_pedido)
        db.session.flush()  # Garante que o pedido tenha um ID antes de associar com o produto

        pedido_produto = PedidoProduto(pedido_id=novo_pedido.id, produto_id=produto.id)
        db.session.add(pedido_produto)

        db.session.commit()
        return jsonify({'message': "Pedido adicionado com sucesso!"}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/listar_pedidos', methods=['GET'])
def listar_pedidos():
    usuario_id = request.args.get('usuario_id')
    if usuario_id:
        # Busca todos os pedidos associados ao usuário especificado
        pedidos = Pedido.query.filter_by(usuario_id=usuario_id).all()
        if pedidos:
            resultados = []
            for pedido in pedidos:
                # Recupera todos os produtos associados a cada pedido
                produtos = []
                for produto in pedido.produtos:  # Asegure-se de que a relação many-to-many está definida
                    produtos.append({"produto_id": produto.id, "nome": produto.nome, "preco": str(produto.preco)})
                
                resultados.append({
                    "id": pedido.id,
                    "usuario_id": pedido.usuario_id,
                    "descricao": pedido.descricao,
                    "status": pedido.status,
                    "produtos": produtos
                })
            return jsonify(resultados), 200
        else:
            return jsonify({"mensagem": "Nenhum pedido encontrado para o usuário especificado"}), 404
    else:
        return jsonify({"mensagem": "ID do usuário não especificado"}), 400

if __name__ == '__main__':
    app.run(debug=True)


if __name__ == '__main__':
    app.run(debug=True)
