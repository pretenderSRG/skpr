import os
import dotenv
from flask import Flask


app = Flask(__name__)
dotenv.load_dotenv(override=True)

# if os.environ.get("APP_CONFIG") == "development":
#     app.config.from_pyfile("config/development.py")
# else:
#     app.config.from_pyfile("config/production.py")


# if __name__ =='__main__':
#     app.run()