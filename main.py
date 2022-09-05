from app import app
from app.settings import *

app.run(
    debug=True,
    host=HOST,
    port=PORT
)
