import json
import logging
import os
import sys

from dotenv import load_dotenv
import requests

log = logging.getLogger(__name__)


class ReadSteamData:
    def __init__(self, api_key: str, player_id: str):
        self.api_key = api_key

        self.player_id = player_id

    def get_owned_games(self, api_key: str, player_id: str):
        url = f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={self.api_key}&steamid={self.player_id}&format=json&include_appinfo=true&include_played_free_games=true"
        response = requests.get(url)

        log.info(response.json())


if __name__ == "__main__":
    logging = logging.basicConfig(level=logging.DEBUG)

    load_dotenv()

    api_key = os.environ.get("API_KEY")
    player_id = os.environ.get("PLAYER_ID")

    reader = ReadSteamData(api_key, player_id)

    reader.get_owned_games(reader.api_key, reader.player_id)
