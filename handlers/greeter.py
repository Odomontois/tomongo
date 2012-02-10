from tornado.web import RequestHandler
from pymongo import Connection

dbConnection  = Connection()
finDocs = dbConnection.FI.finDocs


class Greeter(RequestHandler):
    "This class is adorable"
    def get(self):
        self.write(dict(
            type = "greeting",
            value = "Hello, dear friend!!!",
            instanceNum = getattr(self,"instanceNum",0)
            ))

class MongoGreeter(RequestHandler):
    def get(self):
        self.write( dict(
            type = "DBgreeting",
            instanceNum = getattr(self,"instanceNum",0),
            doc = finDocs.find(fields = {"_id": 0})            
        ))

