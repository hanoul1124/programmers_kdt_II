import flask
from flask import jsonify, request
import sqlite3 as sql

app = flask.Flask(__name__)


@app.route('/whoami')
def get_id():
    context = {
        "name": "hanoul1124",
    }
    return jsonify(context)


@app.route('/echo')
def echo_string():
    context = {
        "value": request.args.get('string')
    }
    return jsonify(context)


@app.route('/weapon')
def get_weapon_list():
    conn = sql.connect('database.db')
    curr = conn.cursor()
    curr.execute('SELECT * FROM weapons')
    rows = curr.fetchall()
    conn.close()
    contexts = [
        {
            "id": row[0],
            "name": row[1],
            "stock": row[2]
        }
        for row in rows
    ]
    return jsonify(contexts)


@app.route('/weapon', methods=['POST'])
def create_weapon():
    data = request.get_json()
    new_name, new_stock = data['name'], data['stock']
    conn = sql.connect('database.db')
    curr = conn.cursor()
    curr.execute(
        'INSERT INTO weapons (id, name, stock) values (?, ?, ?)',
        (None, new_name, new_stock)
    )
    conn.commit()
    curr.execute('SELECT last_insert_rowid()')
    last_data_id = curr.fetchone()[0]
    conn.close()
    context = {
        "id": last_data_id,
        "name": new_name,
        "stock": new_stock
    }
    return jsonify(context)


@app.route('/weapon/<int:id>', methods=['DELETE'])
def delete_weapon(id):
    conn = sql.connect('database.db')
    curr = conn.cursor()
    if curr.execute('select id from weapons where id == (?)', str(id)):
        curr.execute('delete from weapons where weapons.id == (?)', str(id))
        conn.commit()
        conn.close()
        return jsonify({"message": f"Weapon ID:{id}가 성공적으로 삭제되었습니다."})
    conn.close()
    return jsonify({"message": "전달된 ID에 해당하는 Weapon이 존재하지 않습니다."})


@app.route('/weapon/<int:id>', methods=['PUT'])
def update_weapon(id):
    data = request.get_json()
    updated_name, updated_stock = data['name'], data['stock']
    conn = sql.connect('database.db')
    curr = conn.cursor()
    if curr.execute('select id from weapons where id == (?)', str(id)):
        curr.execute('UPDATE weapons SET name = (?), stock = (?) WHERE id == (?)', (updated_name, updated_stock, str(id)))
        conn.commit()
        conn.close()
        context = {
            "id": id,
            "name": updated_name,
            "stock": updated_stock
        }
        return jsonify(context)
    curr.close()
    return jsonify({"message": "전달된 ID에 해당하는 Weapon이 존재하지 않습니다."})


if __name__ == 'main':
    app.run()
