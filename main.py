
# Tokens realizado con una cuenta de gmail silviajaneta-m@hotmail.com
import openai
import uvicorn
from fastapi import FastAPI, Request
from uce.ai.Pruebalunes import Document, interface
from pydantic import BaseModel


@app.post('/inference', status_code=200)
def inference_endpoint(doc: Document):
    response = inference(doc.prompt)
    return{
        'inference': response[0],
        'usage': response[1]
    }


    prompt: str = ''

openai.api_key = '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'
openai.organization='org-J0y1yI2sOfB5bhErJ2Ul9UrT'

app = FastAPI()

class TokenInput(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"Hola": "Mundo"}


completion = openai.ChatCompletion.create(
    model="gtp-3.5-turbo",
    messages = [
        {"role": "system","content": """Eres una calculadora factorial, cada numero ingresado, calcula el factorial"""},

        {"role": "user","content": prompt}
    ]
)


content= completion.choices[0].message.content
total_tokens= completion.usage.total_tokens

@app.post ("/calculadorafactorial/{numero}")
def calcular_factorial(numero: int):
    if numero < 0:
        return {"error": "El número debe ser un entero no negativo."}
    elif numero == 0:
        return {"factorial": 1}
    else:
        factorial = 1
        for i in range(1, numero + 1):
            factorial *= i
        return {"factorial": factorial}


@app.post("/tokens_consumidos")
def contar_tokens_consumidos(texto: TokenInput):
    response = openai.Completion.create(
        engine='davinci',
        prompt=texto.text,
        max_tokens=0,
        log_level="info"
    )

    tokens_consumidos = response['usage']['total_tokens']
    return {"tokens_consumidos": tokens_consumidos}

