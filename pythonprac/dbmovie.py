from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.icgzjjq.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)
db = client.test

target_movie = db.movie.find_one({'title':'가버나움'})
target_star = target_movie['star']

db.movie.update_one({'title':'가버나움'},{'$set':{'star':'0'}})