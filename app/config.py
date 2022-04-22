import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


def get_version():
    return "v0.0.1"


