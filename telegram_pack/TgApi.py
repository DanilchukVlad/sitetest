import requests
from telegram_pack import config


class TgApi:

    def __init__(self):
        self.url = "https://api.telegram.org/bot"

    def send_message(self, text: str, channel_id: int) -> object:
        url = self.url
        token = config.TOKEN
        url += token
        endpoint = url + "/sendMessage"

        r = requests.post(endpoint, data={
             "chat_id": channel_id,
             "text": text
              })

        return r

    def send_photo(self, text: str, link: str, channel_id: int):
        url = self.url
        token = config.TOKEN
        url += token
        endpoint = url + "/sendPhoto"

        files = {'photo': open(text, 'rb')}

        r = requests.post(endpoint, files=files, data={
            "chat_id": channel_id,
            "caption": link
              })

        return r
