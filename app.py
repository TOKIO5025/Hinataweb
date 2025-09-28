from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/ia', methods=['POST'])
def ia():
    data = request.get_json()
    prompt = data.get("prompt", "")
    # Aquí tu lógica de IA (ejemplo básico)
    return jsonify({"respuesta": f"Tu escribiste: {prompt}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    
