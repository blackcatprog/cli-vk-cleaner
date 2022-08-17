from configparser import ConfigParser

import vk_api

from utils.auth import auth
from utils.config_tools import config_reader

class Requests_Cleaner:
	"""Clear outgoing requests"""

	def __init__(self):
		token = config_reader()
		self.session = auth(token)

	def get_requests(self, offset=0) -> int:
		self.getRequests = self.session.method("friends.getRequests", {
			"offset": offset,
			"out": 1,
			"count": 100
			})

		return self.getRequests["count"]

	def clear_requests(self):
		self.offset = 0

		for i in range((self.get_requests() // 100) + 1):
			self.get_requests(self.offset)
			for j in self.getRequests["items"]:
				self.session.method("friends.delete", {
					"user_id": j
				})

			self.offset += 100