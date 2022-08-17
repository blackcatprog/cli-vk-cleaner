from configparser import ConfigParser

import vk_api

from utils.auth import auth
from utils.config_tools import config_reader

class Wall_Cleaner:
	
	def __init__(self):
		token = config_reader()
		self.session = auth(token)

	def get_wall(self, offset=0) -> int:
		self.getWall = self.session.method("wall.get", {
			"count": 100,
			"offset": offset
		})

		self.count_wall = self.getWall["count"]

		return self.count_wall

	def clear_wall(self):
		self.offset = 0

		for i in range((self.get_wall() // 100) + 1):
			self.get_wall(self.offset)

			for j in self.getWall["items"]:
				self.session.method("wall.delete", {
					"owner_id": j["owner_id"],
					"post_id": j["id"]
				})

			self.offset += len(self.getWall["items"])

		self.offset = 0