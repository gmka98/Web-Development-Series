from dotenv import load_dotenv

from server import app_maker

load_dotenv()

app = app_maker()
