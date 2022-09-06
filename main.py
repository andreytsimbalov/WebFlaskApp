from app import app
from settings import *

app.run(
    debug=True,
    host=HOST,
    port=PORT
)
