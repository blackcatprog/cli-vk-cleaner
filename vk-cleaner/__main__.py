import os
import platform

import vk_api

from modules.wall_cleaner import Wall_Cleaner
from modules.likes_cleaner import Likes_Cleaner
from modules.groups_cleaner import Groups_Cleaner
from modules.friends_cleaner import Friends_Cleaner
from modules.requests_cleaner import Requests_Cleaner
from modules.documents_cleaner import Documents_Cleaner
from utils.config_tools import *
from cli import *

def main():
	try:
		if platform.system() == "Windows":
			os.system("cls")
		else:
			os.system("clear")

		print(banner)
		token = config_reader()

		if token:
			print(modules_all)
			prompt = input(cursor)

			match prompt:
				case "likes":
					print()
					_ = Likes_Cleaner()
					_.clear_likes()
				case "friends":
					print(modules_friends)
					prompt = input(cursor)
					print()

					match prompt:
						case "friends":
							_ = Friends_Cleaner()
							_.clear_friends()
						case "friends_all":
							_ = Friends_Cleaner()
							_.clear_all_friends()
						case _:
							print(r"¯\_(' ͜ ')_/¯")
				case "groups":
					print(modules_groups)
					prompt = input(cursor)
					print()

					match prompt:
						case "friends":
							_ = Groups_Cleaner()
							_.clear_groups()
						case "friends_all":
							_ = Groups_Cleaner()
							_.clear_all_groups()
						case _:
							print(r"¯\_(' ͜ ')_/¯")
				case "requests":
					print()
					_ = Requests_Cleaner()
					_.clear_requests()
				case "documents":
					print()
					_ = Documents_Cleaner()
					_.clear_docs()
				case "wall":
					print()
					_ = Wall_Cleaner()
					_.clear_wall()
				case "99":
					print()
					print("Выход...")
				case _:
					print(r"¯\_(' ͜ ')_/¯")
			print("Очистка завершена!")
		else:
			token = input("Введите токен > ")
			config_creator(token)
	except KeyboardInterrupt:
		print("Выход...")

if __name__ == "__main__":
	main()