import mysql.connector
from flask import Flask, make_response, jsonify, request
# from bd import clientes


mydb = mysql.connector.connect(
    host='localhost',
    user='MainUse',
    password='MainPassword',
    database='Pycodebr'
)

app = Flask(__name__)
app.json.sort_keys = False


@app.route('/clientes', methods=['GET'])
def get_clientes():

    my_cursor = mydb.cursor()
    my_cursor.execute('SELECT * FROM clientes')
    meus_clientes = my_cursor.fetchall()

    list_clientes = list()
    for cliente in meus_clientes:
        list_clientes.append(
            {
                'id': cliente[0],
                'nome': cliente[1],
                'bairro': cliente[2],
                'idade': cliente[3]
            }
        )

    return make_response(jsonify(menssagem='Lista de clientes', dados=list_clientes))


@app.route('/clientes', methods=['POST'])
def create_cliente():
    cliente = request.json

    my_cursor = mydb.cursor()
    sql = f"INSERT INTO clientes (nome, bairro, idade) VALUES ('{cliente['nome']}', '{cliente['bairro']}', " \
          f"{cliente['idade']})"
    my_cursor.execute(sql)
    mydb.commit()

    return make_response(jsonify(menssagem='Cliente cadastrado com sucesso', dados=cliente))


app.run(debug=True)
