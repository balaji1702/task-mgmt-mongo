import pymongo as mongo

myclient = mongo.MongoClient("mongodb://localhost:27017/")

db=myclient.to_do

task_collection=db.task
 



