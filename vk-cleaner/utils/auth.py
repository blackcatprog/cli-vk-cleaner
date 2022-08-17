from configparser import ConfigParser
import os
import wget
import requests

from PIL import Image
import vk_api

def two_factor() -> [int, bool]:
	code = input("Код из смс: ")
	remember_device = False

	return code, remember_device

def captcha_handler(captcha):
	captcha_picture = requests.get(captcha.get_url())
	with open("captcha.jpg", "wb") as file:
		file.write(captcha_picture.content)
	img = Image.open("./captcha.jpg")
	img.show()
	# os.remove("./captcha.jpg")
	cpt = input("Введите капчу: ")

	return captcha.try_again(cpt.strip())

def auth(token: str):
	vk_session = vk_api.VkApi(token = token, captcha_handler = captcha_handler, auth_handler = two_factor)

	return vk_session