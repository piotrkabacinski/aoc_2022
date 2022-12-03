from dotenv import dotenv_values
from requests import get


def get_input(url):
    session_id = dotenv_values(".env").get("SESSION_ID")

    response = get(url, cookies={"session": session_id})

    return response.text.split("\n")
