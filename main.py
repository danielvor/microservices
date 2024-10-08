from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/hello', methods=['GET'])
def hello_python():
    return "Hello Python"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
