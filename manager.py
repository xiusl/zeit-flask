from app import app

from mongoengine import connect


connect(MONGO_DB, MONGO_URL)

