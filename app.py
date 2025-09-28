from flask import Flask, request, jsonify, send_from_directory
import replicate
import os

app = Flask(__name__)

# ... (tu ruta /generar ya existente) ...

# NUEVA RUTA: para chat con IA
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    mensaje = data.get("mensaje", "").strip()
    
    if not mensaje:
        return jsonify({"respuesta": "¿En qué puedo ayudarte?"}), 400

    try:
        # Usamos un modelo de lenguaje (como Llama 3) para responder
        output = replicate.run(
            "meta/llama-3-8b-instruct",
            input={"prompt": f"Responde como Hinata Hyuga de Naruto, de forma amable, tímida y dulce. Mensaje: {mensaje}"}
        )
        respuesta = "".join(output).strip()
        return jsonify({"respuesta": respuesta})
    except Exception as e:
        return jsonify({"respuesta": "Lo siento, no pude procesar tu mensaje."}), 500

# ... (el resto de tu código) ...
