import os
from typing import List, Optional

import openai
from dotenv import load_dotenv
from fastapi import FastAPI

from . import personas
from .models import CLIInput, Response

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
app = FastAPI()


# TODO : コマンド実行機能を追加
@app.post("/")
async def chat(cli_input: CLIInput) -> Response:
    chat_log = cli_input.chat_log
    if cli_input.character in personas.PERSONAS.keys():
        persona = personas.PERSONAS[cli_input.character]
        system_setting = {"role": "system", "content": persona}
        # 配列の先頭に挿入
        chat_log.insert(0, system_setting)
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_log,
    )
    sampled_response = response.choices[0].message.content
    response_dict = {"response": sampled_response, "command": None}
    response_object = Response(**response_dict)
    return response_object
