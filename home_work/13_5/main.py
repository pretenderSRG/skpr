import os
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

path = app.config.get("PATH")

print(os.environ.get("PATH"))

# if __name__ =='__main__':
#     app.run()