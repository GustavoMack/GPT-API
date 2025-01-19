import openai
from dotenv import load_dotenv
import os

load_dotenv() #CARREGA AS VARIÁVEIS DO .ENV
openai.api_key = os.getenv('OPENAI_API_KEY') #PEGA A VARIAVEL DO .ENV


resposta = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # Alterado para um modelo de chat mais recente
    messages=[
        {"role": "system", "content": """
         Você é um assistente de um chat sobre culinária
         apenas culinária não pode se desvirtuar do assunto
         """},
        {"role": "user", "content": """
         
         """}
    ],
    max_tokens=100
)

print(resposta['choices'][0]['message']['content']) 