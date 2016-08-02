import tornado.web
import configparser
from redis import Redis

config = configparser.ConfigParser()
config.read('config.txt')
redis = Redis(host='redis', port=6379)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
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
    loop.start()
