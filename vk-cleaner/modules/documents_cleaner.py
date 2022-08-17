from configparser import ConfigParser

import vk_api

from utils.auth import auth
from utils.config_tools import config_reader

class Documents_Cleaner:

	def __init__(self):
		token = config_reader()
		self.session = auth(token)

	def get_docs(self, offset=0) -> int:
		self.getDocuments = self.session.method("docs.get", {
			"offset": offset,
			"count": 100
		})

		return self.getDocuments["count"]

	def clear_docs(self):
		self.offset = 0
		for i in range((self.get_docs() // 100) + 1):
			self.get_docs(self.offset)
			for j in self.getDocuments["items"]:
				self.session.method("docs.delete", {
					"owner_id": j["owner_id"], 
					"doc_id": j["id"]
				})

			self.offset += len(self.getDocuments["items"])