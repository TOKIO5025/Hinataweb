@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    mensaje = data.get("mensaje", "").strip()
    
    if not mensaje:
        return jsonify({"respuesta": "¿En qué puedo ayudarte?"}), 400

    try:
        output = replicate.run(
            "meta/llama-3-8b-instruct",
            input={"prompt": f"Responde como Hinata Hyuga de Naruto, de forma amable y tímida. Mensaje: {mensaje}"}
        )
        respuesta = "".join(output).strip()
        return jsonify({"respuesta": respuesta})
    except Exception as e:
        return jsonify({"respuesta": "Lo siento, no pude procesar tu mensaje."}), 500
