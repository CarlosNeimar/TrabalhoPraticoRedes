# Desafio - implementação usando o flask
# * Dependencia: pip install flask
from flask import Flask, request

app = Flask(__name__)

@app.route('/send', methods=['POST'])
def receive_message():
    sentence = request.data.decode()  # Recebe a mensagem do cliente
    capitalizedSentence = sentence.upper()  # Converte para letras maiúsculas
    return capitalizedSentence  # Retorna a resposta

if __name__ == '__main__':
    app.run(port=12000)
