import tornado.web
import tornado.autoreload
import configparser


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        config = configparser.ConfigParser()
        config.read('./demo/config.txt')
        self.write(config['wechat']['update_time'])

Apprequest = [
    (r'/', MainHandler),
]

Application = tornado.web.Application(
    handlers=Apprequest
)

if __name__ == "__main__":
    Application.listen(5000)
    loop = tornado.ioloop.IOLoop.instance()
    tornado.autoreload.start(loop)
    loop.start()
