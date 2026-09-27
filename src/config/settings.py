import os
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv(
    "API_URL",
    "https://jsonplaceholder.typicode.com/todos/1"
)