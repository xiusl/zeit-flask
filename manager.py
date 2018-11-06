from app import create_app

application = create_app()

import os
MONGO_DB = os.getenv("MONGO_DB") or "heroku_rnz54xf1"
MONGO_URL = os.getenv("MONGO_URL") or "mongodb://127.0.0.1:27017/heroku_rnz54xf1"
print(MONGO_DB)

from mongoengine import connect
connect(alias=MONGO_DB, host=MONGO_URL)


if __name__ == '__main__':
    application.run(debug=True)

