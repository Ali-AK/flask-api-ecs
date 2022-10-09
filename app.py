from flask import Flask, jsonify, make_response

app = Flask(__name__)


@app.route('/', methods=['GET'])
def health_check():
    return make_response(jsonify({'status': 200, 'healthy': True}), 200)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
