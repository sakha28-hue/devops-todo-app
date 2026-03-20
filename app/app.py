from flask import Flask, jsonify, request

app = Flask(__name__)

todos = []
counter = 1

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def create_todo():
    global counter
    data = request.get_json()
    todo = {
        'id': counter,
        'task': data['task'],
        'done': False
    }
    todos.append(todo)
    counter += 1
    return jsonify(todo), 201

@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    global todos
    todos = [t for t in todos if t['id'] != id]
    return jsonify({'message': 'Deleted'}), 200

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
