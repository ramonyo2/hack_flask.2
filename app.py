from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

@app.route('/users', methods=['GET',])
def welcome():
    return jsonify({'payload': 'success'})


app = Flask(__name__)


@app.route('/user', methods=['POST',])
def welcome():
    return jsonify({'payload': 'success'})


app = Flask(__name__)

@app.route('/user', methods=['DELETE',])
def welcome():
    return jsonify({'payload': 'success',})

app = Flask(__name__)

@app.route("/user", methods= ['PUT'])
def welcome():
    return jsonify ({'payload':'success','error':False })
 
app = Flask(__name__)

@app.route("/api/V1/users", methods= ['GET'])
def get_users_V1():
    return jsonify ({'payload':[]})
 
app = Flask(__name__)

@app.route("/api/V1/user", methods= ['POST'])
def get_users_V1():
    email = request.args.get("email")
    name = request.args.get("name")
    user = request.args.get("user")
    return jsonify ({'payload':{'email':email,'name': name}})


@app.route('/api/v1/user/add', methods=['POST'])
def add_user():
    email = request.form.get('email')
    name = request.form.get('name')
    user_id = request.form.get('id')
    return jsonify({'payload': {'email': email, 'name': name, 'id': user_id}})

@app.route('/api/v1/user/create', methods=['POST'])
def create_user():
    data = request.get_json()
    email = data.get('email')
    name = data.get('name')
    user_id = data.get('id')
    return jsonify({'payload': {'email': email, 'name': name, 'id': user_id}})
 



if __name__ == "__main__":
    app.run(debug=True)