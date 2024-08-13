from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def test_hack_1():
    return jsonify({'payload': 'success'})

@app.route('/user', methods=['POST'])
def test_hack_2():
    return jsonify({'payload': 'success'})

@app.route('/user', methods=['DELETE'])
def test_hack_3():
    return jsonify({'payload': 'success'})

@app.route('/user', methods=['PUT'])
def test_hack_4():
    return jsonify({'payload': 'success', 'error': False})

@app.route('/api/v1/users', methods=['GET'])
def test_hack_5():
    return jsonify({'payload': []})

@app.route('/api/v1/user', methods=['POST'])
def test_hack_6():
    email = request.args.get('email')
    name = request.args.get('name')
    if email and name:
        payload = {
            'email': email,
            'name': name
        }
        return jsonify({'payload': payload}), 200
    else:
        return jsonify({'error': 'Invalid request'}), 400

@app.route('/api/v1/user/add', methods=['POST'])
def test_hack_7():
    email = request.form.get('email')
    name = request.form.get('name')
    id = request.form.get('id')
    return jsonify({
        'payload': {
            'email': email,
            'name': name,
            'id': id
        }
    })

@app.route('/api/v1/user/create', methods=['POST'])
def test_hack_8():
    data = request.get_json()
    email = data.get('email')
    name = data.get('name')
    id = data.get('id')
    return jsonify({
        'payload': {
            'email': email,
            'name': name,
            'id': id
        }
    })

if __name__ == '__main__':
    app.run()