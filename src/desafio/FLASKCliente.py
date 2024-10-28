# Desafio - implementação usando o flask
# * Dependencia: pip install flask

import requests

servername = 'http://localhost:12000/send'
sentence = input('Input lowercase sentence: ')
response = requests.post(servername, data=sentence.encode())  # Envia a mensagem para o servidor
modifiedSentence = response.text  # Recebe a resposta
print('From Server:', modifiedSentence)
