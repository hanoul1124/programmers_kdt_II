import flask
from flask import jsonify, request

app = flask.Flask(__name__)

menus = [
    {"id": 1, "name": "Espresso", "price": 3000},
    {"id": 2, "name": "Americano", "price": 4100},
    {"id": 3, "name": "Cafelatte", "price": 4600},
    ]

@app.route('/')
def hello_flask():
    return "Hello world"


#GET /menus | 자료를 가지고 온다
@app.route('/menus')
def get_menus():
    return jsonify({"menus": menus})


#POST /menus | 자료를 자원에 추가한다
@app.route('/menus', methods=['POST'])
def create_menu(): # request가 JSONdlfkrh rkwjd
    # 전달받은 자료를 menus 자원에 추가
    # JSON Parsing with .get_json()
    request_data = request.get_json() # {"name": ... }
    new_menu = {
        "id": 4,
        "name": request_data['name'],
        "price": request_data['price']
    }
    menus.append(new_menu)
    return jsonify(new_menu)


# DELETE /menu/<int:id>
@app.route('/menu/<int:id>', methods=['DELETE'])
def delete_menu(id):
    # menus에 새로운 리스트 값을 할당하는 아래 코드는 global 선언 없이
    # 사용하면 UnboundLocalError가 발생한다.
    # 이는 Python 함수 내에서 외부 변수에 값을 할당할 경우,
    # 할당 시점에서 이를 Local 변수로 간주하기 때문이다.
    # 참조: https://blog.weirdx.io/post/44564
    global menus
    menus = [menu for menu in menus if menu['id'] != id]
    return flask.Response(status=200)


# PUT /menu/<int: id>
@app.route('/menu/<int:id>', methods=['PUT'])
def update_menu(id):
    request_data = request.get_json()
    updated_menu = {
        "name": request_data['name'],
        "price": request_data['price']
    }
    for index, menu in enumerate(menus):
        if menu['id'] == id:
            menus[index] = updated_menu
            break
    return jsonify(updated_menu)
    

if __name__ == '__main__':
    app.run()