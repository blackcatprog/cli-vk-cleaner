from configparser import ConfigParser
from getpass import getpass

from cli import *

def config_creator(token: str):
	config = ConfigParser()
	config.add_section("token")
	config.set("token", "token", token)

	with open("vk-cleaner/config.ini", "w") as cfg_file:
		config.write(cfg_file)

def config_reader() -> str:
	config = ConfigParser()
	config.read("vk-cleaner/config.ini")

	try:
		token = config["token"]["token"]
	except Exception:
		token = input("Введите токен > ")
		config_creater(token)

	return token