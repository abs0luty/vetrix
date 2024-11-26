from pymongo import mongo_client
import pymongo
from app.settings import settings

client = mongo_client.MongoClient(settings.MONGO_DATABASE_URL)
print('Connected to MongoDB...')

db = client[settings.MONGO_DATABASE_NAME]
User = db.users
Post = db.posts
User.create_index([("email", pymongo.ASCENDING)], unique=True)
Post.create_index([("title", pymongo.ASCENDING)], unique=True)