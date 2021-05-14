import flask
from flask import jsonify, request
import sqlite3 as sql


app = flask.Flask(__name__)


@app.route('/')
def hello_flask():
    return "Hello world"


#GET /menus | 자료를 가지고 온다
@app.route('/menus')
def get_menus():
    connect = sql.connect('database.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM MENUS')
    rows = cursor.fetchall()
    menus = [{'id': row[0], 'name': row[1], 'price': row[2]} for row in rows]
    connect.close()
    
    return jsonify({"menus": menus})


#POST /menus | 자료를 자원에 추가한다
@app.route('/menus', methods=['POST'])
def create_menu(): # request가 JSON이라고 가정
    # 전달받은 자료를 menus 자원에 추가
    # JSON Parsing with .get_json()
    request_data = request.get_json() # {"name": ... }
    new_name, new_price = request_data['name'], request_data['price']
    
    connect = sql.connect('database.db')
    cursor = connect.cursor()
    # Auto Increment를 적용했으므로, ID는 따로 값을 넣어주지 않는다
    cursor.execute('INSERT INTO MENUS(ID, NAME, PRICE) VALUES (?, ?, ?)', (None, new_name, new_price))
    connect.commit()
    cursor.execute('SELECT last_insert_rowid()')
    # 가장 마지막에 추가된 row의 ID(자동생성된) 가져오기
    last_data_id = cursor.fetchone()[0]
    connect.close()
    
    new_menu = {'id': last_data_id, 'name': new_name, 'price': new_price}
    return jsonify({"new_menu": new_menu})


# DELETE /menu/<int:id>
@app.route('/menu/<int:id>', methods=['DELETE'])
def delete_menu(id):
    connect = sql.connect('database.db')
    cursor = connect.cursor()
    cursor.execute('DELETE FROM MENUS WHERE MENUS.ID == (?)', (str(id)))
    connect.commit()
    connect.close()
    return flask.Response(status=204)


# PUT /menu/<int:id>
@app.route('/menu/<int:id>', methods=['PUT'])
def update_menu(id):
    request_data = request.get_json()
    new_name, new_price = request_data['name'], request_data['price']
    connect = sql.connect('database.db')
    cursor = connect.cursor()
    cursor.execute('UPDATE MENUS SET NAME = (?), PRICE = (?) WHERE ID == (?)', (new_name, new_price, id))
    connect.commit()
    connect.close()
    
    updated_menu = {'id': id, 'name': new_name, 'price': new_price}
    return jsonify({"updated_menu": updated_menu})
    

if __name__ == '__main__':
    app.run()