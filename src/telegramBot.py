from tkinter import N
from dotenv import load_dotenv
import os
import requests
import json

from src.data.transform_dataframe import transform_data
from src.visualization.visualize import barra_vertical_media_nps_mean_by

load_dotenv()  # take environment variables from .env.


class TelegramBot:
    def __init__(self):
        TOKEN = os.getenv("API_KEY")
        self.url = f"https://api.telegram.org/bot{TOKEN}/"

    def start(self):
        update_id = None
        while True:
            update = self.get_message(update_id)
            messages = update['result']
            if messages:
                for message in messages:
                    try:
                        update_id = message['update_id']
                        chat_id = message['message']['from']['id']
                        message_text = message['message']['text']
                        answer_bot = self.create_answer(message_text)
                        self.send_answer(chat_id, answer_bot)
                    except:
                        pass

    def get_message(self, update_id):
        link_request = f"{self.url}getUpdates?timeout=1000"
        if update_id:
            link_request = f"{self.url}getUpdates?timeout=1000&offset={update_id + 1}"
        result = requests.get(link_request)
        return json.loads(result.content)

    def create_answer(self, message_text):
        df = transform_data(self.driveBot.get_data())
        if message_text in ["/start", "ola", "oi", "olá", "Ola", "oie", "Olá", "menu"]:
            return """ Olá, tudo bem ? Seja bem vindo ao bot do NPS interno mensal da empresa Ficticia
                1 - NPS interno mensal médio por setor \N
                2 - NPS interno mensal médio por contratação \n
                3 - DISTRIBUIÇÃO do NPS interno \n""", 0
        elif message_text == "1":
            return barra_vertical_media_nps_mean_by(df, "Setor"), 1
        elif message_text == "2":
            return barra_vertical_media_nps_mean_by(df, "Tipo de Contratação"), 1
        elif message_text == "3":
            return hist_nps(df), 1
        else:
            return "Desculpe, não entendi o que você quis dizer", 0

    def send_answer(self, chat_id, answer, fig_bool):
        if fig_bool == 0:
                link_to_send = f"{self.url}sendMessage?chat_id={chat_id}&text={answer}"
                requests.get(link_to_send)
                return
        else :
            figure = r"./bot_telegram_analise_dados/graph_last_generate.png"
            files ={
                "photo": open(figure, "rb")
            }
            link_to_send = f"{self.url}sendPhoto?chat_id={chat_id}"
            requests.post(link_to_send, files=files)
            return
