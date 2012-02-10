import tornado.ioloop
from tornado.options import define, options, logging
import tornado.web
from handlers import Greeter,MongoGreeter

define("instn", default=0, help="tun on port 9900 + %instn%", type=int)

settings = {
    "debug": True,
}

server_settings = {
    "xheaders" : True,
}

class MainHandler(tornado.web.RequestHandler):        
    def get(self):
        self.write("You are welcomed at %s station" %(["alpha", "beta"][getattr(self,"instanceNum",0)-1]))



def main():
    tornado.options.parse_command_line()
    tornado.web.RequestHandler.instanceNum = options.instn
    port = 9900 + options.instn
    logging.info("Starting Tornado web server on http://localhost:%s" % port)
    application = tornado.web.Application([
        (r"/",MainHandler),
        (r"/greet", Greeter),
        (r"/fingreet",MongoGreeter)
        
    ], **settings)
    application.listen(port, **server_settings)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()