from app import create_app

application = create_app()

import os
MONGO_DB = os.getenv("MONGO_DB")
MONGO_URL = os.getenv("MONGO_URL")

from mongoengine import connect
connect(MONGO_DB, MONGO_URL)


if __name__ == '__main__':
    application.run(debug=True)

