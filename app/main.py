from flask import Flask, request, jsonify

app = Flask(__name__)

calculation_history = []

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    op = data['operation']
    a = data['a']
    b = data['b']
    
    if op == 'add':
        result = a + b
    elif op == 'subtract':
        result = a - b
    elif op == 'multiply':
        result = a * b
    elif op == 'divide':
        result = a / b
    else:
        result = None
    
    calculation_history.append({'op': op, 'result': result})
    return jsonify({'result': result})

@app.route('/history', methods=['GET'])
def history():
    return jsonify(calculation_history)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
