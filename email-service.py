#!.venv/bin/python
import os

import dotenv

dotenv.load_dotenv()

email_account = os.getenv("EMAIL_ACC")

def main():
	print("initializing...")
	send_email(email_account)

def send_email(acc):
	pass
