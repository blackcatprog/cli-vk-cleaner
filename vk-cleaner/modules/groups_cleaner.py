from configparser import ConfigParser

import vk_api

from utils.auth import auth
from utils.config_tools import config_reader

class Groups_Cleaner:
	
	def __init__(self):
		token = config_reader()
		self.session = auth(token)

	def get_groups(self, offset=0) -> int:
		self.getGroups = self.session.method("groups.get", {
			"extended": 1
		})

		return self.getGroups["count"]

	def clear_groups(self):
		self.get_groups()
		for _ in self.getGroups["count"]:
			response = input(f"Отписаться от группы {self.getGroups['items'][_]['name']} (y(да)/n(нет): ")
			if response == "y":
				self.session.method("groups.leave", {
					"group_id": _["id"]
				})

	def clear_all_groups(self):
		warning = input("Вы уверены (вы отпишитесь от всех сообществ) (y(да)/n(нет): ")
		if warning == "y":
			self.get_groups()
			for _ in self.getGroups["count"]:
				self.session.method("groups.leave", {
					"group_id": _["id"]
				})