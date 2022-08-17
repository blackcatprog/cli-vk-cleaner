from configparser import ConfigParser

import vk_api

from utils.auth import auth
from utils.config_tools import config_reader

class Friends_Cleaner:
	
	def __init__(self):
		token = config_reader()
		self.session = auth(token)

	def get_friends(self) -> int:
		self.getFriends = self.session.method("friends.get", {
			"order": "hints",
			"fields": "bdate"
		})

		self.count_friends = self.getFriends["count"]

		return self.count_friends

	def clear_friends(self):
		self.get_friends()
		for _ in self.getFriends["count"]:
			response = input(f"Удалить друга {self.getFriends['items'][_]['first_name']} {self.getFriends['items'][_]['last_name']} (y(да)/n(нет)): ")
			if response == "y":
				self.session.method("friends.delete", {
					"user_id": _["id"]
				})

	def clear_all_friends(self):
		warning = input("Вы уверены (будут удалены все друзья с вашей страницы) (y(да)/n(нет): ")
		if warning == "y":
			self.get_friends()
			for _ in self.getFriends["count"]:
				self.session.method("friends.delete", {
					"user_id": _["id"]
				})