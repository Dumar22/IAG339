from flask import Flask, request, jsonify
from chatbot_supervisado import build_and_train_model, predict_answer
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Datos de entrenamiento
training_data = [
    ("buenos días", "!Buenos días¡"),
    ("Hola", "Hola!, en que puedo ayudarte?"),
    ("Como estas?", "Soy solo un bot, pero estoy aquí para ayudar!"),
    ("adiós", "!HAsta luego¡"),
    ("tu nombre", "Soy un chatbot de ejmplo"),
    ("que puedes hacer", "Puedo responder preguntas simples")
]

# Entrenar el modelo una sola vez al iniciar
model, vectorizer, unique_answers = build_and_train_model(training_data)

@app.route('/chat', methods=['POST'])
def chat():
    """Endpoint para procesar mensajes del chatbot"""
    try:
        data = request.json
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'El mensaje no puede estar vacío'}), 400
        
        # Obtener respuesta del chatbot
        response = predict_answer(model, vectorizer, unique_answers, user_message)
        
        return jsonify({
            'message': user_message,
            'response': response,
            'success': True
        })
    except Exception as e:
        return jsonify({'error': str(e), 'success': False}), 500

@app.route('/health', methods=['GET'])
def health():
    """Endpoint para verificar que el servidor está en línea"""
    return jsonify({'status': 'online'})

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
