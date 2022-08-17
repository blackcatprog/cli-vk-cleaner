from configparser import ConfigParser

import vk_api

from utils.auth import auth
from utils.config_tools import config_reader

class Likes_Cleaner:

	def __init__(self):
		token = config_reader()
		self.session = auth(token)

	def get_posts(self, offset=0) -> int:
		self.getPosts = self.session.method("fave.getPosts", {
			"count": 100,
			"offset": offset
		})

		return self.getPosts["count"]

	def get_photos(self, offset=0) -> int:
		self.getPhotos = self.session.method("fave.getPhotos", {
			"count": 100,
			"offset": offset
		})

		return self.getPhotos["count"]

	def get_videos(self, offset=0) -> int:
		self.getVideos = self.session.method("fave.getVideos", {
			"count": 100,
			"offset": offset
		})

		return self.getVideos["count"]

	def clear_likes(self):
		self.offset = 0
		for i in range((self.get_posts() // 100) + 1):
			self.get_posts(self.offset)
			for j in self.getPosts["items"]:
				self.session.method("likes.delete", {
					"type": "post",
					"owner_id": j["owner_id"],
					"item_id": j["id"]
				})
				
			self.offset += len(self.getPosts["items"])

		self.offset = 0
		for i in range((self.get_photos() // 100) + 1):
			self.get_photos(self.offset)
			for j in self.getPhotos["items"]:
				self.session.method("likes.delete", {
					"type": "photo",
					"owner_id": j["owner_id"],
					"item_id": j["id"]
				})

			self.offset += len(self.getPhotos["items"])

		self.offset = 0
		for i in range((self.get_videos() // 100) + 1):
			self.get_videos(self.offset)
			for j in self.getVideos["items"]:
				self.session.method("likes.delete", {
					"type": "video",
					"owner_id": j["owner_id"],
					"item_id": j["id"]
				})

			self.offset += len(self.getVideos["items"])